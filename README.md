# Kinesis LocalStream Dashboard

A complete **real-time data streaming project** using **AWS Kinesis, LocalStack, Python, and Streamlit**.  
Kinesis LocalStream Dashboard is a fully functional local simulation of an AWS Kinesis streaming pipeline using LocalStack, designed for IoT data streaming, live analytics, and visualization. This project demonstrates how multiple IoT devices can send real-time temperature data to a Kinesis stream, which can then be visualized through a Streamlit dashboard with live charts, alerts, and multi-device comparison.

It includes a Firehose simulation that writes stream data to a local S3 bucket, enabling end-to-end testing of streaming workflows without requiring a live AWS account. This repository is ideal for developers, data engineers, and students learning real-time data streaming, AWS Kinesis, IoT analytics, and Python-based dashboards.
---

## Features

- ✅ Real-time data ingestion from multiple simulated devices
- ✅ AWS Kinesis Stream simulation via LocalStack
- ✅ Streamlit dashboard with live temperature charts
- ✅ Firehose → local S3 simulation
- ✅ Alerts when device temperature exceeds threshold
- ✅ Multi-device comparison
- ✅ Auto-refresh every 2 seconds

---

## Tech Stack

- Python 3.12  
- Boto3 (AWS SDK for Python)  
- LocalStack (Local AWS cloud simulation)  
- Streamlit (Interactive dashboard)  
- Docker (LocalStack container)

---
## Project Structure

E:\kinesis-local-project
│
├── producer.py # Simulates IoT devices sending data
├── consumer.py # Reads data from Kinesis stream
├── dashboard.py # Streamlit dashboard visualizing live data
├── firehose_sim.py # Simulates Kinesis Firehose → local S3
├── analytics.py # Data processing and analytics
├── docker-compose.yml # Docker setup for LocalStack
├── requirements.txt # Python dependencies
└── .venv/ # Virtual environment (ignored in git)

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/khanarhamali/kinesis-localstream-dashboard.git
cd kinesis-local-project



2. **Create and activate Python virtual environment:**
```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate  # Mac/Linux


3. **Install dependencies:**
```bash
pip install -r requirements.txt


4. **Start LocalStack via Docker:**
```bash
docker-compose up

5. **Run producer to send data:**
```bash
python producer.py


6. **Run Streamlit dashboard:**
```bash
streamlit run dashboard.py

---

## Notes

Make sure Docker is running before starting LocalStack.

Use the dashboard to monitor real-time temperature data and alerts.

Virtual environment .venv/ is ignored in GitHub to avoid large commits.
