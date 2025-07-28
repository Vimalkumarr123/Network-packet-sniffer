from scapy.all import sniff
from utils import check_packet_against_rules
from logger import log_packet

def process_packet(packet):
    if not check_packet_against_rules(packet):
        log_packet(packet)
        print("Blocked:", packet.summary())
    else:
        print("Allowed:", packet.summary())

if __name__ == "__main__":
    print("[+] Starting Firewall...\n")
    sniff(prn=process_packet, store=0)
