# Lesson 4 Hakkında

## 1. Giriş: Table of Contents

Lesson 4 kapsamında Python'da veri yapıları (Sets, Dictionaries), bunlara ait comprehension yapıları ve exceptions mekanizmaları ele alınmaktadır.

Kirk Byers bu derste sırasıyla aşağıdaki konuları işleyeceğini belirtmektedir:

* **Sets:** Kümeler, temel syntax yapısı, metotlar ve matematiksel küme operasyonları.
* **Set Comprehensions:** Set yapıları için dinamik comprehension syntax'ı.
* **Dictionaries:** Key-value eşleşmesiyle çalışan sözlük veri yapısı ve metotları.
* **Dictionary Comprehensions:** Sözlükler üzerinden dinamik veri türetme mekanizmaları.
* **Exceptions:** Hata türleri ve exception handling mekanizmaları.

> * *sets* → benzersiz elemanlardan oluşan sırasız koleksiyon veri tipi.
> * *set comprehensions* → mevcut veri koleksiyonlarından tek satırda dinamik küme türeten syntax.
> * *dictionaries* → anahtar-değer (key-value) eşleşmesiyle çalışan temel veri yapısı.
> * *dictionary comprehensions* → sözlükleri tek satırda dinamik olarak üreten comprehension yapısı.
> * *exceptions* → kod yürütülürken ortaya çıkan istisnai hata durumları. 

---

## 2. Python Sets

Kirk Byers, günlük iş akışında set'leri tonlarca kullanmadığını; ancak bazı kritik durumlarda hayat kurtardığını ve aksi halde çözülmesi çok zor olacak problemleri oldukça kolaylaştırdığını ifade eder.
Python'da set veri tipi, **benzersiz elemanlardan oluşan sırasız bir koleksiyondur**.

---

### 2.1 Syntax Yapısı ve Unique Elements

Set tanımlanırken süslü parantezler `{}` kullanılır ve elemanlar aralarına virgül konularak listelenir:

```python
In [1]: addresses = {"192.168.100.1", "192.168.100.2", "192.168.100.3"}

In [2]: type(addresses)
Out[2]: set
```

`type()` fonksiyonu çalıştırıldığında değişkenin tipi **`set`** olarak döner.

**Yinelenen Elemanların Otomatik Elenmesi:**

Set yapısının en temel karakteristiği, bünyesindeki her elemanın mutlaka unique yani benzersiz olması zorunluluğudur. 
Bir set tanımlanırken yinelenmiş/tekrarlanmış eleman girilirse Python bu kopyaları otomatik olarak eler:

```python
In [3]: addresses = {"192.168.100.1", "192.168.100.2", "192.168.100.1"}

In [4]: addresses
Out[4]: {'192.168.100.1', '192.168.100.2'}
```

---

### 2.2 İndeksleme Sınırlaması 

Set yapıları tamamen sırasızdır. Listelerde veya string'lerde olduğu gibi belirli bir eleman sırası bulunmadığından, elemanlara indeks numaralarıyla (`addresses[0]`) doğrudan erişilemez.

İndeks erişimi denendiğinde Python bir `TypeError` exception fırlatır:

```python
In [5]: addresses[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 addresses[0]

TypeError: 'set' object is not subscriptable
```

---

### 2.3 Eleman Ekleme: `.add()` ve `.update()`

Bir set'e eleman eklemek için iki yöntem bulunur:

**1) Tek Eleman Ekleme (`.add()`):**

Kümeye tekil bir eleman dahil etmek için `.add()` operasyonu kullanılır:

```python
In [6]: addresses
Out[6]: {'192.168.100.1', '192.168.100.2'}

In [7]: addresses.add("10.1.1.1")

In [8]: addresses
Out[8]: {'10.1.1.1', '192.168.100.1', '192.168.100.2'}
```

**2) Başka Bir Kümeyi Ekleme (`.update()`):**

İki kümeyi birleştirmek veya mevcut set'e birden fazla elemanı tek seferde dahil etmek için `.update()` metodu kullanılır.

