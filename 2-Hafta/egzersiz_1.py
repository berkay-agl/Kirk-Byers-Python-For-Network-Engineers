base_address = "192.168.254."

sub_pre_len = int(input("25 ile 30 arasında bir subnet prefix length giriniz: "))

sub_size = 2 ** (32 - sub_pre_len)
hosts = sub_size - 2

print(f"Host sayısı: {hosts}")

net1 = f"{base_address}0"
net2 = f"{base_address}{sub_size}"
print(f"1. Subnet Network: {net1}")
print(f"2. Subnet Network: {net2}")

first_host = f"{base_address}1"
last_host = f"{base_address}{sub_size - 2}"
print(f"1. Subnet İlk Host: {first_host}")
print(f"1. Subnet Son Host: {last_host}")