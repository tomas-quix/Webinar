# import the Quix Streams modules for interacting with Kafka.
# For general info, see https://quix.io/docs/quix-streams/introduction.html
from quixstreams import Application
from quixstreams.dataframe.joins.lookups import QuixConfigurationService

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
    input_topic = app.topic(name=os.environ["input"])
    output_topic = app.topic(name=os.environ["output"])
    config_topic = app.topic(name=os.environ["CONFIG_TOPIC"])

    sdf = app.dataframe(topic=input_topic)

    enricher = QuixConfigurationService(
        topic=config_topic,
        app_config=app.config,
    )

    # Enrich data using defined configs (lookup_join)
    sdf = sdf.join_lookup(
        lookup=enricher,
        fields={
            "editor_name": Field(
                type="printer-config",
                default=None,
                jsonpath="editor_name"
            ),
            "field_scalar": Field(
                type="printer-config",
                default=1.0,
                jsonpath="field_scalar"
            ),
            "mapping": Field(
                type="printer-config",
                default={},
                jsonpath="mapping"
            ),
        }
    ).apply(config_apply)

    # Finish off by writing to the final result to the output topic
    sdf.to_topic(output_topic, key=lambda row: row["machine"])

    # With our pipeline defined, now run the Application
    app.run()

    # Finish off by writing to the final result to the output topic
    sdf.to_topic(output_topic)

    # With our pipeline defined, now run the Application
    app.run()


# It is recommended to execute Applications under a conditional main
if __name__ == "__main__":
    main()