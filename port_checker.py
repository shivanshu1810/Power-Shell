"""Port checker: is the service reachable? A first step for "the app can't connect".

Usage:
    python port_checker.py example.com            (checks common ports)
    python port_checker.py 192.168.1.20 3389 22   (checks only these ports)
"""
import socket
import sys

# Common ports a help desk tech runs into
COMMON = {
    22: "SSH", 25: "SMTP", 53: "DNS", 80: "HTTP", 443: "HTTPS",
    445: "SMB (file shares)", 3389: "RDP", 3306: "MySQL",
}


def is_open(host, port, timeout=2):
    # connect_ex returns 0 when the connection succeeds
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python port_checker.py HOST [PORT ...]")
        return
    host = sys.argv[1]
    ports = [int(p) for p in sys.argv[2:]] or list(COMMON)

    try:
        ip = socket.gethostbyname(host)  # also a quick DNS check
    except socket.gaierror:
        print(f"Could not resolve {host}. Check the name or DNS first.")
        return

    print(f"Checking {host} ({ip})")
    for port in ports:
        name = COMMON.get(port, "")
        state = "OPEN" if is_open(ip, port) else "closed/filtered"
        print(f"  {port:<6} {name:<18} {state}")


if __name__ == "__main__":
    main()
