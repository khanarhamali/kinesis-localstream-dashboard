import boto3
import json
import time

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

while True:
    records = kinesis.get_records(ShardIterator=shard_it, Limit=10)
    shard_it = records["NextShardIterator"]

    for r in records["Records"]:
        print("Received:", json.loads(r["Data"]))

    time.sleep(1)
