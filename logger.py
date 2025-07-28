import logging

logging.basicConfig(filename="firewall.log", level=logging.INFO)

def log_packet(packet):
    logging.info(f"Blocked packet: {packet.summary()}")
