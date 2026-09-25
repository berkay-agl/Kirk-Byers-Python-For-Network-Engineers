# Lesson2 Hakkında

## 1. Giriş: Table of Contents

Lesson 2 kapsamında Python'un temel ve gelişmiş **data type** ile veri yapılarına giriş yapıyoruz.

Kirk Byers bu derste sırasıyla aşağıdaki konuları ele alacağını belirtiyor:

* **Numbers:** Sayısal veri tipleri.
   
* **Booleans and None:** Mantıksal doğruluk değerleri (Booleans) ve Python'a özgü özel `None` tipi.

* **Files:** Dosya işlemleri — dosyaları açma (`open`), okuma (`read`), yazma (`write`) ve sonuna veri ekleme (`append`).

* **Lists:** Python'da daha karmaşık veri yapılarına ilk adım olan listeler.

* **Tuples:** Mantık olarak listelere oldukça benzeyen ancak kendine has özellikleri olan demetler.

* **Sets:** Kendine özel pratik kullanım senaryoları barındıran küme yapıları.

> * *data type* → bir verinin bellekte nasıl tutulacağını ve üzerinde hangi işlemlerin yapılabileceğini belirten veri tipi.
> * *boolean* → sadece `True` veya `False` değerlerini alabilen mantıksal veri tipi.
> * *None* → Python'da bir değerin yokluğunu veya tanımsızlığını ifade eden özel veri tipi.
> * *append* → bir dosyanın veya listenin sonuna yeni veri ekleme işlemi.

---

## 2. Numbers

Python'da en temel veri tiplerinden biri sayılardır. Sayısal yapılarla çalışırken karşımıza iki temel tip çıkar: **integers** ve **floats**.

Python günümüzde data science ve mühendislik alanlarında en baskın dillerden biri haline gelmiştir. 
Bu sebeple dilin ekosisteminde ihtiyaç duyabileceğinizden çok daha fazla matematik kütüphanesi yer alır. 
Ancak temel aritmetik işlemler için harici bir araca gerek kalmadan Python'un kendi operatörleri doğrudan kullanılır.

---

### 2.1 Integers ve Standart Matematik Operatörleri

Tam sayı değerleri doğrudan bir variable'a assign edilebilir. 
Verinin tipini kontrol etmek için built-in `type()` fonksiyonu kullanılır ve sonuç olarak `int` tipi döner:

```python
In [1]: my_var = 22

In [2]: type(my_var)
Out[2]: int
```

Dört işlem için standart matematik operatörleri geçerlidir: toplama (`+`), çıkarma (`-`), çarpma (`*`) ve bölme (`/`):

```python
In [3]: 10 + 20
Out[3]: 30

In [4]: 30 - 10
Out[4]: 20

In [5]: 5 * 5
Out[5]: 25

In [6]: 4 / 5
Out[6]: 0.8
```

> **Bölme İşleminde Önemli Kural:** Python'da standart tek bölü (`/`) ile yapılan bölme işlemlerinin sonucu her zaman bir **float** olarak döner. İşlem tam sayılar arasında yapılsa ve sonuç kalansız olsa dahi çıktı float tipinde üretilir.

---

### 2.2 Diğer Operatörler: Modulo ve Üs Alma

**1) Modulo Operatörü (`%`):**

Modulo operatörü bir bölme işleminin sonucundaki kalanı verir.

Özellikle bir sayının tek mi yoksa çift mi olduğunu anlamak gibi durumlarda modulo operatörü çözümü oldukça kolaylaştırır. 
Bir sayıyı 2'ye böldüğünüzde kalan 1 geliyorsa sayının tek, kalan 0 geliyorsa sayının çift olduğu anlaşılır. 
Benzer şekilde bir sayı diğerine tam bölünüyorsa modulo sonucu 0 döner:


```python
In [7]: my_var = 9

In [8]: my_var % 2
Out[8]: 1

In [9]: my_var % 3
Out[9]: 0
```

**2) Üs Alma Operatörü (`**`):**

Bir sayının kuvvetini almak için çift yıldız (`**`) kullanılır:

```python
In [10]: 2 ** 3
Out[10]: 8

In [11]: 2 ** 4
Out[11]: 16

In [12]: 2 ** 5
Out[12]: 32
```

---

### 2.3 Floats ve `round()` Fonksiyonu

Ondalıklı sayılar Python'da **float** veri tipi ile temsil edilir. Float tipler üzerinde de standart matematiksel işlemler birebir uygulanır:

```python
In [13]: my_var = 3.5

In [14]: type(my_var)
Out[14]: float

In [15]: 3.5 + 5.5
Out[15]: 9.0

In [16]: 5 / 2
Out[16]: 2.5

In [17]: 3.2 * 2.0
Out[17]: 6.4
```

**Sayıları Yuvarlama:**

Örneğin `4 / 3` bölme işleminde olduğu gibi bazı durumlarda sonuç devirli çıkar ve Python bu değeri bellekte çok sayıda basamakla uzayıp giden bir float olarak tutar.

Bu gibi sayıları belirli bir basamak hassasiyetine yuvarlamak için built-in gelen `round()` fonksiyonu kullanılır. 
İlk argüman olarak yuvarlanacak sayı, ikinci argüman olarak ise virgülden sonra kaç basamak bırakılacağı belirtilir:

```python
In [18]: my_var = 4 / 3

In [19]: my_var
Out[19]: 1.3333333333333333

In [20]: round(my_var, 1)
Out[20]: 1.3

In [21]: round(my_var, 2)
Out[21]: 1.33
```

---

### 2.4 Incrementing | Decrementing: Artırma ve Azaltma

Kod yazarken bir sayaç kurup değerini adım adım artırmak çok yaygın bir ihtiyaçtır. 
Klasik yöntemde değişkene kendisinin 1 fazlası yeniden assign edilir (`i = i + 1`).

String konusunda gördüğümüz kısayol operatörü burada da geçerlidir. **`+=`** operatörü doğrudan `i = i + 1` işleminin yerine geçer ve değişkenin değerini 1 artırır:

```python
In [22]: i = 0

In [23]: i = i + 1

In [24]: i
Out[24]: 1

In [25]: i += 1

In [26]: i
Out[26]: 2

In [27]: i += 1

In [28]: i
Out[28]: 3
```

Aynı mantık değeri adım adım eksiltmek için de geçerlidir. 
Bir değişkenin değerini azaltmak istediğimizde **`-=`** operatörü (`i -= 1`) kullanılır ve her çalıştırıldığında ilgili değişkenin değerini belirtilen miktar kadar düşürür.

> * *integer* → pozitif veya negatif tam sayıları temsil eden temel veri tipi.
> * *float* → ondalıklı sayıları temsil eden veri tipi; standart bölme işlemlerinin sonucu daima float döner.
> * *modulo (`%`)* → bölme işleminden kalan değeri veren operatör.
> * *round()* → float sayıları belirlenen basamak hassasiyetine göre yuvarlayan built-in fonksiyon.
> * *increment / decrement* → bir variable'ın değerini `+=` ile artırma veya `-=` ile azaltma işlemi.

---

## 3. Booleans and None

Python'da karar yapıları ve mantıksal denetimler kurulurken **Booleans** ve Python'a özgü özel bir veri tipi olan **None** kullanılır.

---

### 3.1 Booleans Veri Tipi

Boolean veri tipi yalnızca iki değere sahip olabilir: **True** veya **False**.

Bu değerler tanımlanırken tırnak işareti kullanılmaz. Tırnak içerisine yazılırlarsa string olurlar; bu nedenle doğrudan yazılmalıdırlar. 
Ayrıca **True** ifadesinin `T` harfi, **False** ifadesinin ise `F` harfi mutlaka büyük olmalıdır.

Built-in `type()` fonksiyonu ile kontrol edildiğinde tipinin `bool` olduğu görülür.

Kendi ortamımızda çalıştırma:

```python
In [1]: my_var = True

In [2]: type(my_var)
Out[2]: bool

In [3]: my_var2 = False

In [4]: type(my_var)
Out[4]: bool
```

---

### 3.2 Boolean Mantık Operatörleri

Booleans üzerinde mantıksal sorgular yapmak için üç temel operatör kullanılır:

**1) `and` Operatörü:**

Her iki tarafındaki değerin de `True` olmasını bekler. Eğer değişkenlerden biri bile `False` ise sonuç `False` döner:

```python
In [5]: my_var1 = True

In [6]: my_var2 = True

In [7]: my_var1 and my_var2
Out[7]: True

In [8]: my_var2 = False

In [9]: my_var1 and my_var2
Out[9]: False
```

**2) `or` Operatörü:**

Değişkenlerden en az birinin `True` olması durumunda sonucu `True` döndürür. Yalnızca her iki taraf da `False` ise sonuç `False` olur:

