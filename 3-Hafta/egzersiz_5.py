file = open("junos_show_arp.txt", mode="r")

for line in file:
    fields = line.split()

    if len(fields) >= 2 and ":" in fields[0] and "." in fields[1]:
        mac_addr = fields[0]
        ip_addr = fields[1]

        alt_mac_addr = mac_addr.replace(":", "-")

        print(f"IP: {ip_addr}  -->  MAC: {alt_mac_addr}")

file.close()