> **Setlerin Mutable Yapısı:** Kirk Byers burada önemli bir detaya dikkat çeker: Set'ler **mutable** nesnelerdir. `.update()` metodu yeni bir küme üretip döndürmez; doğrudan mevcut `addresses` değişkeninin içeriğini modifiye eder. Eklenen kümede  yinelenmiş/tekrarlanmış elemanlar varsa bunlar da otomatik olarak teke indirgenir.

```python
In [9]: addresses.update({"10.1.1.1", "10.1.1.2"})

In [10]: addresses
Out[10]: {'10.1.1.1', '10.1.1.2', '192.168.100.1', '192.168.100.2'}
```

---

### 2.4 Eleman Silme: `.remove()` vs `.discard()`

Set içerisinden eleman çıkartırken `.remove()` ve `.discard()` metotları kullanılır. 
Bu iki metot arasındaki kritik fark, silinmek istenen eleman kümede bulunmadığında ortaya çıkar:

**1) `.remove()` Metodu:**

Belirtilen elemanı set içerisinden çıkartır. Ancak çıkartılmak istenen eleman set içerisinde **mevcut değilse** derhal bir `KeyError` exception fırlatır:

```python
In [11]: addresses.remove("10.1.1.1")

In [12]: addresses
Out[12]: {'10.1.1.2', '192.168.100.1', '192.168.100.2'}

In [13]: addresses.remove("10.1.1.1")
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[13], line 1
----> 1 addresses.remove("10.1.1.1")

KeyError: '10.1.1.1'
```

**2) `.discard()` Metodu:**

Belirtilen elemanın kümede olup olmamasını umursamaz. 
Eleman kümede varsa çıkartır; eğer eleman kümede zaten yoksa veya art arda birden fazla kez çağrılırsa **hiçbir exception fırlatmadan** işlemi sessizce tamamlar:

```python
In [14]: addresses.discard("10.1.1.1")

In [15]: addresses.discard("10.1.1.1")
```

---

### 2.5 Set Operations

Python set yapıları matematiksel küme operasyonlarını doğrudan destekler. 
Network senaryolarında farklı lokasyonlardaki (örneğin San Francisco ve Los Angeles) çakışan veya benzersiz IP adreslerini tespit etmek için bu operasyonlar kullanılır.

Aşağıdaki iki referans küme üzerinden operasyonlar incelenmektedir:

```python
In [16]: sf_addresses = {
    ...: "192.168.100.1",
    ...: "192.168.100.2",
    ...: "10.1.1.1",
    ...: "10.1.1.2"}

In [17]: la_addresses = {
    ...: "10.1.1.1",
    ...: "10.220.33.1",
    ...: "10.220.33.2"}

In [18]: sf_addresses
Out[18]: {'10.1.1.1', '10.1.1.2', '192.168.100.1', '192.168.100.2'}

In [19]: la_addresses
Out[19]: {'10.1.1.1', '10.220.33.1', '10.220.33.2'}
```

#### 2.5.1 Birleşim — Union (`|`)

Her iki set'in tüm elemanlarını tek bir kümede birleştirir. Ortak elemanlar otomatik olarak elenir ve her adres sadece bir kez yer alır.

> **Orijinal Kümelerin Korunması:** Kirk Byers bu noktayı özellikle vurgular: `|` union operasyonu orijinal `sf_addresses` ve `la_addresses` kümelerini modifiye etmez. Ortaya çıkan birleşimi saklamak istiyorsak bunu yeni bir değişkene assign etmemiz gerekir.


```python
In [20]: sf_addresses | la_addresses
Out[20]: 
{'10.1.1.1',
 '10.1.1.2',
 '10.220.33.1',
 '10.220.33.2',
 '192.168.100.1',
 '192.168.100.2'}
```

#### 2.5.2 Kesişim — (`&`)

Yalnızca her iki kümede de ortak olarak bulunan elemanları döndürür. 
Network ortamında hem SF hem de LA lokasyonunda bulunan tekrarlamış IP adreslerini bulmak ve çakışmaları çözmek için kullanılır:

```python
In [21]: sf_addresses & la_addresses
Out[21]: {'10.1.1.1'}
```

