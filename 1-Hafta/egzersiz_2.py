#!/usr/bin/env python

veri_merkezi = input("Bir veri merkezi konumu gir: ")

upper_case = veri_merkezi.upper()

print()
print("Upper case:")
print(upper_case)

print()
print("Strip işlemleri ve repr():")
print("Öncesi: ", repr(veri_merkezi))
# tırnakları, boşlukları vesaire görmek için repr() kirk mailde söylemişti bunu

veri_merkezi = veri_merkezi.strip()
print("Sonrası: ", repr(veri_merkezi))

veri_merkezi = veri_merkezi.strip().upper()

print()
print("Metot zincirleme: ")
print(repr(veri_merkezi))