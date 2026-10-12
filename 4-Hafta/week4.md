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

### 4.8 Dictionaries are Mutable

Kirk Byers, daha önce listeler ve mutability konusunda konuşulan tüm temel fikirlerin genel olarak dictionary yapıları için de birebir geçerli olduğunu belirtir. 
Dictionaries **mutable** yani değiştirilebilir veri yapılarıdır.

---

#### 4.8.1 Bellek Referansı ve İsim Ataması

Bir dictionary başka bir değişkene doğrudan eşitlendiğinde (`ca_routers = routers`), bellekte yeni bir dictionary nesnesi türetilmez. 
Yalnızca bellekte var olan aynı dictionary nesnesine işaret eden yeni bir isim atanmış olur.

```python
In [1]: routers = {
   ...: "rtr1": "10.100.1.1",
   ...: "rtr2": "10.100.1.2",
   ...: "rtr3": "10.100.100.1"
   ...: }

In [2]: ca_routers = routers

In [3]: ca_routers is routers
Out[3]: True

In [4]: id(ca_routers)
Out[4]: 139690765953344

In [5]: id(routers)
Out[5]: 139690765953344
```

* `ca_routers = routers` ataması yapıldığında bellekte tek bir dictionary nesnesi bulunur; hem `routers` hem de `ca_routers` değişkenleri bu nesneye işaret eder.
* `ca_routers is routers` ifadesi kimlik denetimi yapar ve her iki değişken de aynı nesneyi gösterdiği için `True` evaluate edilir.
* `id()` fonksiyonu ile kontrol edildiğinde her iki değişkenin bellekteki adres numarasının tamamen aynı olduğu doğrulanır.
* Bu değişkenlerden birinde yapılacak herhangi bir değişiklik, doğrudan diğer değişkenin içeriğine de yansır.

---

#### 4.8.2 Shallow Copy ve Deep Copy Durumu

Listelerdeki kopyalama mekanizmaları dictionary'ler için de geçerlidir:

* Bir dictionary'nin değerleri başka dictionary veya listeler barındırabilir.
* Nested yapılar kopyalanırken shallow copy veya deep copy davranışlarına dikkat edilmelidir.

> * *mutable (dict)* → dictionary yapılarının sonradan doğrudan modifiye edilebilir olması özelliği. 
> * *identifier (id)* → bir nesnenin bellekteki benzersiz kimlik adresi.
> * *is* → iki değişkenin bellekte tamamen aynı nesneye işaret edip etmediğini denetleyen kimlik operatörü.
> * *shallow copy / deep copy* → karmaşık veya iç içe dictionary yapılarında referansların kopyalanma derinliğini belirleyen mekanizma.

---

### 4.9 Nested Dictionaries

Kirk Byers, sözlüklerin değer value alanlarında başka veri yapılarının saklanabildiğini ve bu yapıların iç içe geçebildiğini belirtir. 
Ağ mühendisliğinde cihaz envanterlerini, bağlantı parametrelerini ve konfigürasyon verilerini modellemek için nested veri yapıları yaygın olarak kullanılır.

---

#### 4.9.1 Nested Dictionaries Tanımlama ve Key Zincirleme 

En dıştaki sözlükte yer alan key'lerin karşılığı, kendi içinde key-value çiftleri barındıran başka bir sözlük olabilir.

```python
In [4]: my_devices = {
   ...: "rtr1": {
   ...: "host": "device1.domain.com",
   ...: "device_type": "cisco_xe",
   ...: "username": "cisco",
   ...: "password": "cisco123"
   ...: },
   ...: 
   ...: "rtr2": {
   ...: "host": "device2.domain.com",
   ...: "device_type": "juniper_junos",
   ...: "username": "junos",
   ...: "password": "vmx123!"
   ...: }}

In [5]: print(my_devices)
{'rtr1': {'host': 'device1.domain.com', 'device_type': 'cisco_xe', 'username': 'cisco', 'password': 'cisco123'}, 'rtr2': {'host': 'device2.domain.com', 'device_type': 'juniper_junos', 'username': 'junos', 'password': 'vmx123!'}}
```

