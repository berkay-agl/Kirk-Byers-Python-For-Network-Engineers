# Lesson 3 Hakkında

## 1. Giriş: Table of Contents

Lesson 3 kapsamında Python conditionals, loops, list comprehensions ve generator expressions konuları ele alınmaktadır.

Kirk Byers bu derste sırasıyla aşağıdaki konuları işleyeceğini belirtmektedir:

* **Conditionals:** `if`, `elif` ve `else` statement yapılarının nasıl kurulacağı.
* **For Loops:** Python döngü yapıları.
* **While Loops:** `while` döngüleri ile birlikte `continue` ve `break` ifadeleri.
* **List Comprehensions:** Mevcut bir listeden dinamik olarak yeni bir list oluşturma yöntemi.
* **Generator Expressions:** List comprehension yapısına çok benzeyen ve sonrasındaki for loop'larda kullanılmak üzere dinamik olarak bir generator oluşturan yapılar.

> * *conditionals* → `if`, `elif` ve `else` statement kullanılarak oluşturulan karar yapıları.
> * *for loops* → Python'da döngü kurmayı sağlayan temel loop yapısı.
> * *while loops* → belirli bir koşul devam ettiği sürece çalışan döngü yapısı.
> * *continue / break* → loop akışını kontrol eden ifadeler.
> * *list comprehensions* → var olan bir list üzerinden dinamik olarak yeni bir list generate etme yöntemi. 
> * *generator expressions* → list comprehension benzeri syntax ile dinamik generator oluşturan yapılar.


---

## 2. Python Conditionals

Python'da kararlar almak ve program akışını mantıksal sonuçlara göre dallandırmak için **conditionals** yani koşullu durum yapıları kullanılır.

---

### 2.1 Syntax Yapısı ve Indented Block

Temel koşul yapısı `if` ifadesi ile kurulur. 
`if` anahtar kelimesinden sonra bir **expression** yani ifade yer alır. Bu ifade arka planda evaluate edilerek bir Boolean (`True` veya `False`) değer üretir.

Satır sonundaki colon (`:`) karakteri indented yani girintili bir bloğun başlayacağını bildirir. 
Koşul `True` olarak evaluate edilirse bu indented block içerisindeki satırlar çalıştırılır. 
Bu blok tek bir satır olabileceği gibi yüzlerce satırdan da oluşabilir.

```python
In [1]: ip_addr = "192.168.1.1"

In [2]: if "192.168" in ip_addr:
   ...:      print("Adres içinde 192.168 geçiyor.")
   ...: 
Adres içinde 192.168 geçiyor.
```

---

### 2.2 `if`, `elif` ve `else` ile Çoklu Seçimler

Birden fazla seçeneğin bulunduğu durumlarda `if`, `elif` ve `else` blokları birlikte kurgulanır:

* **`if`:** İlk kontrol noktasıdır; yapıda bulunması zorunlu olan tek kısımdır.
* **`elif`:** Kendisinden önceki kontrol `False` olduğunda sıradaki alternatifi evaluate eder. Bir koşul yapısında hiç olmayabileceği gibi 5, 10 veya daha fazla sayıda `elif` bloğu da zincirlenebilir.
* **`else`:** Öncesindeki tüm `if` ve `elif` ifadeleri `False` çıktığında devreye giren son yakalama bloğudur buna **catch-all statement** deniliyor. Kullanımı opsiyoneldir.

> **Kritik Kural:** Bu zincirde **yalnızca tek bir blok** çalıştırılır. Hangi blok `True` evaluate edilirse sadece o bloğun kodu yürütülür ve yapının geri kalanı atlanır.

```python
In [3]: expression = "bir string"

In [4]: if expression:
   ...:      print("Merhaba!")
   ...:      print("İkinci Merhaba!")
   ...: elif ikinci_expression:
   ...:      print("Başka yazı...")
   ...:      print("Selam!")
   ...: else:
   ...:      print("else")
   ...:      print("Merhaba!")
   ...: 
Merhaba!
İkinci Merhaba!
```

---

### 2.3 Karşılaştırma Operatörleri 

Koşullu ifadeleri oluştururken kullanılan temel karşılaştırma operatörleri şunlardır:

* `==` : Eşitlik kontrolü (Comparison equals)
* `!=` : Eşit değil kontrolü (Not equals)
* `>` , `>=` : Büyüktür ve büyük eşittir (Greater than / Greater than or equal to)
* `<` , `<=` : Küçüktür ve küçük eşittir (Less than / Less than or equal to)

```python
In [5]: ssh_timeout = 10

In [6]: if ssh_timeout == 5:
   ...:      print("SSH timeout süresi: 5 saniye.")
   ...: elif ssh_timeout > 15:
   ...:      print("SSH timeout süresi 15 saniyeden fazla.")
   ...: else:
   ...:      print("Bilinmeyen SSH timeout süresi.")
   ...: 
Bilinmeyen SSH timeout süresi.
```

---

### 2.4 Mantıksal Operatörler: `and`, `or` ve `not`

