#!/usr/bin/env python

from datetime import datetime

# "my_var" variable, "=" assignment operatörü, alphanumeric ve alt çizgi.
my_var = 10
print(my_var)

# type() -> atanan değerin türünü görmek için kullanılıyor.
print(type(my_var))

my_var1 = "test"
_my_var2 = "test"
my_VAR3 = "test"

print(my_var1)
print(_my_var2)
print(my_VAR3)

# 4my_var = "test"
# Variable sayı ile başlarsa -> SyntaxError: invalid decimal literal

# Convention - snake_case - lowercase - constants
my_ip_addr = "192.168.88.7"
sf_dc_svr9 = "svr9a.lasthop.io"
global_delay_factor = 4
MAX_RETRIES = 3

print(my_ip_addr)
print(sf_dc_svr9)
print(global_delay_factor)
print(MAX_RETRIES)

# geçici / atılabilir variable
_ = "geçerli variable"
print(_)

# Private attribute veya private method convention'ı
_private_var = "variable"
print(_private_var)

# name mangling
__variable = "variable"
print(__variable)

# Dunder methods ya da magic methods
print(__name__)

# print -> stdout
print("Hello World!")

# input -> stdin -> string
my_var = input("Bir IP Adresi gir: ")
print(my_var)

my_var = "string variable"

# Objectlerin metotlarını ve niteliklerini listelemek için
print(dir(my_var))

# Metotların ne işe yaradığını ve nasıl kullanıldığını öğrenmek için
print(help(my_var.strip))

my_var = "bir string"

# Type() ile variable'ın tipini kontrol etme
print(type(my_var))

my_var = 'bir string'  # "" = ''

#my_var3 = "Cannot do this'
# SyntaxError: unterminated string literal (detected at line 67)

m_string = """
bu bir çoklu satır 
 
string yazısı
 
test
 
öylesine cümleler
"""

# string metot -> orijinal string değiştirilmez
my_var = "bir string"
print(my_var)
print(my_var.upper())
print(my_var)

my_var = my_var.upper()
print(my_var)

# split()  string'i parçalar ve bir list döndürür
ip_addr = "172.31.21.15"
print(ip_addr.split("."))  # separator: "."

# aralarına separator ekler ve birleştirir elemanları
oktektler = ["192", "168", "1", "1"]
print(".".join(oktektler))
print("---".join(oktektler))

sentence = "  Bazen satır başında ve sonunda boşluklar olabilir.   \n\n"
print(sentence.strip())  # kenar boşluklarını sil
print(sentence.lstrip())  # soldan
print(sentence.rstrip())  # sağdan

paragraf = """
bu bir
paragraf
bir şeyler yazabilirsin
test
test
test
python
"""

print(paragraf.splitlines())  # satır sonu new line göre

my_var = "  Bir String  "
print(my_var.lower())  # lower karakter
print(my_var.lower().strip())  # boşlukları kesip

print("Bu bir string: %s" % "merhaba")  # %s variable - % eklenecek

my_var = "Merhaba"
print("Bu bir string: %s" % my_var)

print("Bu bir string: %s %s" % (my_var, "merhaba"))  # tuple

print("Bu bir string: {} {}".format(my_var, "merhaba"))  # %s yerine {}

print(f"Bu bir string: {my_var} merhaba")

my_var2 = "merhaba"
print(f"Bu bir string: {my_var} {my_var2}")

ip_addr1 = "192.168.1.1"

print(f"F-string ile IP adresi bulunan bir variable yazdırma: {ip_addr1}")
print(f"F-string ile matematiksel ifadeler yazdırma: {10 + 10}")
print(f"F-string ile variable split edip daha sonra ilk elemanı yazdırma: {ip_addr1.split('.')[0]}")

ip_addr2 = "192.168.1.2"
ip_addr3 = "192.168.1.3"

print(f"{ip_addr1:20}{ip_addr2:20}{ip_addr3:20}")  # : sütun genişlik
print(f"{ip_addr1:>20}{ip_addr2:>20}{ip_addr3:>20}")  # :> sağa
print(f"{ip_addr1:^20}{ip_addr2:^20}{ip_addr3:^20}")  # :^ ortalama

my_var = 1/3
print(my_var)

print(f"my_var değeri: {my_var:.2f}")  # :.2f float format

my_var = "merhaba"
print(f"{my_var = }")  # karşısındaki değer literal string olarak
print(f"Repr -> my_var: {my_var!r}")  # !r - Internal Representatio - Temsil

now = datetime.now()
print(f"Zaman formatı: {now:%B %d, %Y}")

my_dict = {"ip_addr": "192.168.1.1"}
print(f"Değer: {my_dict["ip_addr"]}")
print(f"Değer: {my_dict['ip_addr']}")  # eskiye yönelik bu daha uygun

bir_str = "Bu bir string mesajı"
print("string" in bir_str)  # substring kontrol

win_path = "C:\windows\new_dir\test\python"
print(win_path)

win_path = r"C:\windows\new_dir\test\python"
print(win_path)

sehir = "Sakarya"
plaka = "54"
konum = sehir + ", " + plaka  # string concatenation
print(konum)

data = "birinci satır output \n"
data = data + "ikinci satır output \n"
print(data)

new_data = "birinci satır output \n"
new_data += "ikinci satır output \n"
print(new_data)

print(bir_str)
print(bir_str[0])
print(bir_str[1])

for letter in bir_str:
    print(letter)
