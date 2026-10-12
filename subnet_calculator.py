"""Subnet calculator: enter an IP with a prefix, get the network details.

Usage:
    python subnet_calculator.py 192.168.1.10/24
    python subnet_calculator.py            (it will ask you)
"""
import ipaddress
import sys


def main():
    # Take the address from the command line, or ask for it
    text = sys.argv[1] if len(sys.argv) > 1 else input("Enter IP/prefix (e.g. 192.168.1.10/24): ")

    try:
        # strict=False lets you type a host address, not just a network address
        net = ipaddress.ip_network(text.strip(), strict=False)
    except ValueError:
        print("That doesn't look like a valid IP/prefix, e.g. 192.168.1.10/24")
        return

    hosts = list(net.hosts())  # usable addresses (no network/broadcast)

    print(f"Network address : {net.network_address}")
    print(f"Broadcast       : {net.broadcast_address}")
    print(f"Subnet mask     : {net.netmask}")
    print(f"Wildcard mask   : {net.hostmask}")
    print(f"Prefix length   : /{net.prefixlen}")
    if hosts:
        print(f"Usable range    : {hosts[0]} - {hosts[-1]}")
    print(f"Usable hosts    : {len(hosts)}")


if __name__ == "__main__":
    main()
