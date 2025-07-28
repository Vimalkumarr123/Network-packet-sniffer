# 🔍 Network Packet Sniffer with Alert System

**Author:** Vimal Kumar R  
**Tech Stack:** Python, Scapy, SQLite, Matplotlib, Tkinter

## 📌 Project Overview

This project is a real-time **Network Packet Sniffer** that monitors incoming and outgoing packets, detects suspicious behavior (like port scanning), logs all traffic into a local database, and optionally displays live traffic summaries through a GUI.

---

## 🎯 Features

- ✅ Real-time packet sniffing using **Scapy**
- 🚨 Anomaly detection (e.g., port scanning)
- 🗃️ Logging of packets into **SQLite**
- 📊 Live traffic statistics via **GUI**
- 📁 Custom alerts logged to file (`alerts.log`)

---

## 📁 Folder Structure

custom_sniffer/
│
├── sniffer.py # Main sniffer engine
├── analyzer.py # Port scan & anomaly detection
├── db_logger.py # SQLite database logger
├── alerts.py # Alert handling logic
├── gui.py # Traffic visualization (Tkinter + Matplotlib)
├── requirements.txt # Dependency list
└── packets.db # Auto-generated SQLite DB

yaml
Copy
Edit

---

## 🛠 Installation & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
If using Linux, you might need to run the script with sudo for sniffing permissions.

2. Run Packet Sniffer (CLI Mode)
bash
Copy
Edit
python sniffer.py
3. Launch GUI Dashboard (Live Stats)
bash
Copy
Edit
python gui.py
GUI shows protocol distribution of captured packets in real-time.

🧠 Anomaly Detection Logic
The sniffer detects port scans by:

Tracking how many unique ports a source IP attempts to access.

If the number of ports accessed within a 10-second window exceeds 20, it triggers an alert.

Alerts are printed in console and stored in:

lua
Copy
Edit
alerts.log
💾 SQLite Logging
Each packet is logged with:

Source & Destination IP

Protocol

Source & Destination Port

Packet Length

Timestamp

You can query the database using:

bash
Copy
Edit
sqlite3 packets.db
📸 GUI Preview
GUI shows live protocol-based bar chart for real-time analysis.

🧩 To-Do / Ideas for Improvement
 Email alerts for severe anomalies

 Add support for ICMP/UDP protocol classification

 Filtering rules (e.g., block certain IPs)

 Export data to CSV/JSON

 Dark mode GUI
```

👨‍💻 Author
Vimal Kumar R
