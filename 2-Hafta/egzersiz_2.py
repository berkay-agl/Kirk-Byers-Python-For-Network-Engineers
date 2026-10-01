print("*" * 50)

f = open("show_version.txt", mode="r")
data = f.read()
f.close()

print(f"show_version.txt dosyasının ilk satırı: {data.splitlines()[0]}")
print(f"'data' variable'ın data type'ı: {type(data)}")

print("*" * 50)

with open("show_version.txt", mode="r") as f:
    data = f.readlines()
    print(f"show_version.txt dosyasının ilk satırı: {data[0].strip("\n")}")
    print(f"'data' variable'ın data type'ı: {type(data)}")

print("*" * 50)
