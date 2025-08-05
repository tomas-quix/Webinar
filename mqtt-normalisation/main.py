from quixstreams import Application
from quixstreams.dataframe.windows.aggregations import Last, Count
from datetime import datetime
import os

# for local dev, load env vars from a .env file
# from dotenv import load_dotenv
# load_dotenv()


def main():

    # Setup necessary objects
    app = Application(
        consumer_group="mqtt_norm",
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
    }, metadata=True)

    sdf = sdf.apply(lambda row: {
        "machine": row["machine"],
        "timestamp": row["timestamp"],
        row["sensor_id"]: row["value"]
    })

    sdf = sdf.group_by("machine")

    sdf = sdf.tumbling_window(100, 1000).agg(
        PRINT_SPEED=Last("PRINT_SPEED"),
        BED_TEMPERATURE=Last("BED_TEMPERATURE"),
        NOZZLE_TEMPERATURE=Last("NOZZLE_TEMPERATURE")).final()

    sdf["start"] = sdf["start"].apply(lambda epoch: str(datetime.fromtimestamp(epoch / 1000)))

    sdf = sdf[["start", "PRINT_SPEED", "BED_TEMPERATURE", "NOZZLE_TEMPERATURE"]]

    # Do StreamingDataFrame operations/transformations here
    sdf = sdf.print_table(metadata=False)

    # Finish off by writing to the final result to the output topic
    #sdf.to_topic(output_topic)

    # With our pipeline defined, now run the Application
    app.run()


# It is recommended to execute Applications under a conditional main
if __name__ == "__main__":
    main()