"""Ping sweep: find which hosts are alive on a small network.

Only scan networks you own or have permission to scan.

Usage:
    python ping_sweep.py 192.168.1.0/24
"""
import ipaddress
import platform
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


def is_alive(ip):
    # Windows uses -n for count and -w (ms) for timeout; Linux/Mac use -c and -W (s)
    if platform.system() == "Windows":
        cmd = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0  # 0 means we got a reply


def main():
    if len(sys.argv) < 2:
        print("Usage: python ping_sweep.py 192.168.1.0/24")
        return
    try:
        net = ipaddress.ip_network(sys.argv[1], strict=False)
    except ValueError:
        print("Enter a network like 192.168.1.0/24")
        return
    if net.num_addresses > 256:
        print("Too big for this tool. Use /24 or smaller.")
        return

    if not shutil.which("ping"):
        print("The ping command isn't available on this computer.")
        return

    hosts = list(net.hosts())
    print(f"Pinging {len(hosts)} addresses...")
    # Ping many hosts at once so a /24 finishes in seconds, not minutes
    with ThreadPoolExecutor(max_workers=50) as pool:
        results = list(pool.map(is_alive, hosts))

    alive = [str(ip) for ip, up in zip(hosts, results) if up]
    for ip in alive:
        print(f"  {ip} is up")
    print(f"Done: {len(alive)} of {len(hosts)} responded.")
    print("Note: some devices block ping, so a silent host isn't always offline.")


if __name__ == "__main__":
    main()