* En dıştaki sözlük (`my_devices`) üzerinde döngü kurulduğunda, varsayılan olarak yalnızca en dıştaki key'ler (`"rtr1"`, `"rtr2"`) elde edilir:

```python
In [6]: for key in my_devices:
   ...:      print(key)
   ...: 
rtr1
rtr2
```

* En dıştaki key'lerden birine erişildiğinde, value olarak içteki sözlüğün tamamı döner:


```python
In [7]: print(my_devices["rtr1"])
{'host': 'device1.domain.com', 'device_type': 'cisco_xe', 'username': 'cisco', 'password': 'cisco123'}
```

* İçteki sözlüğün belirli bir alanına ulaşmak için key'ler soldan sağa doğru arka arkaya zincirlenir:

```python
In [8]: my_devices["rtr1"]["device_type"]
Out[8]: 'cisco_xe'

In [9]: my_devices["rtr2"]["device_type"]
Out[9]: 'juniper_junos'

In [10]: my_devices["rtr2"]
Out[10]: 
{'host': 'device2.domain.com',
 'device_type': 'juniper_junos',
 'username': 'junos',
 'password': 'vmx123!'}

In [11]: my_devices["rtr2"]["device_type"]
Out[11]: 'juniper_junos'
```

İlk indeksleme (`["rtr2"]`) içteki sözlüğü getirir; hemen ardından gelen ikinci indeksleme (`["device_type"]`) ise ilgili iç key'in value bilgisini teslim eder.

---

#### 4.9.2 Dictionaries İçinde Liste Saklama 

İçteki veri yapısının mutlaka bir sözlük olması gerekmez; key'lerin karşılığı bir liste de olabilir:

```python
In [12]: sf1 = {
    ...: "routers": ["192.168.1.1", "192.168.1.1"],
    ...: "switches": ["192.168.1.20", "192.168.1.21"]
    ...: }

In [13]: print(sf1)
{'routers': ['192.168.1.1', '192.168.1.1'], 'switches': ['192.168.1.20', '192.168.1.21']}

In [14]: for key in sf1:
    ...:      print(key)
    ...: 
routers
switches
```

Bu yapıda `"routers"` key'i router IP adreslerinden oluşan bir listeyi, `"switches"` key'i ise switch IP adreslerinden oluşan bir listeyi tutar.

---

#### 4.9.3 Liste İçinde Dictionaries Saklama 

Tersine bir hiyerarşi kurularak en dıştaki yapı bir liste haline getirilebilir ve her bir liste elemanı ayrı bir sözlük olarak tanımlanabilir:

```python
[
    {
        'host': 'device1.domain.com',
        'device_type': 'cisco_xe',
        'username': 'cisco',
        'password': 'cisco123'
    },
    {
        'host': 'device2.domain.com',
        'device_type': 'juniper_junos',
        'username': 'junos',
        'password': 'vmx123!'
    }
]

```

* En dıştaki veri yapısı 2 elemanlı bir listedir.
* Listenin birinci elemanı Cisco cihazının sözlüğü, ikinci elemanı ise Juniper cihazının sözlüğüdür.
* Bu iç içe geçme mekanizması, çözülmek istenen problemin gerektirdiği derinlik seviyesine kadar ilerletilebilir.

---

#### 4.9.4 Veri Yapısı Tasarımı ve Modelleme Tercihleri

Kirk Byers, programlama ilerledikçe veriyi yapılandırma tercihlerinin kritik önem kazandığını vurgular:

* Çözülmek istenen probleme ve verinin doğasına göre bir "list of dictionaries" mi yoksa bir "dictionary of dictionaries" mi kurulacağına karar verilmelidir.
* Veriyi doğru modellemek zaman zaman deneme-yanılma ve tecrübe gerektirir.