```python
In [10]: my_var1 or my_var2
Out[10]: True
```

**3) `not` Operatörü:**

Mevcut Boolean değerin tam tersini alır. Değer `False` ise `True`, `True` ise `False` yapar:

```python
In [11]: my_var2
Out[11]: False

In [12]: not my_var2
Out[12]: True
```

Bu mantıksal operatörler, kursun ilerleyen kısımlarında detaylıca işlenecek olan `if` ve `elif` conditional statement yani koşullu durum yapılarının temelini oluşturur:

```python
In [13]: my_var1
Out[13]: True

In [14]: if my_var1:
    ...:      print("Merhaba!")
Merhaba!
```

---

### 3.3 Truish Kavramı ve Boolean Context

Python'da bir `if` koşuluna yalnızca saf Boolean (`True`/`False`) değerler verilmek zorunda değildir. 
Boolean olmayan diğer veri tipleri de bir **Boolean context** içerisinde değerlendirilebilir.

Python, her bir veri tipi için **boş** ya da **sıfır** kabul edilen tek bir değeri `False` olarak tanımlar; o veri tipine ait geri kalan tüm değerleri ise `True` kabul eder. 
Bu duruma genel olarak **truish** denir.

Bir verinin Boolean context içerisindeki karşılığını görmek için `bool()` fonksiyonu kullanılır:

**1) Strings:**

String veri tipinde boş string (`""`) `False` olarak evaluate edilir. İçerisinde en az bir karakter olan diğer tüm stringler ise `True` döner:

```python
In [15]: my_var1 = "bir string"

In [16]: type(my_var1)
Out[16]: str

In [17]: bool(my_var1)
Out[17]: True

In [18]: my_var1 = ""

In [19]: bool(my_var1)
Out[19]: False
```

Dolu bir string doğrudan `if` ifadesine verildiğinde `True` gibi işlem görür:

```python
In [20]: my_var1 = "bir string"

In [21]: if my_var1:
    ...:      print("Merhaba!")
Merhaba!
```

**2) Integers:**

Sayısal değerlerde yalnızca `0` değeri `False` kabul edilir. Sıfır dışındaki tüm pozitif ve negatif integer değerleri `True` olarak ele alınır:

```python
In [22]: my_var1 = 0

In [23]: bool(my_var1)
Out[23]: False

In [24]: my_var1 = 10

In [25]: bool(my_var1)
Out[25]: True
```

**3) Lists ve Diğer Veri Yapıları:**

Listeler için boş liste (`[]`) `False` değer üretir. İçerisinde en az bir eleman bulunan tüm listeler `True` döner. 
Aynı kural dictionaries, sets ve floats için de geçerlidir; boş/sıfır olan tek durum `False`, diğer tüm durumlar `True` olur:

```python
In [26]: my_var1 = []

In [27]: bool(my_var1)
Out[27]: False
```

---

### 3.4 None Veri Tipi

Python'da **None**, bir değerin yokluğunu temsil eden özel bir veri tipidir ve diğer dillerdeki `null` değerine karşılık gelir.

Kendine ait bir tipi vardır (`NoneType`) ve alabileceği tek değer yine `None` ifadesidir. 
Ayrıca Python'da bir fonksiyon içerisinden herhangi bir return değeri belirtilmediğinde varsayılan olarak dönen default değer `None` olur.

`None` değeri Boolean context içinde evaluate edildiğinde doğal olarak geriye **False** döner:

```python
In [28]: my_var1 = None

In [29]: type(my_var1)
Out[29]: NoneType

In [30]: bool(my_var1)
Out[30]: False
```

> Bir değişkenin değerinin `None` olup olmadığını denetlemek için genellikle `if my_value is None:` yapısı kullanılır.

> * *bool* → yalnızca `True` ve `False` mantıksal değerlerini barındıran veri tipi.
> * *logical and* → bağlı iki ifadenin de `True` olması durumunda `True` döndüren mantıksal operatör.
> * *logical or* → ifadelerden birinin `True` olması halinde `True` döndüren mantıksal operatör.
> * *logical complement (not)* → Boolean değerin mantıksal tersini üreten operatör.
> * *truish* → Boolean olmayan veri tiplerinin boş/sıfır durumlarına göre `True` ya da `False` değerlendirilmesi.
> * *NoneType* → Python'da tanımsızlığı ve yokluğu temsil eden, `null` karşılığı olan özel `None` veri tipi.

---
