# Lesson 8 Hakkında

**Lesson 8**'de (Classes and Objects: Part 2), Python'da object-oriented programlama yaparken tekrarlayan **boilerplate** kodları azaltan **Data Classes** yapısı, tüm object'ler tarafından paylaşılan **Class Attributes**, class'lar arası miras alma mekanizması olan **Class Hierarchy and Inheritance** ve object birleştirme mimarisi olan **Composition** konuları ele alınmaktadır.

## 1. Giriş: Table of Contents

Ders kapsamında işlenecek temel başlıklar şunlardır:

1. **Data Classes** (`@dataclass` Decorator ve Kullanım Sınırları)

2. **Class Attributes** (Class Düzeyindeki Ortak Attribute'lar)

3. **Class Hierarchy and Inheritance** (Class Hiyerarşisi ve Kalıtım)

4. **Composition** (Object Birleştirme Mimari Yaklaşımı)

---

## 2. Data Classes (`@dataclass`)

Python'da nispeten basit class'lar oluştururken yazmamız gereken tekrarlı boilerplate kodları azaltmak için **Data Classes** kullanılır. 
Bu özellik Python 3.7 ve sonraki sürümlerde standart olarak yer alır (Python 3.6 için de sonradan geriye dönük uyarlanmıştır ancak güncel Python 3.7+ sürümleri kullanılmalıdır).

```python
from dataclasses import dataclass

@dataclass
class NetDevice:
    device_type: str
    host: str
    username: str
    password: str
```

### 2.1 `@dataclass` Syntax ve Python Type Hints Davranışı

* **Import ve Decorator:** Python'ın built-in `dataclasses` modülünden `dataclass` decorator'ı içeri aktarılır (`from dataclasses import dataclass`) ve class tanımının hemen üstüne `@dataclass` eklenir.

* **Attribute Tanımlama ve Otomatik Bağlama:** Klasik `__init__` method'u yazıp tek tek `self.host = host` atamaları yapmak yerine, doğrudan class bloğu altında attribute isimleri yazılır. `@dataclass` decorator'ı bu alanları `__init__` parametrelerine dönüştürür ve object oluşturulurken gönderilen argümanları aynı isimle doğrudan object'e bağlar.

* **Type Hints Kullanımı:** Data class yazımında her attribute'ün yanına iki nokta üst üste (`:`) konularak Python **type hints** syntax'ı ile veri tipi belirtilir (`device_type: str`, `int`, `float`, `bool`, `dict`, `list` vb.).

* **Runtime'da Zorlayıcı Değildir:** Python dinamik tipli bir dil olmaya devam eder. Type hint olarak `str` belirtilmiş bir alana çalışma zamanında bir `int` değeri gönderilse bile Python hata fırlatmaz ve kodu çalıştırır. Bu type hint'ler yalnızca harici statik analiz / type-checking araçlarının tutarlılık denetimi yapabilmesi içindir.

### 2.2 Standart `__init__` ile Birebir Eşdeğerlik ve Object Kullanımı

Argüman geçirme ve object'e bağlama açısından yukarıdaki `@dataclass` tanımı, aşağıdaki standart class tanımıyla birebir aynı işi yapar:

```python
class NetDevice:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
```

Oluşturulan data class'tan object türetme ve attribute'lere erişme süreci, standart class'larla tamamen aynıdır:

```python
rtr1 = NetDevice(
    device_type="juniper_junos",
    host="rtr1.domain.com",
    username="admin",
    password="jnpr123",
)
```

`pdbr` debugger üzerinde otomatik bağlanan attribute'lerin kontrolü:

```text
(Pdbr) rtr1.device_type
'juniper_junos'
(Pdbr) rtr1.host
'rtr1.domain.com'
```

### 2.3 Varsayılan Değerler Kuralı

Data class içerisindeki attribute'lere varsayılan değerler atanabilir. 
Ancak tıpkı fonksiyon parametrelerinde olduğu gibi, **varsayılan değere sahip olan attribute'lerin mutlaka varsayılan değeri olmayan zorunlu attribute'lerden sonra (en sonda) tanımlanması gerekir**:

```python
@dataclass
class NetDevice:
    host: str
    username: str
    password: str
    device_type: str = "cisco_ios"
```

### 2.4 Otomatik Üretilen Ek Boilerplate Method'lar (`__repr__` ve `__eq__`)

`@dataclass` decorator'ı yalnızca `__init__` method'unu üretmekle kalmaz; standart class'larda manuel olarak yazmamız gereken başka magic method'ları da arka planda otomatik oluşturur:

* **`__repr__` (Object Temsili):** Standart bir class'ta object'i debugger'da incelediğimizde veya `print()` ile yazdırdığımızda `<__main__.NetDevice object at 0x7fab2db418d0>` şeklinde okunması zor bir bellek adresi çıktısı alırız. Data class'larda ise `__repr__` otomatik oluşturulduğu için (ve `__str__` tanımlı değilse Python otomatik olarak `__repr__` çıktısına düştüğü için) object'in tüm attribute'lerini okunaklı bir formatta görürüz.

* **`__eq__` (Eşitlik Karşılaştırması):** İki farklı object'in sahip olduğu verilerin birbirine eşit olup olmadığını (`==` operatörü ile) karşılaştırabilmemizi sağlayan `__eq__` method'u da otomatik olarak oluşturulur.

`pdbr` debugger üzerinde **Data Class** ve **Standard Class** çıktı farkı:

```text
# Data Class çıktısı:
(Pdbr) print(rtr2)
NetDevice(
    device_type='cisco_ios',
    host='rtr2.domain.com',
    username='admin',
    password='csco123',
    interface_ips=[]
)

# Standard Class with __init__ çıktısı:
(Pdbr) rtr1
<__main__.NetDevice object at 0x7fab2db418d0>
(Pdbr) print(rtr1)
<__main__.NetDevice object at 0x7fab2db418d0>
```

### 2.5 Karmaşık Yapılar ve Data Class Kullanım Sınırları

Data class'lar içerisinde standart method'lar (`def some_method(self, ...):`) tanımlanabilir, karmaşık initialization pattern'ları kurulabilir veya liste/dictionary gibi mutable varsayılan değerler için `field(default_factory=...)` yapısı kullanılabilir:

```python
from dataclasses import dataclass, field
from typing import List

def default_list():
    return []

@dataclass
class NetDevice:
    device_type: str
    host: str
    username: str
    password: str
    interface_ips: List[str] = field(default_factory=default_list)
```

> **Mimari Tavsiye (Ne Zaman Kullanmalı, Ne Zaman Bırakmalı?):** Data class'ların temel varlık amacı karmaşıklığı ve boilerplate kodu azaltmaktır. Eğer yalnızca veri taşıyan basit veri konteynerleri (dictionary alternatifi olup yanında birkaç basit method barındıran yapılar) oluşturuyorsak `@dataclass` harika bir çözümdür. Ancak karmaşık varsayılan değerler, `default_factory` veya özel initialization kuralları gibi gelişmiş senaryolara girildikçe ezberlenmesi ve okunması zor özel syntax'lar ortaya çıkar; bu noktada `@dataclass` kullanmayı bırakıp standart `class` ve `__init__` kalıplarına geri dönmek çok daha temiz ve anlaşılır bir yaklaşımdır.

> * **`@dataclass`** → Class içerisindeki `__init__`, `__repr__` ve `__eq__` gibi tekrarlı boilerplate method'ları otomatik olarak oluşturan built-in decorator.
> * **type hints** → Değişken ve attribute'lerin beklenen veri tiplerini (`str`, `int`, `List[str]` vb.) belirten ancak Python tarafından çalışma zamanında zorunlu tutulmayan tip açıklamaları.
> * **`default_factory`** → Data class içerisinde liste veya dictionary gibi mutable varsayılan değerlerin her yeni object için bağımsız olarak üretilmesini sağlayan `field()` parametresi.

---

## 3. Class Attributes

Şimdiye kadar ele aldığımız attribute'lerin tamamı `__init__` içerisinde `self` referansıyla belirli bir object'e bağlanan **instance attributes** idi. 
Python'da bunun yanında, belirli bir class'tan türetilen **tüm instance'lar (object'ler) tarafından ortaklaşa paylaşılan** **Class Attributes** yapısı bulunur.