> * *nested dictionary* → bir sözlüğün value alanında başka bir sözlük barındırmasıyla oluşan hiyerarşik yapı.
> * *chaining keys* → nested sözlüklerde hedef veriye erişmek için `dict[k1][k2]` şeklinde key'lerin ardışık dizilmesi.
> * *list of dictionaries* → elemanları ayrı ayrı sözlüklerden oluşan liste veri modeli.
> * *dictionary of lists* → değerleri listelerden oluşan sözlük veri modeli.
> * *data structuring* → çözülecek probleme uygun olarak liste ve sözlük hiyerarşisinin en doğru biçimde kurgulanması.

---

## 5. Dictionary Comprehensions

Dictionary comprehensions konusu, list comprehensions ve generator expressions yapılarına oldukça benzeyen, opsiyonel ve orta seviye bir konudur. 
Bir `for` loop ve opsiyonel conditional ifadeler kullanarak dinamik olarak yeni bir dictionary oluşturmanın pratik yoludur.

---

### 5.1 Syntax Yapısı ve Dinamik Dictionary Üretimi

Dictionary comprehension syntax'ında en dışta süslü parantezler `{}` kullanılır. 
Set comprehensions'tan farklı olarak, en başta yer alan expression kısmı aralarında iki nokta üst üste bulunan bir `key: value` çiftinden oluşur.

İçerisinde bir `for` loop bulunur; list comprehensions'ta olduğu gibi multiple loops veya döngü sonuna eklenen koşullar kullanılabilir.

```python
In [1]: {f"rtr{x}": f"192.168.1.{x+20}" for x in range(1, 5)}
Out[1]: 
{'rtr1': '192.168.1.21',
 'rtr2': '192.168.1.22',
 'rtr3': '192.168.1.23',
 'rtr4': '192.168.1.24'}
```

* `for x in range(1, 5)` döngüsü ile 1'den 4'e kadar sayılar taranır ve her adımda `x` loop variable'ına atanır.
* Expression kısmındaki `f"rtr{x}"` ifadesi dinamik olarak dictionary key'ini oluşturur.
* İki noktadan sonra gelen `f"192.168.1.{x+20}"` ifadesi ise bu key'e karşılık gelen value değerini üretir.
* Sonuçta 4 adet key-value çiftinden oluşan yeni bir dictionary dinamik olarak oluşturulur.

---

### 5.2 Key ve Value Yer Değiştirme 

Dictionary comprehensions için yaygın bir use case, mevcut bir dictionary içerisindeki key ve value değerlerinin yerini değiştirmektir.
Kirk Byers bu işlemin sağlıklı çalışabilmesi için mevcut value değerlerinin **unique** ve **immutable** olması gerektiğini önceden varsaydığımızı belirtir:

```python
In [2]: routers = {
   ...: "rtr1": "192.168.1.1",
   ...: "rtr2": "192.168.1.2",
   ...: "rtr3": "192.168.1.3"
   ...: }

In [3]: ip_addr = {value: key for key, value in routers.items()}

In [4]: print(ip_addr)
{'192.168.1.1': 'rtr1', '192.168.1.2': 'rtr2', '192.168.1.3': 'rtr3'}
```

* `routers.items()` üzerinden döngü kurulur ve unpacking ile router isimleri `key`, IP adresleri `value` değişkenine alınır.
* Expression bölümünde `{value: key ...}` syntax'ı kullanılarak IP adresi yeni key, router ismi ise yeni value haline getirilip tersine çevrilmiş yeni bir dictionary üretilir.

---

### 5.3 Duplicate Key Durumu 

Sözlüklerde key'lerin benzersiz olması zorunludur. 
Eğer swap işlemi sırasında orijinal dictionary'de tekrarlayan value'lar varsa, yeni dictionary oluşturulurken bunlar duplicate key yani yinelenen bir key haline gelir.

Kirk Byers bu senaryoda "Hangi değer kazanacak?" sorusunun yanıtını net olarak verir: **En son eklenen değer kazanır**; son gelen değer bir öncekini ezer:

```python
In [6]: routers = {
   ...: "rtr1": "192.168.1.1",
   ...: "rtr2": "192.168.1.2",
   ...: "rtr3": "192.168.1.3",
   ...: "dup_rtr": "192.168.1.3"
   ...: }

In [7]: ip_addr = {value: key for key, value in routers.items()}

In [8]: print(ip_addr)
{'192.168.1.1': 'rtr1', '192.168.1.2': 'rtr2', '192.168.1.3': 'dup_rtr'}

In [9]: print(routers)
{'rtr1': '192.168.1.1', 'rtr2': '192.168.1.2', 'rtr3': '192.168.1.3', 'dup_rtr': '192.168.1.3'}
```

* `routers` dictionary'sinde hem `"rtr3"` hem de `"dup_rtr"` aynı IP adresine (`'192.168.1.3'`) sahiptir.
* Swap comprehension çalışırken döngü önce `'192.168.1.3': 'rtr3'` çiftini oluşturur.
* Döngü bir sonraki adımda `"dup_rtr"` anahtarına geldiğinde, aynı IP key'i için bu kez `'dup_rtr'` değeri atanır ve önceki `'rtr3'` değerinin üzerine yazılır.
* Sonuç olarak yeni `ip_addr` dictionary'sinde `'192.168.1.3'` key'inin karşılığı olarak yalnızca son eklenen `'dup_rtr'` kalır.

> * *dictionary comprehension* → süslü parantezler `{}` içinde `key: value` ifadesi ve `for` döngüsü kullanarak dinamik olarak yeni bir sözlük üreten syntax yapısı.
> * *key: value expression* → comprehension başında iki nokta ile ayrılan, yeni dictionary'nin key ve value'sını eşleyen ifade. 
> * *swapping key and value* → `.items()` üzerinden dönerek mevcut sözlüğün key ve value rollerini yer değiştirme işlemi.
> * *duplicate key behavior* → bir sözlük oluşturulurken aynı key tekrar geldiğinde sonuncu değerin geçerli olması kuralı.

---

## 6. Exception Handling Basics

Kirk Byers, programda bir hata meydana geldiğinde Python'ın bir exception ürettiğini ve kodun çalışmayı durdurarak çöktüğünü belirtir. 
Exception handling, belirli bir hatanın oluşabileceğini önceden bildiğimiz durumlarda programın çökmesini engelleyip hatayı zarifçe yönetmek için kullanılır.

Kirk Byers network üzerinden somut bir örnek verir: 100 farklı ağ cihazına SSH bağlantısı yapan bir kod yazıldığında, bazı cihazların çevrimdışı olması, IP'nin geçersiz olması veya yanlış kimlik bilgileri girilmesi nedeniyle bağlantının kopabileceğini biliriz. Kodun ilk başarısız cihazda çökmesi yerine, bir log mesajı basıp hatayı yakalayarak sıradaki cihaza devam etmesini isteriz.

---

### 6.1 Hata Çıktısının Anatomisi 

Program elemanı olmayan boş bir listede var olmayan bir indekse erişmeye çalıştığında Python çöker ve bir hata çıktısı üretir:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-4$ cat error.py 
my_list = []
print("\nVar olmayan bir indekse erişmeye çalışmak\n")

my_list[0]
print("Bu mesaj print edilmeyecek.")

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-4$ python error.py 

Var olmayan bir indekse erişmeye çalışmak

Traceback (most recent call last):
  File "/home/berkay/Desktop/Python-All/Python-For-Network-Engineers/Week-4/error.py", line 4, in <module>
    my_list[0]
    ~~~~~~~^^^
IndexError: list index out of range
```

* İlk print satırı sorunsuz çalışır ve mesajı ekrana basar.
* `my_list[0]` satırına gelindiğinde bir exception oluşur ve hemen ardından gelen `"Bu mesaj print edilmeyecek."` satırı asla çalıştırılamaz.
* Hata çıktısının en alt satırında oluşan exception türü (**`IndexError`**) ve ek detaylar (`list index out of range`) yer alır.
* Çıktı, hatanın hangi dosyada ve hangi satırda meydana geldiğini işaret eder (`line 4`).

* Kirk Byers, hata çıktısını incelerken işaret edilen satırdan başlayıp geriye doğru satırların kontrol edilmesini önerir; çünkü bazen hatayı asıl tetikleyen durum işaret edilen satırın hemen öncesinde yer alabilir.

---

### 6.2 `try` / `except` Temel Yapısı

Hataları kontrollü şekilde ele almak için **`try`** ve **`except`** blokları kullanılır. 
`try:` ifadesinin altına indented olarak çalıştırılmak istenen satırlar yazılır. Bu satırlarda hedeflenen exception türü meydana gelirse kod anında `except` bloğuna atlar:

```python
In [1]: my_list = []

