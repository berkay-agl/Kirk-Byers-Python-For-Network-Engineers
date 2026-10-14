vlans = [
    {
        "vlanshowbr-vlanid": "1",
        "vlanshowbr-vlanid-utf": "1",
        "vlanshowbr-vlanname": "default",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "2",
        "vlanshowbr-vlanid-utf": "2",
        "vlanshowbr-vlanname": "VLAN0002",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "3",
        "vlanshowbr-vlanid-utf": "3",
        "vlanshowbr-vlanname": "VLAN0003",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "4",
        "vlanshowbr-vlanid-utf": "4",
        "vlanshowbr-vlanname": "VLAN0004",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
]


for vlan in vlans:
    vlan_id = vlan["vlanshowbr-vlanid"]
    vlan_name = vlan["vlanshowbr-vlanname"]
    print(f"VLAN NAME: {vlan_name} \n VLAN ID: {vlan_id}")