```python
class TelnetConn:
    # Class attribute to track all of the Telnet connections
    conns = 0

    def __init__(self, host, username, password):
        self._host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.open()

    def open(self):
        """Create telnet connection."""
        self.telnet_conn = Telnet(self._host)
        self.login()
        TelnetConn.conns += 1
        print(f"Number of telnet connections: {self.conns}")
```

### 3.1 Class Attribute Tanımlama, Okuma ve Güncelleme Kuralları

* **Tanımlama Yeri:** Class attribute'leri `__init__` method'unun içinde veya `self` referansıyla değil, doğrudan `class` bloğunun hemen altında tanımlanır (`conns = 0`).

* **Okuma Sırasında Arama Hiyerarşisi (`self.conns`):** Bir class attribute'ünü yalnızca okumak (`print(f"... {self.conns}")`) için `self` üzerinden erişim yapılabilir. Python bu durumda:

1. Önce **instance seviyesinde** (`self` üzerinde) `conns` adında bir attribute olup olmadığına bakar.
2. Instance seviyesinde bulamazsa bir üst katmana çıkarak **class seviyesinde** (`TelnetConn` üzerinde) `conns` attribute'ünü arar ve değeri oradan getirir.

* **Atama ve Güncelleme Tuzağı (`TelnetConn.conns += 1` vs `self.conns += 1`):** Class attribute'ünü değiştirirken veya artırırken kesinlikle `self.conns += 1` kullanılmamalıdır. Çünkü `self.conns += 1` ifadesi arka planda `self.conns = self.conns + 1` şeklinde bir **assignment** işlemi yapar ve class attribute'ünü güncellemek yerine o instance üzerinde `conns` adında yepyeni ve bağımsız bir instance attribute yaratır. Bu nedenle class attribute'ünü güncellemek için doğrudan class adı üzerinden `TelnetConn.conns += 1` yazılır.