In [2]: try:
   ...:      my_list[0]
   ...: except IndexError:
   ...:      print("Hata yakalandı!")
   ...: 
Hata yakalandı!
```

* `try` bloğundaki `my_list[0]` satırı `IndexError` üretir.
* Python hatayı yakalar ve tanımlanan exception türüyle (`IndexError`) eşleştiği için `except` bloğuna geçer.
* Program çökmeden `print("Hata yakalandı!")` ifadesi ekrana basılır.

---

### 6.3 `try` Bloğunda Satırların Yürütülme Sırası

`try` bloğu birden fazla satır içerebilir. Python satırları yukarıdan aşağıya sırayla yürütür; hatanın oluştuğu anda `try` bloğundaki kalan satırlar atlanır ve doğrudan `except` bloğuna sıçranır:

```python
In [3]: try:
   ...:      print("Önce")
   ...:      my_list[0]
   ...:      print("Sonra")
   ...: except IndexError:
   ...:      print("Hata yakalandı!")
   ...: 
Önce
Hata yakalandı!
```

* `print("Önce")` ifadesi hatadan önce geldiği için normal şekilde çalışır ve ekrana basılır.
* `my_list[0]` satırında hata meydana geldiği anda kod `except IndexError:` bloğuna atlar.
* Hatanın hemen altında yer alan `print("Sonra")` satırı hiçbir zaman yürütülmez.

---

### 6.4 `except` Bloğunda Çoklu Satırlar ve Blok Dışı Akış

Hem `try` hem de `except` bloğu birden fazla satır barındırabilir. `except` bloğundaki işlemler bittiğinde program akışına normal şekilde devam eder ve blokların dışındaki kodları çalıştırır:

```python
In [4]: try:
   ...:      my_list[0]
   ...: except IndexError:
   ...:      print("Hata yakalandı!")
   ...:      print("Başka bir hata yakalama.")
   ...: print("Dışarıda kalan print.")
Hata yakalandı!
Başka bir hata yakalama.
Dışarıda kalan print.
```

* `IndexError` oluştuktan sonra `except` bloğu içerisindeki iki print satırı da sırayla ekrana basılır.
* Hata yönetimi tamamlandığında `try`/`except` kapsamı dışında kalan en alttaki `print("Dışarıda kalan print.")` satırı yürütülür.

---

### 6.5 Hata Oluşmadığında `except` Bloğunun Atlanması

Eğer `try` bloğu içerisindeki kodlar hatasız bir şekilde tamamlanırsa, `except` bloğu tamamen atlanır ve program doğrudan sonraki kodları çalıştırmaya geçer:

```python
In [5]: my_list = ["10.1.1.1"]

In [6]: try:
   ...:      my_list[0]
   ...: except IndexError:
   ...:      print("Hata yakalandı!")
   ...:      print("Başka bir hata yakalama.")
   ...: print("Dışarıda kalan print.")
