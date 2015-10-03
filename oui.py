
import re

lines = []
with open("/usr/share/wireshark/manuf") as f:
    lines = f.readlines()
    
e = [re.split("\s+", s, 3) for s in lines]

table = {str(p[0]) : str(p[-1]) for p in e if len(p[0]) == 8}

def oui_lookup(mac):
    key = mac[0:8].upper()
    if key in table:
        return table[key]
    else:
        return "Unknown"
    