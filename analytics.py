import json
from datetime import datetime
import time

print("Analytic engine running...")

buffer = []
window_size = 5  # 5 records

while True:
    try:
        with open("s3_out/data.json") as f:
            lines = f.readlines()
    except:
        lines = []

    # only process new lines
    for line in lines[-window_size:]:
        try:
            record = json.loads(line)
            buffer.append(record)
        except:
            pass

    if len(buffer) >= window_size:
        avg_temp = sum([i["temperature"] for i in buffer]) / len(buffer)
        print(f"Window Avg Temp = {avg_temp:.2f}")

        buffer = []

    time.sleep(3)
