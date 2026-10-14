filename = "arubacx_show_vlan.txt"
with open(filename) as f:
    data = f.read()

vlan_map = {}
for line in data.splitlines():
    if "----" in line or "Status" in line or not line.strip():
        continue

    parts = line.split()
    vlan_id = parts[0]
    interfaces = parts[-1]

    intf_groups = interfaces.split(",")

    intf_list = []
    for intf in intf_groups:
        if "-" in intf:
            intf_start, intf_end = intf.split("-")

            if "/" in intf_start:
                base_intf = intf_start.rsplit("/", 1)[0] + "/"
                start_idx = int(intf_start.split("/")[-1])
                end_idx = int(intf_end.split("/")[-1])

            elif "lag" in intf_start:
                base_intf = "lag"
                start_idx = int(intf_start.replace("lag", ""))
                end_idx = int(intf_end.replace("lag", ""))

            new_intf = [f"{base_intf}{idx}" for idx in range(start_idx, end_idx + 1)]
            intf_list.extend(new_intf)

        else:
            intf_list.append(intf)

    vlan_map[int(vlan_id)] = set(intf_list)

print()
print("Section a.")
print("-" * 25)
shared_intf = vlan_map[1] & vlan_map[2] & vlan_map[3]
print(f"Common interfaces VLAN1, VLAN2, VLAN3: {shared_intf}")
print()

all_intf = {intf for intf_set in vlan_map.values() for intf in intf_set}
print("Section b.")
print("-" * 25)
print(f"All interfaces that belong to a VLAN:\n{all_intf}")
print()

vlan_12_13 = vlan_map[12] | vlan_map[13]
print("Section c.")
print("-" * 25)
print(f"All interfaces associated with VLAN12 or VLAN13 (in either):\n{vlan_12_13}")
print()