### 3.2 Eşzamanlı Bağlantı Takibi Örneği (`attribs1.py`)

Aşağıdaki döngüde iki farklı router'a ikişer adet olmak üzere toplam 4 eşzamanlı `TelnetConn` object'i oluşturulmakta ve tüm object'lerin ortak `TelnetConn.conns` sayacını paylaştığı görülmektedir:

```python
# Two connections to each
for host in (
    "rtr1.lasthop.io",
    "rtr1.lasthop.io",
    "rtr2.lasthop.io",
    "rtr2.lasthop.io",
):
    tc = TelnetConn(
        host=host,
        username=username,
        password=password
    )
    tc.write("\n")
    data = tc.read()
    print(data)
```

Terminal çıktısı (`$ python attribs1.py`):

```text
$ python attribs1.py
Enter router password:
Number of telnet connections: 1

cisco1#
Number of telnet connections: 2

cisco1#
Number of telnet connections: 3

cisco2#
Number of telnet connections: 4

cisco2#
```

### 3.3 Instance Attribute ve Class Attribute Çakışma Kuralları

Aynı isimde hem bir **class attribute** hem de bir **instance attribute** tanımlandığında, Python'ın attribute çözümleme sırası nedeniyle **instance attribute her zaman kazanır**.

#### Senaryo 1: Hem Class hem Instance Attribute Mevcutsa (Instance Attribute Kazanır)

```python
class A:
    my_attr = 100

    def __init__(self):
        self.my_attr = 10

obj = A()
print(obj.my_attr)
```

`pdbr` debugger çıktısı:

```text
(Pdbr) obj.my_attr
10
```

#### Senaryo 2: Instance Attribute Yoksa (Python Class Attribute'e Bakar)

