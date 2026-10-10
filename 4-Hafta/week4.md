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