#### 2.5.3 Simetrik Fark — (`^`)

Kesişim kümesinde yer almayan, yani iki küme arasında çakışmayan tüm benzersiz elemanları bir araya getirir:

```python
In [22]: sf_addresses ^ la_addresses
Out[22]: {'10.1.1.2', '10.220.33.1', '10.220.33.2', '192.168.100.1', '192.168.100.2'}
```

#### 2.5.4 Fark — (`-`)

Bir set'ten diğer set'in elemanlarını çıkartma işlemidir. 
Kirk Byers bu operasyonda **hangi kümenin önce geldiğinin, yani yönün/sıralamanın kritik olduğunu** belirtir:

* **`sf_addresses - la_addresses`:** Her iki kümede ortak olan tüm elemanları `sf_addresses` kümesinden çıkartır; geriye yalnızca San Francisco'ya özgü kalan adresleri döndürür:

```python
In [23]: sf_addresses - la_addresses
Out[23]: {'10.1.1.2', '192.168.100.1', '192.168.100.2'}

```

* **`la_addresses - sf_addresses`:** Sıralama ters çevrildiğinde, ortak elemanlar `la_addresses` kümesinden çıkartılır; geriye yalnızca Los Angeles'a özgü kalan adresler döner:

```python
In [24]: la_addresses - sf_addresses
Out[24]: {'10.220.33.1', '10.220.33.2'}
```

> * *set* → süslü parantezlerle tanımlanan, sırasız ve benzersiz elemanlar barındıran mutable koleksiyon yapısı.
> * *unique elements* → küme içerisindeki her elemanın tekil olması; yinelenmiş değerlerin otomatik olarak elenmesi kuralı.
> * *not subscriptable* → kümenin sırasız olması sebebiyle indeks numarasıyla (`[0]`) doğrudan eleman erişimi yapılamaması durumu.
> * *.add()* → kümeye tek bir yeni eleman ekleyen operasyon.
> * *.update()* → mevcut kümenin içeriğini doğrudan modifiye ederek başka bir kümenin elemanlarını dahil eden metot.
> * *.remove()* → belirtilen elemanı silen; eleman kümede bulunamazsa `KeyError` exception fırlatan metot.
> * *.discard()* → belirtilen elemanı silen; eleman kümede olmasa bile exception üretmeden sessizce çalışan metot.
> * *union (`|`)* → iki kümenin tüm elemanlarını yinelenmişleri eleyerek birleştiren operasyon.
> * *intersection (`&`)* → iki kümenin yalnızca kesişiminde yer alan ortak elemanları döndüren operasyon. 
> * *symmetric difference (`^`)* → kesişim dışındaki ortak olmayan benzersiz elemanları bir araya getiren operasyon.
> * *difference (`-`)* → solundaki kümeden sağındakinin ortak elemanlarını çıkaran ve yönün kritik olduğu fark operasyonu.

---

## 3. Set Comprehensions 

Set comprehensions konusu, list comprehensions yapısına oldukça benzeyen, opsiyonel ve orta seviye bir konudur. 
Bir `for` loop kullanarak dinamik olarak yeni bir set oluşturmanın pratik yoludur.

---

### 3.1 Syntax Yapısı ve Çalışma Mantığı

Set comprehension syntax'ı temel olarak list comprehension ile aynı mantıkta çalışır. Tek fark, dış sınırları belirleyen köşeli parantezler `[]` yerine süslü parantezlerin `{}` kullanılmasıdır:

