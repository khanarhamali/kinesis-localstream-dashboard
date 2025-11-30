import boto3
import json
import time
import random

kinesis = boto3.client(
    "kinesis",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",            # required for LocalStack
    aws_secret_access_key="test"         # required for LocalStack
)

while True:
    data = {
        "device_id": random.randint(1, 5),
        "temperature": round(random.uniform(20, 80), 2),
        "timestamp": time.time()
    }

    print("Sending:", data)

    kinesis.put_record(
        StreamName="stream1",                 # same stream name as created
        Data=json.dumps(data),
        PartitionKey=str(data["device_id"])
    )

    time.sleep(1)
