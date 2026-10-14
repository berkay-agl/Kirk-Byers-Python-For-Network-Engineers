all_interfaces = {}

with open("show_ip_int_brief.txt", mode="r") as f:
    file = f.read().splitlines()
    for line in file:
        if not line or "Interface" in line:
            continue
            
        line = line.split()
        interface = line[0]
        ip_addr = line[1]
        line_status = " ".join(line[4:-1])  
        line_protocol = line[-1]
        
        all_interfaces[interface] = {
            "ip_addr": ip_addr,
            "line_status": line_status,
            "line_protocol": line_protocol
        }

print(all_interfaces["GigabitEthernet0/0/0"])
print(all_interfaces["GigabitEthernet0/0/1"])