Dışarıda kalan print.
```

* `my_list` içerisinde eleman bulunduğu için `my_list[0]` erişimi başarıyla gerçekleşir ve hiçbir exception üretilmez.
* Hata oluşmadığı için `except IndexError:` bloğu tamamen yok sayılır ve atlanır.
* Yalnızca `try`/`except` yapısının dışında kalan satır yürütülerek ekrana `"Dışarıda kalan print."` basılır.

> * *exception* → kodun çalışması sırasında meydana gelen ve yönetilmezse programın çökmesine yol açan hata durumu. 
> * *crash* → beklenmeyen bir exception nedeniyle programın yürütmeyi tamamen durdurması.
> * *gracefully handle* → oluşabilecek hataları `try`/`except` ile yakalayarak programın çökmeden işleyişine devam etmesini sağlama yaklaşımı.
> * *traceback* → hatanın meydana geldiği dosya, satır ve çağrı hiyerarşisini gösteren Python hata raporu.
> * *IndexError* → dizilerde veya listelerde var olmayan bir indeks numarasına erişilmeye çalışıldığında üretilen exception türü.
> * *try block* → hata çıkarma ihtimali olan satırların yazıldığı ve Python'ın çalıştırmayı denediği kod bloğu.
> * *except block* → `try` içerisinde beklenen hata gerçekleştiğinde devreye giren ve hatayı yöneten kod bloğu.

---

### 6.6 Handling Multiple Exception Types

Kirk Byers, bir programda birden fazla farklı hata türüyle karşılaşılabileceğini ve bu durumları yönetmek için iki temel yaklaşım bulunduğunu belirtir:

1. **Tek Bir Handler ile Birden Fazla Exception Türünü Yakalama:** Farklı hatalar için aynı kurtarma veya loglama adımı yürütülecekse kullanılır.
2. **Farklı Exception Türleri İçin Ayrı Handler'lar Tanımlama:** Her hata türüne özel farklı bir işlem yürütülecekse tercih edilir.

---

#### 6.6.1 Tek Bir Blokta Çoklu Exception Yakalama 

Farklı hata türlerini tek bir `except` bloğunda toplamak için hata isimleri parantez içinde virgülle ayrılarak bir **tuple** şeklinde yazılır (`except (IndexError, KeyError):`):

```python
In [1]: my_list = []

In [2]: my_dict = {}

In [3]: try:
   ...:      my_list[0]
   ...:      my_dict["olmayan key"]
   ...: except (IndexError, KeyError):
   ...:      print("Hata yakalandı!")
   ...: print("Dışarıda kalan print.")
Hata yakalandı!
Dışarıda kalan print.
```

* `try` bloğu içerisinde `my_list[0]` satırına gelindiğinde bir `IndexError` üretilir.
* Kirk Byers'ın vurguladığı gibi: Karşılaşılan ilk hatada Python derhal `try` bloğundan çıkar ve doğrudan `except` bloğuna atlar.
* Bu nedenle hemen altındaki `my_dict["olmayan key"]` satırına hiçbir zaman geçilmez.
* Hata, tanımlanan tuple içerisindeki türlerden biriyle (`IndexError`) eşleştiği için `except` bloğundaki `print("Hata yakalandı!")` çalıştırılır.
* Blok sonlandığında program normal akışına devam ederek en dıştaki `print("Dışarıda kalan print.")` satırını yürütür.

---

#### 6.6.2 Farklı Exception Türleri İçin Ayrı Handler'lar 

Her hata türü için farklı bir aksiyon almak gerektiğinde ardışık `except` blokları tanımlanır. Python oluşan hatanın türüne uyan ilk `except` bloğuna atlar ve yalnızca o bloğu yürütür:

```python
In [4]: try:
   ...:      my_list[0]
   ...:      my_dict["olmayan key"]
   ...: except IndexError:
   ...:      print("Hata yakalandı: olmayan list elemanı")
   ...: except KeyError:
   ...:      print("Hata yakalandı: olmayan key")
   ...: print("Dışarıda kalan print.")
