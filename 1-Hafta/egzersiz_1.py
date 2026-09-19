#!/usr/bin/env python

sf_gw1 = "172.31.255.1/24"
sf_gw2 = input("İkinci bir IP adresi gir: ")  # 172.40.255.1/24
header = "-" * 20

print(f"{'sf_gw1':^20} {'sf_gw2':^20}")
print(f"{header} {header}")
print(f"{sf_gw1:^20} {sf_gw2:^20}")