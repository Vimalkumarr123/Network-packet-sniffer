import sqlite3
from datetime import datetime

conn = sqlite3.connect("packets.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_ip TEXT, dst_ip TEXT,
    protocol TEXT, src_port INTEGER,
    dst_port INTEGER, length INTEGER,
    timestamp TEXT
)
""")
conn.commit()

def log_packet(src, dst, proto, sport, dport, length):
    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO packets (src_ip, dst_ip, protocol, src_port, dst_port, length, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (src, dst, str(proto), sport, dport, length, timestamp))
    conn.commit()
