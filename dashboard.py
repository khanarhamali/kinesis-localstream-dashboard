# dashboard.py
import streamlit as st
import boto3
import json
import time
import pandas as pd

# ---------- Kinesis Client (LocalStack) ----------
kinesis = boto3.client(
    "kinesis",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url="http://localhost:4566"
)

st.title("Kinesis Stream Dashboard")
st.markdown("Live data from Kinesis stream `stream1`")

# ---------- DataFrame to store incoming data ----------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["device_id", "temperature", "timestamp"])

# ---------- Function to fetch records ----------
def fetch_records():
    try:
        shard_id = kinesis.describe_stream(StreamName="stream1")["StreamDescription"]["Shards"][0]["ShardId"]
        shard_iterator = kinesis.get_shard_iterator(
            StreamName="stream1",
            ShardId=shard_id,
            ShardIteratorType="LATEST"
        )["ShardIterator"]

        response = kinesis.get_records(ShardIterator=shard_iterator, Limit=10)
        records = response.get("Records", [])
        data_list = []
        for record in records:
            payload = json.loads(record["Data"])
            data_list.append(payload)
        return data_list
    except Exception as e:
        st.error(f"Error fetching records: {e}")
        return []

# ---------- Main loop ----------
placeholder = st.empty()
AUTO_REFRESH_INTERVAL = 2  # seconds
TEMPERATURE_THRESHOLD = 50  # example threshold

while True:
    new_records = fetch_records()
    if new_records:
        df_new = pd.DataFrame(new_records)
        if not df_new.empty:
            st.session_state.df = pd.concat([st.session_state.df, df_new], ignore_index=True)

    with placeholder.container():
        st.subheader("Recent Records")
        if not st.session_state.df.empty:
            st.dataframe(st.session_state.df.tail(20))  # last 20 rows

            st.subheader("Average Temperature Chart")
            # Average temperature per timestamp
            df_avg = st.session_state.df.groupby("timestamp")["temperature"].mean().reset_index()
            st.line_chart(df_avg.rename(columns={"timestamp":"index"}).set_index("index"))

            # High temperature alert per device
            high_temp_df = st.session_state.df[st.session_state.df["temperature"] > TEMPERATURE_THRESHOLD]
            if not high_temp_df.empty:
                for _, row in high_temp_df.iterrows():
                    st.error(f"🔥 High temperature alert! Device {row['device_id']} = {row['temperature']:.2f}°C")

            # Firehose → local S3 simulation
            st.subheader("Firehose → Local S3 Simulation")
            st.write("Simulated push to S3:")
            st.json(st.session_state.df.tail(5).to_dict(orient="records"))

    time.sleep(AUTO_REFRESH_INTERVAL)
