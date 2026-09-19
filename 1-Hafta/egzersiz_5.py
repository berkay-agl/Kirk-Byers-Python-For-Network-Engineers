#!/usr/bin/env python

ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"

print("String concatenation")
print(ip_addr + " --> " + mac_addr)

print()

print("F-string concatenation")
print(f"{ip_addr} --> {mac_addr}")

print()

print(".format() concatenation")
print("{} --> {}".format(ip_addr, mac_addr))