Instance seviyesinde `my_attr` tanımlanmadığında Python önce instance'a bakar, bulamayınca class seviyesine çıkar ve `100` değerini döndürür:

```python
class A:
    my_attr = 100

    def __init__(self):
        pass

obj = A()
print(obj.my_attr)
```

`pdbr` debugger çıktısı:

```text
(Pdbr) obj.my_attr
100
```

#### Senaryo 3: Doğrudan Class Adı Üzerinden Erişim (`A.my_attr`)

Hiçbir instance oluşturmadan doğrudan class adı üzerinden (`A.my_attr`) erişim yapıldığında Python doğrudan class attribute'ünü getirir:

```python
class A:
    my_attr = 100

    def __init__(self):
        my_attr = 10

print(A.my_attr)
```

`pdbr` debugger çıktısı:

```text
(Pdbr) print(A.my_attr)
100
```

### 3.4 Gerçek Dünya Örneği: Veri Merkezi Adres Tablosu (`attribs6.py`)

Class attribute'ler, bir class'a ait tüm instance'ların ortak kullanacağı sabit arama tablolarını class yapısı içinde düzenli tutmak için de kullanılır. Böylece hem class içinden hem de class dışından (`NetDevice.addresses`) bu verilere erişilebilir.

```python
class NetDevice:
    addresses = {
        "sf1": "365 Main Street, San Francisco, CA 94105",
        "sf2": "200 Paul Avenue, San Francisco, CA 94124",
        "la1": "600 West 7th Street, Los Angeles, CA 90017",
    }

    def __init__(
        self,
        device_type,
        host,
        username,
        password,
        data_center,
    ):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

        self.data_center = data_center
        self.address = NetDevice.addresses[data_center]
```

Class'ın kullanımı ve terminal çıktısı (`$ python attribs6.py`):

```python
rtr1 = NetDevice(
    device_type="juniper_junos",
    host="rtr1.domain.com",
    username="admin",
    password="jnpr123",
    data_center="la1",
)

print()
print(f"RTR1 DC: {rtr1.data_center}")
print(f"RTR1 Address: {rtr1.address}")
print()
```

```text
$ python attribs6.py

RTR1 DC: la1
RTR1 Address: 600 West 7th Street, Los Angeles, CA 90017
```

> * **instance attribute** → `__init__` veya method'lar içinde `self.attr` şeklinde tanımlanan ve yalnızca o tekil object'e ait olan değişken.
> * **class attribute** → Doğrudan `class` bloğu altında tanımlanan ve o class'tan üretilen tüm object'ler tarafından ortaklaşa paylaşılan değişken.
> * **attribute lookup precedence** → `obj.attr` okunurken Python'ın önce instance seviyesine bakması, bulamazsa class seviyesine çıkması; aynı isimde ikisi de varsa instance attribute'ün kazanması kuralı. 

---

## 4. Class Hierarchy ve Inheritance

Python'da class'lar arasında hiyerarşik bir yapı kurarak birbirinden özellik ve davranış miras alan parent/child class ilişkileri oluşturabiliriz. 
Python'daki tüm class hiyerarşisinin en tepesinde built-in base class olan **`object`** yer alır.

### 4.1 Base Class `object` ve Inheritance Syntax'ı

Bir class tanımlarken parantez içinde hangi parent class'tan inheritance yani inheritance alacağını belirtiriz. 
Eğer parantez içinde hiçbir şey belirtmezsek, Python o class'ı varsayılan olarak otomatik şekilde **`object`** base class'ından türetir. 
Dolayısıyla aşağıdaki iki tanım birbiriyle tamamen aynıdır:

```python
class ConnectionClass:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

# Yukarıdaki tanım ile birebir eşdeğerdir:
class ConnectionClass(object):
    pass
```

Python'daki en temel base class olan `object` class'ının dahili olarak (CPython için muhtemelen C dilinde implemente edilmiş olsa da) Python karşılığı olarak nasıl davrandığını gösteren kaba örnek yapı şudur:

```python
class object:
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{self.__class__} object at {hex(id(self))}>"
```

