file = open("show_ip_int_brief.txt", mode="r")

ip_list = []
intf_list = []

for line in file:
    if "10." in line:
        fields = line.split()
        intf_name = fields[0]
        ip_addr = fields[1]

        intf_list.append(intf_name)
        ip_list.append(ip_addr)

file.close()

print("Interfaces:", intf_list)
print("IP Addresses:", ip_list)