#!/usr/bin/env python3
# port_scanner.py
# Simple TCP port scanner for learning/demo purposes.
# ⚠️ Use only on systems you own or have explicit permission to scan.

import socket
import sys
from datetime import datetime

def scan_host(host, ports):
    print(f"Scanning {host} ports {ports[0]}-{ports[-1]}")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Could not resolve host:", host)
        return

    start = datetime.now()
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except Exception:
            pass
    end = datetime.now()

    print("Open ports:", open_ports if open_ports else "None found")
    print("Scan time:", end - start)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 port_scanner.py <host> <start_port>-<end_port>")
        sys.exit(1)

    host = sys.argv[1]
    rng = sys.argv[2].split('-')
    start_p = int(rng[0]); end_p = int(rng[1])
    if start_p > end_p:
        start_p, end_p = end_p, start_p

    ports = list(range(start_p, end_p + 1))
    scan_host(host, ports)

