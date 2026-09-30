import copy

# Numbers - int
my_var = 22 # integer
print(type(my_var))  # Verinin tipini kontrol

# operators
print(10 + 20)
print(30 - 10)
print(5 * 5)
print(4 / 5)

# modulo
my_var = 9
print(my_var % 2)
print(my_var % 3)

# ** üs alma
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)

# Numbers - floats
my_var = 3.5
print(type(my_var))

print(3.5 + 5.5)
print(5 / 2)
print(3.2 * 2.0)

my_var = 4 / 3
print(my_var)

# yuvarlama
print(round(my_var, 1))
print(round(my_var, 2))

# Incrementing | Decrementing: Artırma ve Azaltma
i = 0
i = i + 1
print(i)

i += 1
print(i)
i += 1
print(i)

i -= 1
print(i)
i -= 1
print(i)

# Boolean
my_var = True
print(type(my_var))

my_var2 = False
print(type(my_var2))

# Boolean logical - and her ikisi true
my_var1 = True
my_var2 = True

print(my_var1 and my_var2)

my_var2 = False
print(my_var2 and my_var1)

# Boolean logical - or ikisinden biri true
print(my_var1 or my_var2)

# Boolean logical - not mevcut Boolean değerin tam tersini
print(my_var2)
print(not my_var2)

print(my_var1)
if my_var1:
    print("True olduğu için çalıştı.")

# bir veri tipi için boşluk veya 0 False gerisi True bu -> truish
my_var1 = "bir string"
print(type(my_var1))
print(bool(my_var1))  # True

my_var1 = ""
print(bool(my_var1))  # False

my_var1 = "bir string"

if my_var1:
    print("Yine true.")

my_var1 = 0
print(bool(my_var1))

my_var1 = 10
print(bool(my_var1))

my_var1 = []
print(bool(my_var1))

# NoneType - Boolean context olarak False
my_var1 = None
print(type(my_var1))
print(bool(my_var1))

f = open("show_version.txt")  #  f: file handle
print(f)

f = open("show_version.txt", mode="r")  # Explicit Tanımlama

f = open("show_version.txt")
data = f.read()
f.close()
print(data)

print("-----\n")

f = open("show_version.txt", mode="r")
print(f.readline())  # satırla

print("-----\n")

f = open("show_version.txt")
print(f.readline())
print(f.readline())
f.seek(0)  # başa sarmak için
print(f.readline())

print("-----\n")

# tüm satırları list olarak
f = open("show_version.txt")
data = f.readlines()
print(data)

print("-----\n")

# loop üzerinden
f = open("show_version.txt")
for line in f:
    print(line)

f.close()  # open() ile en önemli kural kapatılması dosyanın

print("-----\n")

f = open("test_file.txt", "w")  # w: write
f.write("Merhaba...\n")
f.write("Merhaba...\n")

# anında diske yazmak için
f.flush()

f = open("test_file.txt", "w")  # w: destructive yani önceki içeriği siliyor
f.write("yeni mesaj\n")
f.close()

# Append için
f = open("test_file.txt", "w")
f.write("Merhaba!\n")
f.flush()
f.close()

f = open("test_file.txt", "a")
f.write("Tekrar merhaba!\n")
f.flush()
f.close()

# Nested blok
if True:
    print("Merhaba")  # 4
    print("Tekrar")
    for x in range(10):
        print(x)  # 8
        print(x)
    print("Başka")
print("Merhaba!")

print("-----\n")

# context manager - with
with open("show_version.txt", mode="r") as f:
    data = f.read()
    print(data)

print("------\n")

# Exception durumunda cleanup
with open("show_version.txt", mode="r") as f:
    ...
    #print(no_var)
    # NameError: name 'no_var' is not defined. Did you mean: 'my_var'?

#print(f.read())
# yukarıda dosyanın kapatıldığını doğrulamak için

my_list = ["berkay", 1, "network", [], None, 1.9]
print(type(my_list))
print(my_list)

print(my_list[0])  # zero-based

my_list[2] = "NetworkRose"
print(my_list)

print(my_list[-1])

my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]
print(my_list)
print(len(my_list))  # items sayısı

print(list(range(10)))  # sayı dizeleri
print(list(range(5, 10)))

# Membership
print("network" in my_list)
print("test123" in my_list)

# duplicate elements: birden fazla item aynı listede olabilir

my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]
print(my_list)
my_list.append("yeni eleman")
print(my_list)

# clear
my_list.clear()
my_list = []

my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]
print(my_list.count("network"))  # belirli eleman sayısı

new_list = my_list.copy()  # shallow copy
print(new_list)

# farklı list object
print(id(my_list))
print(id(new_list))

