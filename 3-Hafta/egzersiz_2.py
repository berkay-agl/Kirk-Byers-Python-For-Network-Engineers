file = open("show_ip_int_brief.txt", mode="r")

for line in file:
    if "10.220" in line:
        fields = line.split()
        intf_name = fields[0]
        ip_addr = fields[1]

        print(f"intf_name: {intf_name}")
        print(f"ip_addr: {ip_addr}")

file.close()