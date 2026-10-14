# sets
addresses = {"192.168.100.1", "192.168.100.2", "192.168.100.1"}
print(addresses)

#print(addresses[0])
# TypeError: 'set' object is not subscriptable - sırasız

# item ekleme
addresses.add("10.1.1.1")
print(addresses)

# birden fazla item - küme
addresses.update({"10.1.1.1", "10.1.1.2"})
print(addresses)

# silme
addresses.remove("10.1.1.1")
print(addresses)
#addresses.remove("10.1.1.1")
# KeyError: '10.1.1.1' -  mevcut değilse KeyError

# umursama yok
addresses.discard("10.1.1.1")
addresses.discard("10.1.1.1")
print(addresses)

print("*" * 20)

sf_addresses = {
    "192.168.100.1",
    "192.168.100.2",
    "10.1.1.1",
    "10.1.1.2"
}

la_addresses = {
    "10.1.1.1",
    "10.220.33.1",
    "10.220.33.2"
}

print(sf_addresses)
print(la_addresses)

print(sf_addresses | la_addresses)  # | ortak eleme hepsinden bir tane
print(sf_addresses & la_addresses)  # & sadece ortak
print(sf_addresses ^ la_addresses)  # ^ tüm benzersizler
print(sf_addresses - la_addresses)  # - her iki kümede ortak olan tüm elemanları sf_addresses kümesinden çıkartır
print(la_addresses - sf_addresses)  # bu da la_addresses için

print("*" * 20)

# Set Comprehensions
my_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)
print({rakamlar**2 for rakamlar in my_set})
print({rakamlar**2 for rakamlar in my_set if rakamlar % 2 == 0})

base_addr = "192.168."
print({f"{base_addr}{x}.{y}" for x in range(1, 5) for y in range(1, 5)})

set_co = {f"{base_addr}{x}.{y}"
   for x in range(1, 10)
   for y in range(1, 10)
   if x == y
}

print(set_co)

print("*" * 20)

# Dictionaries
my_dict = {
   "rtr1": "10.100.1.1",
   "rtr2": "10.100.2.1",
   "rtr3": "10.100.3.1",
}

print(my_dict)
print(my_dict["rtr3"])

my_dict["rtr3"] = "10.100.100.1"
print(my_dict)

# olmayan key
#my_dict["rtr4"]
# KeyError: 'rtr4'

print(my_dict.get("rtr3"))
ret_val = my_dict.get("rtr4")
print(ret_val)  # None - hatasız
print(my_dict.get("rtr4", "unknown"))

my_dict = {
   "rtr1": "10.100.1.1",
   "rtr2": "10.100.2.1",
   "rtr3": "10.100.100.1",
}

print(my_dict)

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

# python unpacking sayesinde
for key, value in my_dict.items():
    print(key, value)

print("*" * 20)

# Methods
my_dict = {
   "rtr1": "10.100.1.1",
   "rtr2": "10.100.2.1",
   "rtr3": "10.100.100.1",
   "rtr4": "10.99.1.1",
}

print(my_dict)
ret_value = my_dict.pop("rtr4")
print("Silinen: " + ret_value)
print(my_dict)

my_dict = {
   "rtr1": "10.100.1.1",
   "rtr2": "10.100.2.1",
   "rtr3": "10.100.100.1",
   "rtr4": "10.99.1.1",
}

print(my_dict)
del my_dict["rtr4"]
print(my_dict)

ca_routers = {
    "rtr1": "10.100.1.1",
    "rtr2": "10.100.2.1",
    "rtr3": "10.100.100.1",
}

print(ca_routers)

la_routers = {
    "la_rtr1": "10.101.254.1",
    "la_rtr2": "10.101.254.2",
    "rtr3": "192.168.200.1",
}

ca_routers.update(la_routers)  # rtr3 ezildi
print(ca_routers)

# Dictionaries - Mutable
routers = {
   "rtr1": "10.100.1.1",
   "rtr2": "10.100.1.2",
   "rtr3": "10.100.100.1",
}

ca_routers = routers
print(ca_routers is  routers)
print(id(ca_routers))
print(id(routers))

# Nested Dictionaries
my_devices = {
    "rtr1": {
    "host": "device1.domain.com",
    "device_type": "cisco_xe",
    "username": "cisco",
    "password": "cisco123",
    },

    "rtr2": {
    "host": "device2.domain.com",
    "device_type": "juniper_junos",
    "username": "junos",
    "password": "vmx123!",
    }
}

print(my_devices)

for key in my_devices:
    print(key)

print(my_devices["rtr1"])
print(my_devices["rtr1"]["device_type"])
print( my_devices["rtr2"])
print(my_devices["rtr2"]["device_type"])

sf1 = {
    "routers": ["192.168.1.1", "192.168.1.1"],
    "switches": ["192.168.1.20", "192.168.1.21"]
}

print(sf1)

for key in sf1:
    print(key)

list_dict = [
    {
        'host': 'device1.domain.com',
        'device_type': 'cisco_xe',
        'username': 'cisco',
        'password': 'cisco123',
    },
    {
        'host': 'device2.domain.com',
        'device_type': 'juniper_junos',
        'username': 'junos',
        'password': 'vmx123!',
    }
]

print(list_dict)
print(type(list_dict))

print("*" * 20)

# Dictionary Comprehensions
print({f"rtr{x}": f"192.168.1.{x+20}" for x in range(1, 5)})

routers = {
   "rtr1": "192.168.1.1",
   "rtr2": "192.168.1.2",
   "rtr3": "192.168.1.3",
}

ip_addr = {value: key for key, value in routers.items()}  # value: key şeklinde - key: value değil
print(ip_addr)

routers = {
   "rtr1": "192.168.1.1",
   "rtr2": "192.168.1.2",
   "rtr3": "192.168.1.3",
   "dup_rtr": "192.168.1.3",
}

ip_addr = {value: key for key, value in routers.items()}
print(ip_addr)  # rtr3 ezildi en son kim eklendiyse o kazanır
print(routers)