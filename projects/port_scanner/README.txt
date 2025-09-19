 What
A simple TCP port scanner written in Python to demonstrate how sockets work.  
⚠️ Use only on systems you own or are authorized to test.

---

## ▶️ How to run
1. Make sure you have Python 3 installed.
2. Run the script from the terminal:

```bash
python3 port_scanner.py <host> <start_port>-<end_port>
 example:- python3 port_scanner.py 127.0.0.1 0-65535

   THIS SCRIPT IS ONLY TO SHOW HOW THE NETWORK SCAN WORK
  

                        MORE DETAILS INFORMATION

Port Scanner

A simple Python-based port scanner that allows you to check open ports on a target IP address or domain. This tool is useful for cybersecurity learning, network testing, and penetration testing practice.

Features

Scan a single host for open ports.

Scan a range of ports.

Display open ports with service information (optional enhancement).

Lightweight and easy to use.

Installation

Clone the repository:

git clone https://github.com/your-username/port_scanner.git


Navigate to the project directory:

cd port_scanner


Install required dependencies (if any). This scanner uses Python's standard libraries, so no external modules are needed:

# No installation needed if using standard libraries

Usage

Open a terminal and run the script:

python port_scanner.py


Enter the target IP address or domain:

Enter target IP or domain: 192.168.1.1


Enter the port range you want to scan (optional):

Enter start port: 1
Enter end port: 1000


The script will display all open ports on the target.

Example Output
Scanning 192.168.1.1...
Port 22 is open
Port 80 is open
Port 443 is open
Scan completed.

How It Works

The scanner uses Python's socket module to attempt connections to the target ports.

If the connection is successful, the port is considered open.

If the connection fails, the port is closed or filtered.

Disclaimer

This tool is intended for educational purposes only.

Scanning networks without permission is illegal. Always obtain proper authorization before scanning any network.
