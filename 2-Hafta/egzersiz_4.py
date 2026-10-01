with open("show_arp.txt","r") as f:
    show_arp = f.readlines()

print(f"'show_arp' variable data type'ı: {type(show_arp)}")
len_show_arp = len(show_arp)
print("*" * 50)
print(f"'show_arp' variable length: '{len_show_arp}'")
print("*" * 50)
print(f"'show_arp' ilk satırı: {show_arp[0]}")
print("*" * 50)
print(f"'show_arp' tabular data ilk satırı: {show_arp[1]} \n'show_arp' son satırı: {show_arp[-1]}")
print("*" * 50)

fields = show_arp[0].split()
print(f"'show_arp' fields: {fields}")
print("*" * 50)

print(f"'fields' variable data type'ı: {type(fields)}")
print("*" * 50)

len_show_fields = len(fields)
print(f"'fields' variable length: '{len_show_fields}'")  # (min) ve Addr kısmını dahil ettim şimdilik tabii
print("*" * 50)

print(f"Birinci fields item: {fields[0]} \nSonuncu fields item: {fields[-1]}")
print("*" * 50)

del fields[3]
fields[3] = "Hardware_Addr"
del fields[4]

print(f"'show_arp' fields: {fields}")

len_show_fields = len(fields)
print(f"'fields' variable length: '{len_show_fields}'")