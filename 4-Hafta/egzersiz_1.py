ip_dict = {}

with open("show_ip_int_brief.txt", mode="r") as f:
    file = f.read().splitlines()
    for line in file:
        if "unassigned" not in line:
            line = line.split()
            if "YES" in line:
                interface = line[0]
                ip_address = line[1]
                ip_dict[interface] = ip_address

print(ip_dict)