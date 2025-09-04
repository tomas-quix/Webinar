# import the Quix Streams modules for interacting with Kafka.
# For general info, see https://quix.io/docs/quix-streams/introduction.html
from quixstreams import Application
from quixstreams.dataframe.joins.lookups import QuixConfigurationService, QuixConfigurationServiceJSONField as Field

import os

# for local dev, load env vars from a .env file
# from dotenv import load_dotenv
# load_dotenv()


def main():
 
    # Setup necessary objects
    app = Application(
        consumer_group="data_encrichment_v1",
        auto_create_topics=True,
        auto_offset_reset="earliest"
    )
    input_topic = app.topic(name=os.environ["input"], key_deserializer="str")
    output_topic = app.topic(name=os.environ["output"])
    config_topic = app.topic(name=os.environ["config_topic"])

    sdf = app.dataframe(topic=input_topic)

    enricher = QuixConfigurationService(
        topic=config_topic,
        app_config=app.config,
    )

    # Enrich data using defined configs (lookup_join)
    sdf = sdf.join_lookup(
        lookup=enricher,
        fields={
            "location": Field(
                type="experiment-cfg",
                default=None,
                jsonpath="location"
            ),
            "mapping": Field(
                type="experiment-cfg",
                default={},
                jsonpath="mapping"
            ),
        }
    )

    sdf.print()
    
    # Finish off by writing to the final result to the output topic
    sdf.to_topic(output_topic)

    # With our pipeline defined, now run the Application
    app.run()


# It is recommended to execute Applications under a conditional main
if __name__ == "__main__":
    main()