Hata yakalandı: olmayan list elemanı
Dışarıda kalan print.
```

* `my_list` boş olduğu için ilk satırda `IndexError` oluşur.
* Python doğrudan eşleşen ilk handler olan `except IndexError:` bloğuna sıçrar ve `"Hata yakalandı: olmayan list elemanı"` mesajını basar.
* İkinci handler olan `except KeyError:` bloğu tamamen atlanır.
* Kirk Byers'ın slaytında gösterdiği gibi; eğer liste düzgün tanımlanmış olsaydı liste satırı başarıyla geçilecek, ardından dictionary satırında `KeyError` oluşacak ve bu kez ikinci handler (`except KeyError:`) devreye girecekti.
* Hata yönetimi tamamlandıktan sonra blok dışındaki `print("Dışarıda kalan print.")` satırı her halükarda çalıştırılır.

> * *multiple exception types* → bir programda ortaya çıkabilecek farklı hata türlerinin ayrı ayrı veya birlikte yönetilmesi.
> * *tuple exception syntax* → `except (Err1, Err2):` şeklinde birden fazla hata türünü tek bir handler altında toplama yöntemi.
> * *multiple handlers* → her exception türü için ayrı `except` bloğu kurarak hataya özgü işlem yürütme yapısı.
> * *first error match* → `try` bloğunda ilk hatayla karşılaşıldığı anda sonraki satırların durdurulup eşleşen ilk exception handler'a atlanması kuralı.

---

### 6.7 Capturing ve Reraising Exceptions

Kirk Byers, exception handling sırasında hata nesnesinin bir değişkene kaydedilebileceğini ve gerektiğinde bir exception'ın kasıtlı olarak tekrar fırlatılabileceğini yani **reraise** kavramını belirtir.

---

#### 6.7.1 Exception Nesnesini Değişkene Yakalama (`as e`)

Oluşan hataya dair detayları incelemek veya ekrana yazdırmak için exception nesnesi `as` anahtar kelimesiyle bir değişkene atanabilir (`except IndexError as e:`):

```python
In [1]: my_list = []

In [5]: try:
   ...:    my_list[0]
   ...: except IndexError as e:
   ...:     print(f"Çok kötü bir hata: {str(e)}")
   ...: print("raise yok çalışır...")
Çok kötü bir hata: list index out of range
raise yok çalışır...

In [6]: 
```

* `except IndexError as e:` ifadesi, meydana gelen hata nesnesini `e` isimli değişkene kaydeder.
* `str(e)` fonksiyonu kullanılarak hatanın doğrudan açıklaması (`list index out of range`) elde edilir ve ekrana basılır.
* Hata yönetildiği için program kırılmaz; blok dışındaki print satırı da normal şekilde çalışır.

---

#### 6.7.2 Exception'ı Yeniden Fırlatma (`raise`)

Kirk Byers buradaki temel use case'i şöyle açıklar: Programda bir hata olduğunda ekrana mesaj basmak, log kaydı oluşturmak veya bir bildirim tetiklemek isteyebiliriz; ancak bu işlemlerden sonra programın yine de çökmesini istiyor olabiliriz.

Bu senaryoda, hata yakalandıktan sonra blok içinde tek başına **`raise`** ifadesi kullanılır:

```python
In [3]: try:
   ...:    my_list[0]
   ...: except IndexError as e:
   ...:     print(f"Çok kötü bir hata: {str(e)}")
   ...:     raise
   ...: print("Burası çalışmaz (raise farkı)")
Çok kötü bir hata: list index out of range
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[3], line 2
      1 try:
----> 2    my_list[0]
      3 except IndexError as e:
      4     print(f"Çok kötü bir hata: {str(e)}")

IndexError: list index out of range

