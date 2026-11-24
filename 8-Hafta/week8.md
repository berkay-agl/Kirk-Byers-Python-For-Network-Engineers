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
