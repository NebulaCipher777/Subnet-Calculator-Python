# Subnet Calculator

import ipaddress

# Ask user for input
ip = input("Enter an IP address: ")
subnet_mask = input("Enter a subnet mask (prefix length or dotted decimal): ")

# Create an IPv4Network object
network = ipaddress.ip_network(f"{ip}/{subnet_mask}", strict=False)

# Display subnet information
print("\n--- Subnet Information ---")
print(f"Network Address: {network.network_address}")
print(f"Broadcast Address: {network.broadcast_address}")
print(f"Subnet Mask: {network.netmask}")
print(f"Number of Hosts: {network.num_addresses - 2}")  # Exclude network and broadcast addresses

# First and Last usable hosts
hosts = list(network.hosts())

if hosts:
    print(f"First Usable Host: {hosts[0]}")
    print(f"Last Usable Host: {hosts[-1]}") 