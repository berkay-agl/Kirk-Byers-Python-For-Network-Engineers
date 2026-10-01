intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()
intf_name, intf_ip_addr = intf_fields[0],intf_fields[1]
intf_status, intf_protocol = intf_fields[-2],intf_fields[-1]
print(f"Interface Name: {intf_name} - Interface IP Address: {intf_ip_addr}")
print(f"Interface Status: {intf_status} - Interface Protocol: {intf_protocol}")

status = intf_status == "up" and intf_protocol == "up"
print(status)