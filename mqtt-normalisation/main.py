from quixstreams import Application

import os

# for local dev, load env vars from a .env file
# from dotenv import load_dotenv
# load_dotenv()


def main():

    # Setup necessary objects
    app = Application(
        consumer_group="my_transformation",
        auto_create_topics=True,
        auto_offset_reset="earliest"
    )
    input_topic = app.topic(name=os.environ["input"], key_deserializer="str")
    output_topic = app.topic(name=os.environ["output"])
    sdf = app.dataframe(topic=input_topic)

    sdf  = sdf.apply(lambda value, key, timestamp, h: {
        "machine": key.split("/")[0],
        "sensor_id": key.split("/")[1],
        "timestamp": timestamp,
        "value": value
    })

    # Do StreamingDataFrame operations/transformations here
    sdf = sdf.print_table(metadata=True)

    # Finish off by writing to the final result to the output topic
    #sdf.to_topic(output_topic)

    # With our pipeline defined, now run the Application
    app.run()


# It is recommended to execute Applications under a conditional main
if __name__ == "__main__":
    main()