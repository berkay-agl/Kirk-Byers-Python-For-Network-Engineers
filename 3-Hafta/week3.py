# syntax, indented block
ip_addr = "192.168.1.1"

if "192.168" in ip_addr:
    print("Adres içinde 192.168 geçiyor.")

# if, elif, else
expression = "bir string"
ikinci_expression = "bir string"

if expression:
   print("Merhaba!")
   print("İkinci Merhaba!")
elif ikinci_expression:
   print("Başka yazı...")
   print("Selam!")
else:
   print("else")
   print("Merhaba!")

# operators
ssh_timeout = 10

if ssh_timeout == 5:
   print("SSH timeout süresi: 5 saniye.")
elif ssh_timeout > 15:
   print("SSH timeout süresi 15 saniyeden fazla.")
else:
   print("Bilinmeyen SSH timeout süresi.")

# logical operators
ssh_timeout = 10
host_ulasilabilir = True
ip_addr = "192.168.1.1"

if host_ulasilabilir and ssh_timeout >= 5:
    print("Connection sağlanıyor...")
elif not host_ulasilabilir or ip_addr == "192.168.1.1":
    print("Host çözümlenemedi. Connection sağlanamıyor.")
else:
    print("Bilinmeyen hata!")

print("*" * 20)

# nested
ssh_timeout = 10
host_ulasilabilir = True

if host_ulasilabilir:
   if ssh_timeout is not None:
       print("Connection sağlanıyor...")
else:
   print("ssh_timeout tanımlı değil!")

print("*" * 20)

# idiomatic
ssh_timeout = 10
host_ulasilabilir = True
ip_addr = None

if ssh_timeout is None:
    print("Hata: SSH timeout bulunamadı.")
if host_ulasilabilir is False:
    print("Hata: host ulaşılabilir değil.")
if ip_addr is not None:
    print("IP Address connection: OK")
else:
    print("Sanırım her şey tamam (:")

# truish
ssh_timeout = 0

if not ssh_timeout:
    print("0 -> Truish ama 'not' sayesinde buraya girdik.")

# for loop
ip_list = [
   "192.168.1.1",
   "192.168.1.2",
   "192.168.1.3",
   "192.168.1.4",
]

for ip in ip_list:
   print(ip)

print("*" * 20)

# iterator
for harf in "bir string":
   print(harf)

print("*" * 20)

# flow
for i in range(10):
   print(i)
   if i == 5:
       break

print(f"---> {i}")

print("*" * 20)

for i in range(10):
   if i == 5:
       continue
   print(i)

print(f"---> {i}")

print("*" * 20)

veri_merkezleri = [
    ("sf1", "192.100.10."),
    ("sf2", "192.100.20.")
]

for vm, base_addr in veri_merkezleri:
    for net_addr in range(1, 5):
        print(f"{vm} ---> {base_addr}{net_addr}")

print("*" * 20)

veri_merkezleri = ["sf1", "sf2", "la1", "la2", "dallas"]

for i, vm in enumerate(veri_merkezleri):
    print(f"{i} --> {vm}")

for element in []:
    print("Burası print olacak mı?")

for vm in veri_merkezleri:
    pass

print("*" * 20)

# for-else

for i in range(1, 10):
     print(i)
     if i == 5:
         break
else:
    print("Hiçbir 'break' yaşanmadı.")

print("*" * 20)

for i in range(1, 10):
    print(i)
    if i == 20:
        break
else:
    print("Hiçbir 'break' yaşanmadı.")  # bunu görürüz

print("*" * 20)

# while
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("'break' olmadı ?!")

print("*" * 20)

# oktet_4 yerine test amaçlı 3
base_addr = "192.168"
oktet_3 = 0

while oktet_3 < 3:
   oktet_4 = 2
   while oktet_4 < 3:
       ip_addr = f"{base_addr}.{oktet_3}.{oktet_4}"
       print(f"IP Adresi: {ip_addr}")
       oktet_4 += 1
   oktet_3 += 1

print("*" * 20)

base_addr = "192.168"
oktet_3 = 0

while oktet_3 <= 3:
   for oktet_4 in range(1, 4):
       ip_addr = f"{base_addr}.{oktet_3}.{oktet_4}"
       print(f"IP Adresi: {ip_addr}")
   oktet_3 += 1

print("*" * 20)

# list Comprehensions
my_list = [0, 1, 2, 3, 4]
print(my_list)
print([rakamlar**2 for rakamlar in my_list])

print("*" * 20)

print([rakamlar**2 for rakamlar in my_list])
print([rakamlar**3 for rakamlar in my_list])
print([rakamlar**4 for rakamlar in my_list])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([rakamlar for rakamlar in my_list if rakamlar % 2 == 0])

print([f"192.168.{x}.{y}" for x in range(3) for y in range(3)])

print([f"192.168.{x}.{y}"
       for x in range(3)
       for y in range(3)]
)

print([f"192.168.{x}.{y}" for x in range(10) for y in range(5) if y == 1])

print("*" * 20)

# Generator Expressions
def gen(n):
   i = 0
   while i < n:
       yield i
       i += 1

for val in gen(10):
    print(val)

print("*" * 20)

my_generator = (rakamlar**2 for rakamlar in range(10))
print(type(my_generator))
print(my_generator)

for val in my_generator:
    print(val)

print("*" * 20)

my_generator = (rakamlar ** 2 for rakamlar in range(100_000_000))

base_addr = "192.168"
ip_generator = (f"{base_addr}.{x}.{y}"
                for x in range(10, 15)
                for y in range(5, 10)
)

print(type(ip_generator))

for ip_addr in ip_generator:
    print(ip_addr)
    break

for ip_addr in ip_generator:
    print(ip_addr)
    break

for ip_addr in ip_generator:
    print(ip_addr)
    break

for ip_addr in ip_generator:
    print(ip_addr)
    break

ip_generator = (f"{base_addr}.{x}.{y}"
                for x in range(15, 30)
                for y in range(10, 20)
                if x == y
)

print("*" * 20)

for ip_addr in ip_generator:
    print(ip_addr)
    break

print("*" * 20)

ip_generator = (f"{base_addr}.{x}.{y}" for x in range(10, 20) for y in range(10, 20) if x == y)

for ip_addr in ip_generator:
    print(ip_addr)

print("*" * 20)

 # generator tüketti
for ip_addr in ip_generator:
    print(ip_addr)  # boş
    break


