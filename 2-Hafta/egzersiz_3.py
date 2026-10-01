ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
print(f"Başlangıç listesi: {ip_list}")

ip_list.append("192.168.1.6")
ip_list.extend(["192.168.1.7", "192.168.1.8"])
ip_list = ip_list + ["192.168.1.9", "192.168.1.10"]

print(f"Güncel tüm liste: {ip_list}")
print(f"Birinci IP Adresi: {ip_list[0]}")
print(f"Sonuncu IP Adresi: {ip_list[-1]}")

delete_ip_1 = ip_list.pop(0)
print(f"Silinen IP Adresi: {delete_ip_1}")
dalete_ip_2 = ip_list.pop(-1)
print(f"Silinen IP Adresi: {dalete_ip_2}")

print(f"Güncel tüm liste: {ip_list}")

ip_list[0] = "2.2.2.2"

print(f"Yeni IP adresi: {ip_list[0]}")
