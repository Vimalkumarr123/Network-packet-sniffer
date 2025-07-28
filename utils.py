import json

def load_rules():
    with open("rules.json") as f:
        return json.load(f)

rules = load_rules()

def check_packet_against_rules(packet):
    src_ip = packet[0][1].src if packet.haslayer(1) else ""
    dst_ip = packet[0][1].dst if packet.haslayer(1) else ""
    proto = packet.proto if hasattr(packet, 'proto') else ""
    sport = packet.sport if hasattr(packet, 'sport') else None
    dport = packet.dport if hasattr(packet, 'dport') else None

    for rule in rules:
        if rule["action"] == "block":
            if "ip" in rule and (src_ip == rule["ip"] or dst_ip == rule["ip"]):
                return False
            if "port" in rule and (sport == rule["port"] or dport == rule["port"]):
                return False
            if "protocol" in rule and rule["protocol"].lower() in str(proto).lower():
                return False
    return True