* **CPython ve Built-in Method'lar:** `object` class'ı yukarıdaki `__init__` ve `__repr__` dışında başka built-in method'lar da barındırır.

Kendi class'ımızı tanımladığımızda ve içine kendi `__init__` method'umuzu yazdığımızda, otomatik olarak miras alınan `object` class'ının varsayılan `__init__` method'unu **override** yani ezmiş oluruz:

```python
class object:
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{self.__class__} object at {hex(id(self))}>"

class ConnectionClass:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
```

* **Override Davranışı:** `ConnectionClass` içerisinde kendi `__init__()` method'umuzu tanımladığımız anda, base class (`object`) içindeki varsayılan boş `__init__()` devre dışı kalır ve bizim yazdığımız `__init__()` çalışır. Ancak `__repr__()` method'unu kendi class'ımızda yeniden yazmadığımız için `object` class'ındaki varsayılan `__repr__()` kullanılmaya devam eder.

### 4.2 Parent / Child Class Hiyerarşisi Oluşturma

Varsayılan `object` hiyerarşisini kendi parent ve child class'larımızı ekleyerek genişletebiliriz. 
Aşağıdaki yapıda `TelnetConnection` ve `SSHConnection` birer child class olarak `ConnectionClass` parent class'ından inheritance almakta, `ConnectionClass` ise `object` base class'ından inheritance almaktadır:

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    pass
```

* **Ortak `__init__` Mirası:** Bu yapıda ne `TelnetConnection` ne de `SSHConnection` kendi içinde bir `__init__` tanımlamadığı için, her ikisi de `ConnectionClass` içerisinde tanımlı olan ortak `__init__` method'unu miras alır ve kullanır.

### 4.3 Method Resolution Order (MRO) - Single Inheritance

**Method Resolution Order (MRO)**, bir object üzerinde belirli bir method veya attribute çağrıldığında Python'ın class hiyerarşisi içerisinde bu method'u hangi sırayla arayacağını belirleyen mekanizmadır. Python'da multiple inheritance mümkün olsa da bu Kirk Byers karmaşıklığı önlemek adına yalnızca her class'ın tek bir parent class'a sahip olduğu **Single Inheritance** ele alınmaktadır.

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    pass
```

Single inheritance yapısında MRO arama sırası aşağıdan yukarıya doğrudur:

1. Python önce çağrının yapıldığı **mevcut class'ın kendisine** bakar (`SSHConnection`).
2. Orada bulamazsa bir üstteki **parent class'a** bakar (`ConnectionClass`).
3. Orada da bulamazsa hiyerarşinin en tepesindeki **`object`** base class'ına kadar çıkar.

#### Senaryo 1: `__init__` Araması (Parent Class'ta Bulunma)

`ssh_conn = SSHConnection(...)` çalıştırıldığında Python önce `SSHConnection` içinde `__init__` arar; bulamayınca parent class olan `ConnectionClass` içine bakar ve oradaki `__init__` method'unu çalıştırır:

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    pass

ssh_conn = SSHConnection(
    device_type="cisco_ios",
    host="rtr1.domain.com",
    username="admin",
    password="cisco123"
)
```

* **`__repr__` Araması:** Benzer şekilde `ssh_conn` object'i doğrudan incelendiğinde veya yazdırıldığında Python önce `SSHConnection`'a, sonra `ConnectionClass`'a bakar; ikisinde de `__repr__` bulamayınca en üstteki `object` class'ının `__repr__` method'unu kullanır.

#### Senaryo 2: `print_host()` Araması (Child Class'ın Kendisinde Bulunma)

Her iki child class kendi özel `print_host()` method'unu tanımladığında, `ssh_conn.print_host()` çağrısı yapıldığında Python daha ilk adımda `SSHConnection` içinde bu method'u bulur ve doğrudan kendi method'unu çalıştırır:

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    def print_host(self):
        print(f"Telnet Connection to: {self.host}")

class SSHConnection(ConnectionClass):
    def print_host(self):
        print(f"SSH Connection to: {self.host}")

ssh_conn = SSHConnection(
    device_type="cisco_ios",
    host="rtr1.domain.com",
    username="admin",
    password="cisco123"
)
ssh_conn.print_host()
```

