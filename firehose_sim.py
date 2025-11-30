import boto3
import json
import time
import os

if not os.path.exists("s3_out"):
    os.makedirs("s3_out")

kinesis = boto3.client(
    "kinesis",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566"
)

shard_it = kinesis.get_shard_iterator(
    StreamName="stream1",
    ShardId="shardId-000000000000",
    ShardIteratorType="LATEST"
)["ShardIterator"]

file = open("s3_out/data.json", "a")

while True:
    records = kinesis.get_records(ShardIterator=shard_it, Limit=100)
    shard_it = records["NextShardIterator"]

    for r in records["Records"]:
        file.write(r["Data"].decode() + "\n")
        print("Saved to S3 folder:", r["Data"].decode())

    file.flush()
    time.sleep(2)
