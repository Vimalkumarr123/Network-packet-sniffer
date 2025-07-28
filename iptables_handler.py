import os

def block_ip(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")