### 4.4 Inheritance Kullanma Amacı: DRY Prensibi ve Code Drift Önleme

Class hiyerarşisi ve inheritance kullanmamızın temel nedeni yazılım mühendisliğindeki **DRY (Don't Repeat Yourself)** prensibini uygulamaktır.

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    def print_host(self):
        print(f"Telnet Connection to: {self.host}")

class SSHConnection(ConnectionClass):
    def print_host(self):
        print(f"SSH Connection to: {self.host}")
```

* **Code Duplication ve Code Drift:** Hem `TelnetConnection` hem de `SSHConnection` için tamamen aynı olan `__init__` kodunu iki ayrı class'ta tekrar tekrar kopyalamak (**code duplication**), ileride bir değişiklik gerektiğinde tüm kopyaların eşzamanlı güncellenmesini zorlaştırır ve kopyalar arasında uyumsuzluk oluşmasına (**code drift**) yol açar. Ortak kodları parent class (`ConnectionClass`) altında tek bir merkezde toplayarak kod tekrarını ortadan kaldırırız.

> * **`object`** → Python'daki tüm class'ların varsayılan olarak en tepede inheritance aldığı built-in base class.
> * **method overriding** → Child class içerisinde, parent class'ta zaten var olan bir method ile aynı isimde yeni bir method tanımlayarak parent'taki davranışın yerine kendi davranışımızı koymak.
> * **Method Resolution Order (MRO)** → Bir method veya attribute çağrıldığında Python'ın önce mevcut class'a, ardından sırayla parent class'lara ve en son `object` class'ına bakarak arama yapma sırası.
> * **DRY (Don't Repeat Yourself)** → Aynı veya benzer kod bloklarını farklı yerlerde kopyalamaktan kaçınarak kod kaymasını (**code drift**) önlemeyi amaçlayan temel programlama prensibi.

---

### 4.5 Mevcut Bir Method'u Genişletme (`super()`)

Parent class'ta tanımlı olan bir method'u (`__init__` gibi) tamamen silip sıfırdan yazmak yani **override** etmek yerine, mevcut davranışını koruyup üzerine yeni özellikler eklemek istediğimizde Python'ın built-in **`super()`** yapısını kullanırız. `super()` (parantezlerle çağrılır), parent class'taki method'u MRO sırasına göre bulup doğrudan çalıştırmamızı sağlar.

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)
```

Object oluşturulurken `key_file` argümanının gönderilmesi:

```python
ssh_conn = SSHConnection(
    device_type="cisco_ios",
    host="rtr1.domain.com",
    username="admin",
    password="cisco123",
    key_file="~/.ssh/my_ssh_key"
)
```

* **Neden `ConnectionClass` Değiştirilmedi?** Base class olan `ConnectionClass` hem `TelnetConnection` hem de `SSHConnection` class'larına hizmet verir; Telnet bağlantılarında SSH key dosyası kullanılmadığı için `key_file` parametresi yalnızca `SSHConnection` içerisine eklenmiştir.

* **`super().__init__(...)` İşleyişi:** `SSHConnection.__init__()` önce `key_file` değerinin `None` olup olmadığını kontrol eder; eğer gönderilmişse `self.key_file = key_file` olarak object'e bağlar. Ardından `device_type`, `host`, `username` ve `password` atamalarını tekrar yazıp, code duplication yaratmak yerine `super().__init__(device_type, host, username, password)` çağrısıyla parent class'ın `__init__` method'unu çalıştırarak kalan attribute'lerin object'e bağlanmasını sağlar.

### 4.6 Parent Class Değişikliklerine Karşı `*args` ve `**kwargs` Kullanımı

Yukarıdaki açık argüman listesi yaklaşımında, eğer parent class (`ConnectionClass` veya üçüncü parti bir library'den miras alınan bir class) ileride güncellenir ve `__init__` parametrelerine yeni argümanlar eklenirse, child class'taki `__init__` imzasını da sürekli güncellemek zorunda kalırız. Bunu önlemek ve kodu parent class değişikliklerine karşı dayanıklı hale getirmek için `*args` ve `**kwargs` kullanılır:

```python
# Eski (Açık Argümanlı) Yöntem:
class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)

# Yeni (*args ve **kwargs ile Esnek) Yöntem:
class SSHConnection(ConnectionClass):
    def __init__(self, *args, **kwargs):
        if kwargs.get("key_file"):
            self.key_file = kwargs.pop("key_file")
        return super().__init__(*args, **kwargs)
```

* **Tüm Positional ve Keyword Argümanları Kabul Etme:** `*args` herhangi bir sayıda positional argümanı, `**kwargs` ise herhangi bir sayıda keyword argümanı kabul etmemizi sağlar.

* **`kwargs.pop("key_file")` Zorunluluğu:** `kwargs` dictionary'si içinde `"key_file"` key'inin varlığı kontrol edilir; varsa `kwargs.pop("key_file")` ile dictionary'den çıkarılarak `self.key_file` olarak object'e bağlanır. Parent class (`ConnectionClass`) `key_file` argümanını tanımadığı için `super().__init__(*args, **kwargs)` çağrısından önce bu key'in `kwargs` içinden mutlaka çıkarılması gerekir.

* **Tasarım Kısıtı:** Bu yöntem kullanıldığında `key_file` parametresi positional argüman olarak değil, **yalnızca keyword argüman** (`key_file="..."`) olarak gönderilebilir.

### 4.7 İkinci `super()` Örneği: `__repr__` Method'unu Genişletme

`super()` yalnızca state değiştiren (`self` üzerine attribute bağlayan) method'larda değil, bir değer döndüren method'ların çıktısını yakalayıp değiştirmek için de kullanılır.

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)

    def __repr__(self):
        orig = super().__repr__()
        return f"{orig} --> Hello"
```

Direkt `SSHConnection` kodu ve `pdbr` debugger çıktısı:

```python
class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)

    def __repr__(self):
        orig = super().__repr__()
        return f"{orig} --> Hello"
