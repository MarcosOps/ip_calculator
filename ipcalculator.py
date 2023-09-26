import ipaddress




def main():
    print("IP Calculator")
    while True:
        choice = input("1. Subnet Calculation\n2. Exit\nEnter your choice: ")

        if choice == '1':
            subnet_calculation()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def subnet_calculation():
    ip = input("Enter IP address: ")
    subnet_mask_str = input("Enter subnet mask (e.g., 255.255.255.0 or 24): ")

    try:
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask_str}", strict=False)
        start_ip = network.network_address + 1
        end_ip = network.broadcast_address - 1
        subnet_mask = network.netmask
        wildcard_mask_int = ~int(subnet_mask) & 0xFFFFFFFF
        wildcard_mask = ipaddress.IPv4Address(wildcard_mask_int)
        total_ips = network.num_addresses
        usable_ip = network.num_addresses - 2
        print( " ")
        print(f"#   Network Address: {network.network_address}")
        print(f"#   Broadcast Address: {network.broadcast_address}")
        print(f"#   Start IP: {start_ip}")
        print(f"#   Last IP: {end_ip}")
        print(f"#   Total IPs: {total_ips}")
        print(f"#   Total Usable IPs: {usable_ip}")
        print(f"#   Subnet Mask: {network.netmask}")
        print(f"#   Wildcard Mask: {wildcard_mask}")
        print(f"#   Binary Subnet Mask: {'.'.join(format(int(octet), '08b') for octet in subnet_mask.packed)}")
        print(f"#   CIDR Notation: /{network.prefixlen}")
        print(f"#   IP Type: {get_ip_type(ip)}")
        print(f"#   IP Class: {get_ip_class(ip)}")
        #print(f"#   6to4 Prefix: {get_6to4_prefix(ip)}")
        print( " ")
    except ipaddress.AddressValueError:
        print("Invalid IP address or subnet mask.")
    except ipaddress.NetmaskValueError:
        print("Invalid subnet mask format.")


def get_ip_class(ip):
    first_octet = int(ip.split(".")[0])
    if 1 <= first_octet <= 126:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224 <= first_octet <= 239:
        return "D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "E (Reserved)"

def get_ip_type(ip):
    ip = ipaddress.IPv4Address(ip)
    if ip.is_private:
        return "Private"
    elif ip.is_reserved or ip.is_loopback or ip.is_link_local or ip.is_multicast:
        return "Reserved"
    else:
        return "Public"

def get_6to4_prefix(ip):
    ip = ipaddress.IPv4Address(ip)
    if ip.is_private:
        return "N/A (Private IP)"
    else:
        prefix = ipaddress.IPv6Network(f"2002:{ip}/48")
        return prefix

if __name__ == "__main__":
    main()
