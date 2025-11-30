# Kinesis LocalStream Dashboard

A complete **real-time data streaming project** using **AWS Kinesis, LocalStack, Python, and Streamlit**.  
This project simulates IoT devices sending temperature data to Kinesis streams and visualizes it live on a Streamlit dashboard.

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

### 1. Clone the repository
```bash
git clone https://github.com/abc/project.git
cd project
```

### 2. Create virtual environment
```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate   # Windows
```

```bash
source .venv/bin/activate # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Docker
```bash
docker-compose up
```

### 5. Run producer
```bash
python producer.py
```

### 6. Run dashboard
```bash
streamlit run dashboard.py
```
