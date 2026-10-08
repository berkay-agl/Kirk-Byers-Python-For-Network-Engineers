base_address = "192.168.254."

sub_pre_len = int(input("25 ile 30 arasında bir subnet prefix length giriniz: "))

sub_size = 2 ** (32 - sub_pre_len)
hosts = sub_size - 2
num_subnets = 256 // sub_size

print("\nSubnets:")
print(f" Subnet sayıs: {num_subnets}")

for octet in range(0, 256, sub_size):
    print(f" Subnet numarası: {base_address}{octet}")

print(f"\nHost sayısı: {hosts}")

first_host = f"{base_address}1"
last_host = f"{base_address}{sub_size - 2}"

print(f"İlk subnet'deki ilk host: {first_host}")
print(f"İlk subnet'deki son host: {last_host}")