```

```text
(Pdbr) ssh_conn
<__main__.SSHConnection object at 0x7f2734939d10> --> Hello
```

* **MRO Üzerinden `__repr__` Çözümlemesi:** `super().__repr__()` çağrıldığında Python MRO sırasını takip ederek önce `ConnectionClass`'a bakar; orada `__repr__` bulamayınca bir üstteki `object` base class'ına çıkar, varsayılan `__repr__` çıktısını string olarak alır ve `orig` değişkenine kaydeder. Ardından bu string'in sonuna `" --> Hello"` eklenerek yeni string döndürülür.

* **Önce vs Sonra `super()` Çağırma Farkı:**
* `__init__` örneğinde **önce** object'in state'i değiştirilmiş (`self.key_file = key_file`), **sonra** `super().__init__(...)` çağrılarak kalan attribute'ler bağlanmıştır.

* `__repr__` örneğinde ise **önce** `orig = super().__repr__()` çağrılarak parent'ın döndürdüğü değer yakalanmış, **sonra** bu dönüş değeri değiştirilerek `return` edilmiştir.

> * **`super()`** → Child class içerisinden MRO sırasını kullanarak parent class'taki method'ları doğrudan çağırmamızı ve mevcut davranışı genişletmemizi sağlayan built-in fonksiyon.
> * **`*args` ve `**kwargs` ile `super()**` → Child class'ın sabit argüman listesine bağımlı kalmadan tüm positional ve keyword argümanları yakalayıp kendi özel argümanını `kwargs.pop()` ile ayıkladıktan sonra kalanları parent class'a iletmesi.

---

### 4.8 Inheritance Özeti ve Mimari Değerlendirme 

Class hierarchy ve inheritance mekanizmasının temel işleyişini ve sunduğu avantajlar ile beraberinde getirdiği dezavantajları bir arada değerlendirmek gerekir.

#### Inheritance Temel Özeti

1. **Kod Tekrarını Önleme:** Parent class'larda tanımlanan kodları tekrar yazmadan (**code duplication** yapmadan, **DRY** prensibiyle) child class'larda kullanmamızı sağlayan bir class hiyerarşisi oluşturabiliriz.

2. **`super()` ile Davranış Genişletme:** Child class içerisinde kendi özel işlemlerimizi yapıp ardından parent class'taki method'u çalıştırmak (davranışı genişletmek) için `super()` kullanabiliriz.

3. **Single Inheritance ve MRO:** Single inheritance yapısında Python, çağrılan bir method'u bulmak için önce mevcut class'a, ardından sırayla parent class'lara bakarak **Method Resolution Order (MRO)** kuralını uygular.

4. **Multiple Inheritance:** Python'da birden fazla parent class'tan inheritance alma (**multiple inheritance**) da mümkündür; ancak multiple inheritance durumunda MRO kuralları oldukça karmaşık hale gelir.

#### Inheritance — Avantajlar

* **Code Duplication:** Inheritance kullanmanın en büyük artısı, ortak kodları parent class altında toplayarak gereksiz kod tekrarını ortadan kaldırmasıdır.

#### Inheritance — Dezavantajlar ve Zorluklar 

* **Örtülü Kod Akışı:** MRO mekanizması parent class'lar üzerinden otomatik arama yaptığı için kodun gerçekte nereden çalıştığını anlamak her zaman açık ve net değildir. Örneğin `SSHConnection` object'i üzerinde `str()` (`__str__`) gibi bir method çağrıldığında, bu method'un hangi parent class içerisinde tanımlı olduğunu bulmak için hiyerarşiyi geriye doğru tek tek taramak gerekebilir; `super()` çağrıları eklendiğinde bu takip daha da karmaşıklaşır.

* **Parent Class Değişikliklerinin Child Class'ı Bozması:** Child class doğrudan parent class'taki koda bağımlı olduğu için, parent kodda yapılan kırıcı değişiklikler child class'ı da bozar. Özellikle parent class sizin kontrolünüzde olmayan harici bir library'de yer alıyorsa, davranışı garanti altına almak için library'i belirli bir sürüme sabitlemeniz ve yalnızca test edip kırıcı değişiklikleri düzeltecek vaktiniz olduğunda sürüm güncellemesi yapmanız gerekir.

* **Method Tanımlarında Tutarlılığı Koruma Zorluğu:** Class hiyerarşisi büyüyüp onlarca dosyaya ve yüzlerce dunder / non-dunder method'a yayıldığında, parent ve child class'lardaki method tanımlarının (method'ların kabul ettiği argüman imzalarının) tüm hiyerarşi boyunca tutarlı kalmasını sağlamak zorlaşır.

Method tanımlarındaki tutarlılık varsayımını ve hiyerarşi yapısını gösteren örnek kod:

```python
class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

class TelnetConnection(ConnectionClass):
    pass

class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)

    def __repr__(self):
        orig = super().__repr__()
        return f"{orig} --> Hello"

# Önemli bir not bu mimari için:
# Buradaki varsayım, method tanımlamanın (yani method'ların kabul ettiği argümanların) class hierarchy'nizdeki class'lar arasında genellikle tutarlı olacağıdır.
```

> * **implied code** → MRO ve `super()` mekanizmaları nedeniyle bir method çağrıldığında çalıştırılan kodun mevcut class içinde açıkça görünmeyip parent class hiyerarşisinden örtülü olarak gelmesi durumu.
> * **version pinning** → Kontrolümüz dışındaki harici bir parent class veya library'de yapılacak kırıcı değişikliklerin kodumuzu bozmasını engellemek için "dependencies"ı belirli bir sürüme sabitleme pratiği.
> * **method signature consistency** → Büyük class hiyerarşilerinde parent ve child class'lardaki method'ların kabul ettiği parametre yapılarının birbiriyle uyumlu tutulması gerekliliği.

---