In [4]:
```

* `except` bloğu içerisindeki loglama/mesaj satırı (`print(f"Info about exception: {str(e)}")`) çalıştırılır.
* Ardından gelen `raise` ifadesi, arkasında herhangi bir exception türü belirtilmese dahi yakalanan orijinal hatayı (`IndexError`) yeniden fırlatır.
* Program çöker, terminalde `IndexError` traceback çıktısı oluşur ve `try`/`except` dışındaki satıra asla geçilemez.
* Kirk Byers, burada istenirse orijinal hata yerine farklı bir exception türünün de `raise` edilebileceğini ekler.

> * *capturing exception (`as e`)* → oluşan hata nesnesini `as` anahtar kelimesiyle bir değişkene kaydedip hatanın detaylarına erişme yöntemi.
> * *str(e)* → exception nesnesinin hata açıklamasını string olarak döndüren ifade. 
> * *reraise (`raise`)* → hatayı yakalayıp loglama veya bildirim işlemlerini tamamladıktan sonra programın çökmesini sağlamak amacıyla exception'ı tekrar fırlatma mekanizması.

---

### 6.8 Broad Exception Handling

Kirk Byers, exception handling yaparken çok genel yaklaşımların kullanılabileceğini (`except Exception:` veya yalın `except:`); ancak bu durumun **hataları gizleme** riski taşıdığı konusunda çok dikkatli olunması gerektiğini belirtir.

Bir exception handler yazdığımızda örtük olarak *"Burada ne tür hataların çıkabileceğini biliyorum ve bunları nasıl yöneteceğimin farkındayım"* demiş oluruz. 
`try` bloğunda çok sayıda kod satırı olduğunda veya çeşitli fonksiyonlar çağrıldığında, çok geniş kapsamlı bir handler koymak programda en az iki kritik soruna yol açar:

1. **Program Durumunun Bozulması:** Beklemediğimiz bir hata oluştuğunda genel handler bunu sessizce yakalayabilir; ancak bu işlem programı gerçekten düzeltmez. Program yürütülmeye devam eder fakat iç durumu tamamen beklenmeyen bir hale gelir ve ilerleyen aşamalarda asıl bozulma yüzünden çöker.

2. **Bilgi Kaybı ve Debugging Zorluğu:** Hatanın asıl kaynağı `try` bloğunun içinde gizlendiği için, ekranda beliren hata mesajı çok daha sonraki bir adıma ait olur. Geliştirici hatanın nerede başladığını anlamakta zorlanır ve geriye doğru çalışarak kök sebebi bulmak zorunda kalır.

---

#### 6.8.1 Genel Exception Yakalama ve Hata Türünün Belirsizleşmesi

```python
In [1]: my_list = []

In [2]: try:
   ...:      my_list[0]
   ...: except Exception:
   ...:      print("Genel exception yakalama.")
   ...: 
Genel exception yakalama.

In [3]: my_dict = {}

In [4]: try:
   ...:      my_list[0]
   ...:      my_dict["key_123"]
   ...: except Exception:
   ...:      print("Ne tür bir hata oldu?")
Ne tür bir hata oldu?
```

* İlk blokta `my_list[0]` erişimi bir `IndexError` üretir. Ancak yakalayıcı olarak genel `Exception` sınıfı tanımlandığı için hata türü ayırt edilmeksizin yakalanır ve `"Genel exception yakalama."` yazdırılır.

* İkinci blokta `try` altında hem liste hem sözlük erişimi yer alır. `except Exception:` veya yalın `except:` kullanıldığında, hatanın bir `IndexError` mı yoksa `KeyError` mı olduğu anlaşılmaz; hata türüne dair bilgi kaybolur.

---

#### 6.8.2 Kirk Byers'ın Genel Kuralı 

Kirk Byers genel kural olarak şunu önerir:

* Yalnızca **belirli ve somut nedenlerle ortaya çıkacağını bildiğin hataları** (`IndexError`, `KeyError` veya bağlantı hataları gibi) spesifik olarak yakala.

* Tıpkı SSH bağlantı senaryosunda olduğu gibi; sınırları net çizilmiş durumlarda, cihaz çevrimdışı olduğunda log basıp bir sonrakine geçmek doğru bir yöntemdir.

* Programın durumu olması gerektiği gibi değilse, o hatayı gizlemek yerine **programın çökmesine izin vermek çoğu zaman çok daha sağlıklıdır**.

> * *broad / generic exception handling* → `except Exception:` veya doğrudan `except:` yazarak tüm hata türlerini ayrım gözetmeksizin yakalama yaklaşımı.
> * *hiding errors* → beklemediğimiz kritik hataların genel handler tarafından yakalanarak gizlenmesi ve programın bozuk bir durum ile yürütülmeye devam etmesi problemi.
> * *loss of information* → hatanın asıl türünün ve kaynağının gizlenmesi sonucu debugging sürecinin zorlaşması durumu.
> * *specific handling* → yalnızca oluşacağı önceden öngörülen ve nasıl çözüleceği bilinen spesifik hata sınıflarını yakalama kuralı.

---