Birden fazla koşulu tek bir expression içinde birleştirmek için mantıksal operatörler kullanılır:

* **`and` (Logical AND):** İfadenin `True` sayılması için her iki tarafındaki tüm şartların da `True` olması zorunludur.
* **`or` (Logical OR):** Bağlanan şartlardan en az birinin `True` olması durumunda tüm ifadeyi `True` yapar.
* **`not`:** Boolean değerin tersini alır (`True` ise `False`, `False` ise `True` yapar).

```python
In [11]: ssh_timeout = 10

In [12]: host_ulasilabilir = True

In [13]: ip_addr = "192.168.1.1"

In [16]: if host_ulasilabilir and ssh_timeout >= 5:
    ...:      print("Connection sağlanıyor...")
    ...: elif not host_ulasilabilir or ip_addr == "192.168.1.1":
    ...:      print("Host çözümlenemedi. Connection sağlanamıyor.")
    ...: else:
    ...:      print("Bilinmeyen hata!")
    ...: 
Connection sağlanıyor...
```

---

### 2.5 Nested Koşullar (İç İçe)

Koşul bloklarının içerisine ihtiyaca göre yeni koşul blokları yerleştirilebilir. 
Bu hiyerarşi kodun gereksinimine göre birden fazla derinlik seviyesine kadar uzanabilir.

Her iç blok colon (`:`) sonrasında 4 space daha içeriye girintilenir:

```python
In [7]: ssh_timeout = 10

In [8]: host_ulasilabilir = True

In [9]: if host_ulasilabilir:
   ...:      if ssh_timeout is not None:
   ...:          print("Connection sağlanıyor...")
   ...:      else:
   ...:          print("ssh_timeout tanımlı değil!")
   ...: 
Connection sağlanıyor...
```

---

### 2.6 Idiomatic Expressions

Python'da belirli kontrollerin yazılması tercih edilen standart biçimler vardır; Kirk Byers bunları **idiomatic expressions** olarak adlandırır. 
Kodun okunabilirliği ve linter araçlarının hata vermemesi açısından bu kurallara uyulması önerilir:

* **`None` Kontrolü:** `== None` yerine doğrudan **`is None`** kullanılır. Bellekte tek bir `None` object bulunduğu için kimlik denetimi yapılır.
* **`None` Değildir Kontrolü:** `not ... is None` yerine **`is not None`** syntax'ı tercih edilir.
* **Boolean Değer Kontrolleri:** `== False` veya `== True` yerine **`is False`** ya da **`is True`** kalıpları kullanılır.

```python
In [17]: ssh_timeout = 10

In [18]: host_ulasilabilir = True

In [19]: ip_addr = None

In [20]: if ssh_timeout is None:
    ...:      print("Hata: SSH timeout bulunamadı.")
    ...: if host_ulasilabilir is False:
    ...:      print("Hata: host ulaşılabilir değil.")
    ...: if ip_addr is not None:
    ...:      print("IP Address connection: OK")
    ...: 
```

---

### 2.7 "Truish" Kavramı ve Koşullarda Dikkat Edilmesi Gerekenler

Python'da her veri tipinin `False` kabul edildiği tek bir boş/sıfır durumu bulunur; geri kalan tüm değerler `True` sayılır:

* Integers için `0`
* Floats için `0.0`
* Strings için boş string `""`
* Lists için boş liste `[]`
* `None` ve `False`

`if not variable:` gibi bir kontrol kurgulandığında; değişkenin `0`, `""`, `None` veya `False` olması durumlarının tamamı `True` olarak evaluate edilir.

Kirk Byers bu noktada dikkatli olunması gerektiğini vurgular: Değişkenin `0` olması ile `None` olması kodunuzda farklı anlamlara gelebilir. 
Eğer ikisine farklı tepkiler verilmesi gerekiyorsa saf truish kontrolü yerine açık bir `is None` sorgusu tercih edilmelidir.


```python
In [21]: ssh_timeout = 0

In [22]: if not ssh_timeout:
    ...:      print("Hata: SSH timeout bulunamadı.")
    ...: 
Hata: SSH timeout bulunamadı.
```

> * *conditionals* → kodun belirli mantıksal şartlara göre dallanmasını sağlayan karar yapıları (`if`, `elif`, `else`).
> * *expression* → `True` veya `False` Boolean değerine indirgenen koşul ifadesi.
> * *catch-all (else)* → önceki tüm şartların `False` çıkması durumunda mutlaka çalışan son blok. 
> * *nesting conditionals* → koşul bloklarının hiyerarşik olarak birbiri içine yerleştirilmesi.
> * *idiomatic expressions* → Python topluluğunda ve linter araçlarında standart kabul edilen, okunabilirliği yüksek yazım kalıpları (`is None`, `is not None`).
> * *truish* → Boolean olmayan veri tiplerinin boş ya da sıfır olma durumlarına göre `False`, diğer tüm durumlarına göre `True` evaluate edilmesi. 

---