# concat
print("network" + "rose")
print("network" + " rose")

print(my_list + [10, "string"])

# in-place
my_list.extend(['test', 54])
print(my_list)

my_list.append(["test", 54])  # farka bakılmalı
print(my_list)

val1 = my_list.pop()  # return eder
print(val1)
print(my_list)

val2 = my_list.pop(0)
print(val2)
print(my_list)

my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]
print(my_list[1:3])  # 1: included, 3: excluded
print(my_list[2:4])
print(my_list[:3])
print(my_list[4:])

print(my_list[:])  # shallow copy

print(my_list[4:-1])
print(my_list[4:-2])

# Multidimensional Lists
my_list = [[1, 2, 3], ["a", "b", "c"]]
print(my_list[0])
print(my_list[1])

# Chain Indices
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])

print(my_list[1][0])  # [1]: outermost - [0]: inner
print(my_list[1][1])
print(my_list[1][2])

str_list = my_list[1]
print(str_list)
print(str_list[0])

rtr1_addr = "10.250.1.1"
gw1 = rtr1_addr
print(id(rtr1_addr))
print(id(gw1))
print(rtr1_addr in gw1)

ssh_timeout = 2
print(id(ssh_timeout))

ssh_timeout = 1
print(id(ssh_timeout))  # id farklı name tag yeni object'e

ssh_timeout = 2
print(id(ssh_timeout))  # immutable olduğu

ssh_timeout += 1
print(id(ssh_timeout))  # sayaç ile yine object - name tag aktarım

ssh_timeout = 2
print(id(ssh_timeout))
ssh_timeout = 1
print(id(ssh_timeout))
ssh_timeout = 2
print(id(ssh_timeout))
ssh_timeout += 1
print(id(ssh_timeout))
ssh_timeout -= 1
print(id(ssh_timeout))
ssh_timeout -= 1
print(id(ssh_timeout))

data_centers = ["sf1", "sf2", "la1", "la2", "denver", "dallas"]
print(id(data_centers))
data_centers.append("ny1")
print(id(data_centers))  # mutable

# contiguous block of memory  - pointer
print(data_centers[0])
print(id(data_centers[0]))
print(data_centers[1])
print(id(data_centers[1]))

liste = ["a", "b"]
print(id(liste))
print(id(liste[0]))
print(id(liste[1]))

liste[0] = 1
print(liste)

print(id(liste[0]))
print(id(liste))

print(data_centers)
my_dcs = data_centers
my_dcs.append("london")
print(my_dcs)
print(data_centers)  # asıl data_centers etkilendi

my_dcs = data_centers.copy()  # shallow copy ile yalnızca outermost list
my_dcs.append("london")
print(my_dcs)
print(data_centers)

data_centers = ["sf1", "sf2", "la1", "la2", "dallas"]
dc_list = data_centers.copy()
print(dc_list)
print(data_centers)

data_centers.append("ny1")
dc_list[-1] = "denver"
print(data_centers)
print(dc_list)

print(id(data_centers))
print(id(dc_list))

data_centers = [['365 Main', 'Freemont 1', '1525 Comstock'], ['600 W 7th', '808 North Spring Street']]
print(data_centers[0])

dc_list = data_centers.copy()
print(dc_list[0])

print(dc_list[0] is data_centers[0])  # is - inner listleri True
# nested listelerde shallow copy yanılgısı

data_centers = [['365 Main', 'Freemont 1', '1525 Comstock'], ['600 W 7th', '808 North Spring Street']]
print(data_centers[0])
dc_list = data_centers.copy()
print(dc_list[0])

print(id(data_centers))
print(id(dc_list))
print(id(data_centers[0]))
print(id(dc_list[0]))

dc_list[0].append("200 Paul")
print(dc_list[0])
print(data_centers[0])  # etkilendi

# deep copy: import copy - nested list için inner list dahil
data_centers = [['365 Main', 'Freemont 1', '1525 Comstock'], ['600 W 7th', '808 North Spring Street']]
dc_list = copy.deepcopy(data_centers)
print(id(data_centers))
print(id(dc_list))
print(id(data_centers[0]))
print(id(dc_list[0]))

dc_list[0].append("200 Paul")
print(dc_list)
print(data_centers)

for element in data_centers:
    print(id(element))

for element in dc_list:
    print(id(element))

# Tuples
my_tuple = (1, "merhaba", 10, None, 1.9)
print(type(my_tuple))

print(my_tuple[1])

#my_tuple[1] = "naber"
# TypeError: 'tuple' object does not support item assignment

#my_tuple.append("naber")
# AttributeError: 'tuple' object has no attribute 'append'
