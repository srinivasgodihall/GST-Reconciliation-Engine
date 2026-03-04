# GST Reconciliation & Compliance Automation Engine

## Overview

The GST Reconciliation & Compliance Automation Engine is an enterprise-style tax automation project built using Python.  

This system simulates a real-world corporate workflow where ERP transaction data is reconciled against GSTR-2A vendor-reported data to identify mismatches, detect compliance risks, and generate structured working papers for review.

The project demonstrates practical implementation of tax technology automation concepts including API integration, financial computation logic, reconciliation design, exception reporting, and dashboard development.

---

## Business Problem

In corporate tax environments, reconciliation between internal ERP records and GSTR-2A data is critical to:

- Prevent incorrect Input Tax Credit (ITC) claims  
- Identify vendor filing discrepancies  
- Reduce compliance risk and penalties  
- Improve audit readiness  
- Automate manual working paper preparation  

This project replicates that workflow through a modular Python-based system.

---

## System Architecture

ERP API Data  
→ Data Validation  
→ GST Computation Engine  
→ Simulated GSTR-2A Dataset  
→ Invoice-Level Reconciliation  
→ Mismatch Detection  
→ Exception Classification  
→ Excel Compliance Report  
→ Interactive Dashboard  

---

## Key Features

- REST API integration for transactional data ingestion  
- Automated GST computation (CGST / SGST split)  
- Simulated GSTR-2A dataset generation  
- Invoice-level reconciliation logic  
- Tolerance-based mismatch detection  
- Exception reporting sheet  
- Timestamped Excel working paper generation  
- Interactive dashboard using Streamlit  
- Modular and scalable architecture  
- Configurable GST rate  

---

## Tech Stack

- Python  
- Pandas  
- Requests  
- XlsxWriter  
- Streamlit  

---

## Project Structure
GRCAE/
│
├── app.py
├── main.py
├── config.py
├── api_handler.py
├── gst_processor.py
├── reconciliation.py
├── validator.py
├── report_generator.py
├── requirements.txt
│
├── .gitignore
├── README.md
└── output/


---

## How to Run

### 1. Clone Repository
git clone https://github.com/srinivasgodihall/GST-Reconciliation-Engine.git

cd grcae


---

### 2. Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate


Mac/Linux:
python3 -m venv venv
source venv/bin/activate


---

### 3. Install Dependencies
pip install -r requirements.txt


---

### 4. Run Excel Reconciliation Engine
python main.py

Output:  
Timestamped Excel file generated inside `/output` folder.

---

### 5. Run Interactive Dashboard
streamlit run app.py


Open the local URL shown in terminal to access the dashboard.

---

## Dashboard Capabilities

- Adjustable GST rate  
- Real-time reconciliation execution  
- Invoice-level reconciliation table  
- Total mismatch metrics  
- Category-wise GST visualization  

---

## What This Project Demonstrates

- API-based data ingestion  
- Financial logic implementation  
- Reconciliation engine design  
- Compliance exception management  
- Automated Excel reporting  
- Interactive executive dashboard creation  
- Enterprise-style modular architecture  

---

## Practical Relevance

This project simulates workflows typically performed in:

- Tax Technology teams  
- Risk Advisory functions  
- Corporate tax departments  
- Compliance automation roles  
- Data-driven audit environments  

---

## Future Enhancements

- Risk scoring model for mismatch severity  
- Database integration (PostgreSQL / SQLite)  
- FastAPI backend deployment  
- Unit testing framework  
- Scheduled batch execution  
- Cloud deployment (AWS / Azure)  

---

## Author

Srinivas Godihall  