```python
In [1]: my_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

In [2]: my_set
Out[2]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

In [3]: {rakamlar**2 for rakamlar in my_set}
Out[3]: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

* **Döngü Kısmı:** `{... for rakamlar in my_set}` ifadesi mevcut küme üzerinde gezinir ve her bir değeri `rakamlar` loop variable'ına atar.
* **Expression:** En başta yer alan `rakamlar**2` ifadesi, yeni set'e eklenecek olan yeni elemanları hesaplar (karelerini alır).
* **Yeni Set Üretimi:** Orijinal kümedeki elemanların kareleri alınarak tek satırda yeni bir set dinamik olarak üretilir.

---

### 3.2 Conditional Set Comprehensions

Set comprehension yapısının sonuna bir `if` koşulu eklenebilir. Bu durumda yalnızca koşulu sağlayan (`True` evaluate edilen) elemanlar ifadeye sokulup yeni kümeye dahil edilir:

```python
In [4]: {rakamlar**2 for rakamlar in my_set if rakamlar % 2 == 0}
Out[4]: {0, 4, 16, 36, 64}
```

* For loop ile `my_set` elemanları tek tek taranır.
* `if rakamlar % 2 == 0` kontrolü ile yalnızca çift sayılar filtrelenir; tek sayılar elenir.
* Filtreyi geçen çift sayıların kareleri (`rakamlar**2`) alınarak yeni set'e aktarılır.

---

### 3.3 Multiple Loops

Tıpkı list comprehension'da olduğu gibi, set comprehension içerisinde de birden fazla `for` döngüsü peş peşe tanımlanabilir. 
Soldan sağa doğru okunduğunda ilk döngü dış döngü, sonraki ise iç döngü olarak çalışır:

```python
In [5]: base_addr = "192.168."

In [6]: {f"{base_addr}{x}.{y}" for x in range(1, 10) for y in range(1, 10)}
Out[6]: 
{'192.168.1.1',
 '192.168.1.2',
 '192.168.1.3',
 ...
 '192.168.9.7',
 '192.168.9.8',
 '192.168.9.9'}
```

* İlk döngü olan `for x in range(1, 10)` dış döngüdür.
* `x` değeri her bir adım için sabit tutulurken, içteki `for y in range(1, 10)` döngüsü sırayla tüm `y` değerlerini tüketir.
* İç döngü tamamlandığında `x` değeri artırılır ve süreç yinelenerek dinamik IP adresleri üretilir.

---

### 3.4 Multiple Loops ve Conditional

Birden fazla `for` döngüsü ve bir `if` koşulu aynı set comprehension içerisinde birlikte kullanılabilir. 
Kirk Byers, bu tip karmaşık ifadelerde okunabilirliği artırmak adına kodu alt alta çok satırlı yazmanın çok daha temiz olduğunu belirtir:

```python
In [7]: {f"{base_addr}{x}.{y}"
   ...: for x in range(1, 10)
   ...: for y in range(1, 10)
   ...: if x == y
   ...: }
Out[7]: 
{'192.168.1.1',
 '192.168.2.2',
 '192.168.3.3',
 '192.168.4.4',
 '192.168.5.5',
 '192.168.6.6',
 '192.168.7.7',
 '192.168.8.8',
 '192.168.9.9'}
```

* `for x in range(1, 10)` en dıştaki döngüdür.
* `for y in range(1, 10)` içteki döngüdür.


* Sona eklenen `if x == y` koşulu, yalnızca `x` ve `y` değerlerinin birbirine eşit olduğu durumları filtreler. Yalnızca bu koşulu sağlayan IP adresleri yeni set'in elemanı olarak kaydedilir.

> * *set comprehension* → süslü parantezler `{}` içinde `for` döngüsü kullanarak tek satırda dinamik yeni küme üreten syntax yapısı.
> * *expression* → comprehension'ın en başında yer alan ve yeni set'e eklenecek elemanların değerini belirleyen işlem.
> * *inner loop / topmost loop* → çoklu döngülü comprehension yapılarında sırasıyla iç ve dış döngüleri ifade eden hiyerarşik yapı.
> * *conditional set comprehension* → döngü sonuna `if` ekleyerek yalnızca belirli şartları karşılayan elemanları yeni kümeye dahil etme mekanizması.
> * *readability (multiple lines)* → karmaşık comprehension ifadelerini alt alta satırlara bölerek okunabilirliği artırma yöntemi.

---

## 4. Python Dictionaries 

Kirk Byers, Python'da en çok odaklanılması gereken en temel iki veri yapısının **lists** ve **dictionaries** olduğunu belirtir. 
Dictionaries çok yaygındır ve verilerin saklanıp kullanılmasında çok sayıda farklı bağlamı yönetir.

---

### 4.1 Syntax Yapısı ve Key-Value İlişkisi

Dictionary yapısı **key-value** çiftlerinden oluşan bir koleksiyondur. 
Diğer programlama dillerinde bu yapılar **hashes** veya **hash maps** olarak da adlandırılır.

* **Sıralama:** Python 3.7 sürümünden itibaren dictionary yapıları **sıralı** hale getirilmiştir. Bu sıra, elemanların dictionary içerisine eklenme sırasıdır.
* **Syntax:** Tanımlama süslü parantezler `{}` ile yapılır. Her bir eleman `key: value` biçiminde yazılır ve çiftler birbirinden virgülle ayrılır.
* **Veri Tipleri:** Key'ler neredeyse her zaman string tipindedir. Karşılık gelen value kısmı ise string, integer, list veya başka bir dictionary gibi farklı veri tiplerinde olabilir.

```python
In [1]: my_dict = {
   ...: "rtr1": "10.100.1.1",
   ...: "rtr2": "10.100.2.1",
   ...: "rtr3": "10.100.3.1",
   ...: }

