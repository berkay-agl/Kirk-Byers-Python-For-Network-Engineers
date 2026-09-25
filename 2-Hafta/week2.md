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