In [2]: my_dict
Out[2]: {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.3.1'}
```

---

### 4.2 Key ile Erişme ve Yeni Value Atama 

Dictionary içerisindeki bir değere erişmek veya değeri güncellemek için köşeli parantez `[]` syntax'ı kullanılır:

**1) Değere Erişme:**

Dictionary adının yanına köşeli parantez içinde ilgili key yazılarak karşılık gelen value elde edilir:

```python
In [3]: my_dict["rtr3"]
Out[3]: '10.100.3.1'
```

**2) Yeni Değer Atama:**

Mevcut bir key'e yeni bir değer atamak için doğrudan key referans alınarak atama yapılır:

```python
In [4]: my_dict["rtr3"] = "10.100.100.1"

In [5]: my_dict
Out[5]: {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}
```

---

### 4.3 Big-O Notasyonu ve Arama Hızı ($O(1)$)

Kirk Byers'ın vurguladığı en kritik noktalardan biri dictionary yapılarının erişim hızıdır.

* Bir dictionary içerisinde 100 bin, 1 milyon veya 10 milyar eleman olsa dahi bir key verildiğinde karşılık gelen value değerinin getirilme süresi veri yapısının büyüklüğüne göre değişmez.
* Bilgisayar biliminde arama süresi **Big-O notation** ile ölçülür.
* Dictionary yapılarında key üzerinden arama hızı **$O(1)$** (constant / fixed time) olarak tanımlanır. Yani veri kümesi ne kadar devasa olursa olsun arama işlemi temelde sabit bir sürede son derece hızlı gerçekleşir. (Bence ekstra olarak O(1), O(N), O(N^2) araştırmak iyi olur.) 

---

### 4.4 Olmayan Bir Key'e Erişme ve KeyError Exception

Dictionary içerisinde tanımlı olmayan bir key köşeli parantez ile çağrıldığında Python bir **`KeyError`** exception fırlatır:

```python
In [6]: my_dict["rtr4"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[6], line 1
----> 1 my_dict["rtr4"]

KeyError: 'rtr4'
```

Programın çökmesine yol açan bu durum, aranan anahtarın sözlükte bulunmadığını belirtir.

---

### 4.5 `.get()` Metodu ile Güvenli Arama

Hata almadan daha kontrollü bir erişim sağlamak için **`.get()`** metodu kullanılır:

* **Varsayılan Davranış (`None` Dönüşü):** Key mevcutsa değerini döndürür; eğer key mevcut değilse hata fırlatmak yerine varsayılan olarak **`None`** döndürür. Program kırılmadan çalışmayı sürdürür.

```python
In [7]: my_dict.get("rtr3")
Out[7]: '10.100.100.1'

In [8]: ret_val = my_dict.get("rtr4")

In [9]: print(ret_val)
None

In [10]: ret_val

In [11]: my_dict
Out[11]: {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}
```

* **Varsayılan Değeri Değiştirme:** `.get()` metoduna ikinci bir argüman verilerek `None` yerine dönmesi istenen varsayılan değer belirlenebilir:


```python
In [12]: my_dict.get("rtr4", "unknown")
Out[12]: 'unknown'

In [13]: my_dict
Out[13]: {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}
```

Aranan `"rtr4"` anahtarı bulunamadığı için metot `"unknown"` değerini teslim eder; ancak dictionary içeriğine herhangi bir ekleme yapmaz.

> * *dictionary* → süslü parantezlerle tanımlanan, key-value çiftlerini saklayan sıralı koleksiyon veri yapısı.
> * *key-value pair* → bir anahtar ve o anahtara atanmış değerden oluşan eşleşme.
> * *insertion order* → elemanların dictionary'ye eklendikleri sırayı koruma özelliği (Python 3.7+).
> * *Big-O / $O(1)$* → dictionary içerisindeki bir key'in veri seti büyüklüğünden bağımsız sabit sürede bulunabilme arama karmaşıklığı.
> * *KeyError* → dictionary içerisinde yer almayan bir key'e köşeli parantezle doğrudan erişilmek istendiğinde üretilen exception.
> * *.get()* → aranan key mevcut değilse exception fırlatmak yerine `None` veya belirlenen varsayılan değeri döndüren güvenli erişim metodu.

---

### 4.6 Looping over Dictionaries

Dictionary üzerinde döngü kurarken ihtiyaç duyulan veriye göre (yalnızca key'ler, yalnızca value'lar veya her ikisi birden) farklı döngü yaklaşımları kullanılır.

---

#### 4.6.1 Doğrudan Döngü ile Key'leri Alma

Bir dictionary üzerinde doğrudan `for` döngüsü kurulduğunda, varsayılan olarak her iterasyonda sıradaki **key** döner:

```python
In [1]: my_dict = {
   ...: "rtr1": "10.100.1.1",
   ...: "rtr2": "10.100.2.1",
   ...: "rtr3": "10.100.100.1",
   ...: }

In [2]: print(my_dict)
{'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}

In [3]: for key in my_dict:
   ...:      print(key)
   ...: 
rtr1
rtr2
rtr3
```

Loop variable (burada `key`) her adımda sıradaki anahtar ismini tutar.

---

#### 4.6.2 `.values()` Metodu ile Value'ları Alma

Yalnızca değerler üzerinde gezinmek istendiğinde **`.values()`** metodu kullanılır.
Döngü adımlarında dictionary'ye eklenme sırasına sadık kalınarak doğrudan value verileri döner:

```python
In [4]: for value in my_dict.values():
   ...:      print(value)
   ...: 
10.100.1.1
10.100.2.1
10.100.100.1
```

---

#### 4.6.3 `.items()` ve Unpacking ile Key ve Value'ları Birlikte Alma

En yaygın kullanım kalıplarından biri, hem key hem de value değerlerine aynı anda erişmektir. Bunun için **`.items()`** metodu kullanılır.

`.items()` metodu döngüye her adımda iki elemanlı bir yapı teslim eder. 
Python'ın otomatik **unpacking** yeteneği sayesinde key birinci değişkene (`key`), value ise ikinci değişkene (`value`) atanır:

```python
In [5]: for key, value in my_dict.items():
   ...:      print(f"Key: {key} Value: {value}")
   ...: 
Key: rtr1 Value: 10.100.1.1
Key: rtr2 Value: 10.100.2.1
Key: rtr3 Value: 10.100.100.1
```

> * *looping over dictionaries* → dictionary üzerinde key, value veya ikisini birlikte işlemek üzere kurulan for loop yapıları.
> * *default loop behavior* → dictionary üzerinde doğrudan dönüldüğünde yalnızca key'lerin gelmesi kuralı. 
> * *.values()* → döngüde yalnızca value elemanlarını sırayla döndüren metot.
> * *.items()* → döngüde key ve value çiftlerini eşzamanlı olarak teslim eden metot.
> * *unpacking (dict items)* → `.items()` çıktısını döngü satırında `for key, value in ...` şeklinde iki ayrı değişkene doğrudan dağıtma mekanizması.

---

### 4.7 Dictionary Methods

Dictionary yapılarında eleman silmek veya iki farklı sözlüğü birleştirmek için çeşitli metotlar ve ifadeler kullanılır.

---

#### 4.7.1 `.pop()` Metodu ile Key Silme

Kirk Byers, bir dictionary içerisinden bir key silmek istediğinde tipik olarak **`.pop()`** metodunu tercih ettiğini belirtir.

`.pop()` metodu, argüman olarak verilen key'i dictionary'den çıkartır ve o key'e ait karşılık gelen **value değerini döndürür**:

```python
In [1]: my_dict = {
   ...: "rtr1": "10.100.1.1",
   ...: "rtr2": "10.100.2.1",
   ...: "rtr3": "10.100.100.1",
   ...: "rtr4": "10.99.1.1",
   ...: }

In [2]: print(my_dict)
{'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1', 'rtr4': '10.99.1.1'}

In [3]: ret_value = my_dict.pop("rtr4")

In [4]: print(ret_value)
10.99.1.1

In [5]: my_dict
Out[5]: {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}
```

* `my_dict.pop("rtr4")` çağrıldığında `"rtr4"` anahtarına ait `'10.99.1.1'` değeri `ret_value` değişkenine atanır.
* İşlem sonrasında `"rtr4"` key-value çifti `my_dict` içerisinden tamamen kaldırılmış olur.

---

#### 4.7.2 `del` İfadesi ile Key Silme

Bir key'i silmenin bir diğer yolu built-in **`del`** ifadesini kullanmaktır.

`del` ifadesi silinen değeri geriye döndürmez; doğrudan belirtilen key-value çiftini sözlükten kaldırır:

```python
In [6]: my_dict = {
   ...: "rtr1": "10.100.1.1",
   ...: "rtr2": "10.100.2.1",
   ...: "rtr3": "10.100.100.1",
   ...: "rtr4": "10.99.1.1",
   ...: }

In [7]: print(my_dict)
{'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1', 'rtr4': '10.99.1.1'}

In [8]: del my_dict["rtr4"]

In [9]: print(my_dict)
{'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'}
```

---

#### 4.7.3 `.update()` Metodu ile Sözlükleri Birleştirme 

İki farklı dictionary'yi birleştirmek için **`.update()`** metodu kullanılır.

Bu işlemde argüman olarak geçilen dictionary'deki tüm key-value çiftleri hedef dictionary'ye eklenir. 
Eğer her iki sözlükte aynı key mevcutsa, sonradan eklenen sözlükteki yeni değer eskisinin üzerine yazılır:

```python
In [10]: ca_routers = {
    ...: "rtr1": "10.100.1.1",
    ...: "rtr2": "10.100.2.1",
    ...: "rtr3": "10.100.100.1",
    ...: }

In [11]: la_routers = {
    ...: "la_rtr1": "10.101.254.1",
    ...: "la_rtr2": "10.101.254.2",
    ...: "rtr3": "192.168.200.1",
    ...: }

In [12]: ca_routers.update(la_routers)

In [13]: print(ca_routers)
{'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '192.168.200.1', 'la_rtr1': '10.101.254.1', 'la_rtr2': '10.101.254.2'}
```

* `la_routers` içindeki `"la_rtr1"` ve `"la_rtr2"` anahtarları doğrudan `ca_routers` sözlüğüne dahil edilir.
* Her iki sözlükte ortak olan `"rtr3"` anahtarının değeri, `la_routers` içerisindeki yeni IP adresi olan `'192.168.200.1'` ile güncellenir (eski `'10.100.100.1'` değeri ezilir).

> * *.pop()* → belirtilen key'i dictionary'den silen ve silinen değeri değişkene döndüren metot.
> * *del* → bir dictionary içerisinden belirtilen key-value çiftini geriye değer döndürmeksizin doğrudan silen ifade.
> * *.update() (dict)* → bir dictionary'ye başka bir dictionary'nin verilerini ekleyen, ortak key varsa yeni değerle güncelleyen metot.

---

