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

## 3. Python For Loops

Python'da döngü kurmanın en temel ve yaygın yöntemi **for loop** yapısıdır. 
Bir veri koleksiyonu (örneğin bir list) üzerindeki elemanları sırayla tek tek işlemek için kullanılır.

---

### 3.1 Syntax Yapısı ve Çalışma Mekaniği

For loop tanımlanırken `for` keyword'ü, bir **loop variable**, `in` keyword'ü ve üzerinde dönülecek olan koleksiyon nesnesi belirtilir. 
Satır sonundaki colon (`:`) sonrasında indented block başlar.

```python
In [1]: ip_list = [
   ...: "192.168.1.1",
   ...: "192.168.1.2",
   ...: "192.168.1.3",
   ...: "192.168.1.4",
   ...: ]

In [2]: for ip in ip_list:
   ...:      print(ip)
   ...: 
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
```

* **Loop Variable:** Buradaki `ip` ismi keyfidir; istenirse `x` ya da başka bir isim verilebilir.
* **Her İterasyondaki Değer:** Döngünün her adımında (`loop iteration`), listeden sıradaki bir eleman kopyalanıp `ip` değişkenine atanır (1. iterasyonda `"192.168.1.1"`, 2. iterasyonda `"192.168.1.2"` vb.).
* **Listenin Korunması:** Döngü boyunca orijinal listenin kendisi hiçbir değişikliğe uğramaz.

---

### 3.2 Iterator Kavramı ve Stringler Üzerinde Döngü

Python'da üzerinde döngü kurulabilecek yapılar sadece listelerle sınırlı değildir; bu yapılara genel olarak **iterator** denir. 
Iterator, üzerinde her döngü adımında size sıradaki tek bir elemanı veren nesneleri ifade eder. 
Listeler, tuple'lar, dictionary'ler, set'ler ve string'ler birer iterator örneğidir.

String'ler üzerinde for loop kurulduğunda, döngü her adımda sıradaki tek bir karakteri teslim eder:

```python
In [3]: for harf in "bir string":
   ...:      print(harf)
   ...: 
b
i
r
 
s
t
r
i
n
g
```

---

### 3.3 Akış Denetimi: `break` ve `continue`

**1) Döngüyü Tamamen Sonlandırma (`break`):**

`break` keyword'ü çalıştırıldığı anda döngü o milisaniyede derhal sonlandırılır ve doğrudan for loop bloğunun dışına çıkılır:

```python
In [4]: for i in range(10):
   ...:      print(i)
   ...:      if i == 5:
   ...:          break
   ...: print(f"---> {i}")
0
1
2
3
4
5
---> 5
```

`range(10)` 0'dan 9'a kadar sayılar üretir. Değişken `5` olduğunda ekrana yazdırılır, ardından `if` koşulu sağlanarak `break` devreye girer; 6, 7, 8 ve 9 değerleri hiç işlenmeden döngü sonlanır. Dışarıdaki print ifadesinde `i` değeri en son `5` olarak kalır.

**2) Sıradaki İterasyona Atlama (`continue`):**

`continue` keyword'ü döngüyü tamamen kırmaz; yalnızca o anki döngü adımını yarıda kesip derhal döngünün başına döner ve sıradaki elemana geçer:

```python
In [5]: for i in range(10):
   ...:      if i == 5:
   ...:          continue
   ...:      print(i)
   ...: print(f"---> {i}")
0
1
2
3
4
6
7
8
9
---> 9
```

`i == 5` olduğunda `continue` tetiklenir; bu yüzden `print(5)` satırı atlanır ve döngü doğrudan `6` değeriyle devam eder. 
Döngü normal akışıyla 9'a kadar çalıştığı için döngü bittiğinde `i` değeri `9` olur.

---

### 3.4 Nested Loops ve Unpacking

For döngüleri iç içe yerleştirilebilir: **nested for loops**. 
Bu yapı kodun mantığına göre istenilen derinlik seviyesine kadar uzanabilir.

Elemanları iki elemanlı tuple'lardan oluşan bir listede, Python döngü satırında otomatik **unpacking** yapma yeteneğine sahiptir:

```python
In [11]: veri_merkezleri = [
    ...: ("sf1", "192.100.10."),
    ...: ("sf2", "192.100.20.")
    ...: ]

In [12]: for vm, base_addr in veri_merkezleri:
    ...:      for net_addr in range(1, 5):
    ...:          print(f"{vm} ---> {base_addr}{net_addr}")
    ...: 
sf1 ---> 192.100.10.1
sf1 ---> 192.100.10.2
sf1 ---> 192.100.10.3
sf1 ---> 192.100.10.4
sf2 ---> 192.100.20.1
sf2 ---> 192.100.20.2
sf2 ---> 192.100.20.3
sf2 ---> 192.100.20.4
```

* **Dış - Outermost Loop:** `veri_merkezleri` listesindeki ilk tuple'ı alır ve unpacking yaparak `vm = "sf1"`, `base_addr = "192.100.10."` atamasını gerçekleştirir.
* **İç - Inner Loop):** `range(1, 5)` üzerinden `1, 2, 3, 4` sayılarını dönerek 4 satır çıktı üretir.

* İç döngü tamamlandığında dış döngü sıradaki `"sf2"` elemanına geçer ve iç döngü onun için de baştan sona tekrar çalışır.

---

### 3.5 `enumerate()` ile İndeks ve Değeri Birlikte Alma

Bir liste üzerinde dönerken aynı anda hem elemanın **indeks numarasını** hem de **kendisini** almak istediğimizde **`enumerate()`** built-in fonksiyonu kullanılır.

`enumerate()` fonksiyonu her iterasyonda geriye iki elemanlı bir **tuple** döndürür: İlk eleman indeks numarası, ikinci eleman ise listedeki gerçek değerdir. 
Döngü tanımında iki değişken verilerek unpacking yapılır:

```python
In [13]: veri_merkezleri = ["sf1", "sf2", "la1", "la2", "dallas"]

In [14]: for i, vm in enumerate(veri_merkezleri):
    ...:      print(f"{i} --> {vm}")
    ...: 
0 --> sf1
1 --> sf2
2 --> la1
3 --> la2
4 --> dallas
```

Burada `i` indeks numarasını (`0, 1, 2...`), `vm` ise listenin elemanını (`"sf1"`, `"sf2"...`) temsil eder.

---

### 3.6 Boş Liste Üzerinde Döngü ve `pass` Keyword'ü

**Boş Listede Döngü:**

Eğer boş bir liste (`[]`) üzerinde for loop çalıştırılırsa Python hiçbir syntax hatası vermez; ancak listede işlenecek eleman bulunmadığı için döngü bloğuna hiç girmeden derhal sonlanır:

```python
In [15]: for element in []:
    ...:      print("Burası print olacak mı?")
    ...: 
```

**`pass` Keyword:**

Python'da iki nokta (`:`) konulduğunda mutlaka altına girintili bir blok yazılması zorunludur. 
Eğer döngü gövdesinde şimdilik hiçbir şey yapılmasını istemiyorsanız, yer tutucu olarak **`pass`** keyword'ü kullanılır. 
Bu ifade Python'da bir **no-op** (no operation) görevi görür; yani hiçbir işlem yapmadan akışı sürdürür:

```python
In [16]: for vm in veri_merkezleri:
    ...:      pass
    ...: 
```

---

### 3.7 For Döngülerinde `else` Bloğu 

Python'da for döngülerinin sonuna bir **`else`** bloğu eklenebilir. Kirk Byers bu yapıyı *"the mythical else clause / efsanevi else ifadesi"* olarak adlandırır.
Bu `else` bloğunun çalışma kuralı çok nettir: Döngü boyunca hiçbir `break` ifadesiyle karşılaşılmadıysa `else` bloğu çalıştırılır.

**1) Break Çalıştığında (`else` Atlanır):**

```python
In [17]: for i in range(1, 10):
    ...:      print(i)
    ...:      if i == 5:
    ...:          break
    ...: else:
    ...:      print("Hiçbir 'break' yaşanmadı.")
    ...: 
1
2
3
4
5
```

Döngü `5` değerinde bir `break` ile karşılaşıp kırıldığı için for bloğuna bağlı `else` kısmı kesinlikle yürütülmez.

**2) Break Çalışmadığında (`else` Yürütülür):**

```python
In [18]: for i in range(1, 10):
    ...:      print(i)
    ...:      if i == 20:
    ...:          break
    ...: else:
    ...:      print("Hiçbir 'break' yaşanmadı.")
    ...: 
1
2
3
4
5
6
7
8
9
Hiçbir 'break' yaşanmadı.
```

`range(1, 10)` yalnızca 1'den 9'a kadar sayılar üretir; `i == 20` koşulu hiçbir zaman sağlanmaz ve döngü asla `break` görmez. 
Döngü doğal yoldan tamamlandığı için hemen ardından `else` bloğu devreye girer ve mesajı ekrana basar.

> * *for loop* → bir koleksiyonun veya dizinin elemanlarını sırayla işlemek için kullanılan döngü yapısı.
> * *loop variable* → döngünün her iterasyonunda sıradaki elemanı tutan değişken.
> * *iterator* → üzerinde döngü kurulabilen ve her adımda sıradaki tek bir elemanı veren nesne.
> * *break* → for veya while döngüsünü o anda tamamen sonlandıran akış ifadesi.
> * *continue* → mevcut iterasyonun geri kalanını atlayarak doğrudan bir sonraki döngü adımına geçiren ifade.
> * *nested loop* → bir for döngüsünün içerisine başka bir döngünün yerleştirilmesi.
> * *unpacking* → tuple gibi paketli yapıların elemanlarını döngü tanımında birden fazla değişkene (`for vm, base_addr in ...`) doğrudan dağıtma mekanizması.
> * *enumerate()* → döngü esnasında hem indeks numarasını hem de listenin ilgili elemanını tuple olarak döndüren built-in fonksiyon.
> * *pass (no-op)* → syntax gereği boş bırakılamayan kod bloklarında hiçbir işlem yapmamak üzere konulan yer tutucu.
> * *for-else* → döngü bir `break` ile kesilmeden doğal olarak tamamlandığında çalışan blok yapısı.

---

## 4. Python While Loops

Python'da döngü kurmanın bir diğer temel yöntemi **while loop** yapılarıdır. 
Bir veri koleksiyonunu baştan sona tüketmek yerine, belirli bir mantıksal koşul `True` kaldığı sürece çalışmaya devam eden döngüler oluşturmak için kullanılır.

---

### 4.1 Syntax Yapısı ve Çalışma Mekaniği

While döngüsü `while` keyword'ü ve ardından gelen bir **expression** yani koşul ifadesi ile tanımlanır. 
Satır sonundaki colon (`:`) karakterinden sonra indented block başlar:

```python
while expression:
    print("A message")
    print("A second message")
```

Bu ifade `True` olarak evaluate edildiği sürece döngünün gövdesindeki komutlar çalıştırılır. 
Bloğun sonuna gelindiğinde Python tekrar en başa döner ve koşul ifadesini yeniden değerlendirir. Koşul `False` değerine düştüğünde döngü sonlanır.

Döngünün doğal olarak sonlanması için döngü gövdesi içinde koşulun `False` olmasını sağlayacak bir durumun gerçekleşmesi (örneğin bir sayacın artırılması) ya da bir `break` ifadesinin çalışması gerekir.

Kirk Byers'ın ilk örnekte belirttiği sayaç yapısı:

```python
i = 1
while i <= 5:
    # do something
    print(i)
    if i == 5:
        break
    i += 1
```

Burada `i` değişkeni `1` olarak initialize edilir; `i <= 5` koşulu doğru kaldığı sürece döngü devam eder, `i += 1` ile artırılır ve `i == 5` olduğunda ya da ifade `False` olduğunda döngüden çıkılır.

---

### 4.2 Sonsuz Döngü Tuzağı ve `continue`

While döngülerinde en sık karşılaşılan problem **infinite loops** yani sonsuz döngü durumudur. 
Eğer döngüden çıkışı sağlayacak koşul hiçbir zaman `False` olmuyorsa veya sayaç güncellenemiyorsa döngü sonsuza kadar çalışır ve program kilitlenir.

Özellikle **`continue`** kullanılırken sayaç artırımı atlanırsa sonsuz döngü meydana gelir:

```python
#!/usr/bin/env python3

i = 0
while i <= 5:
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
    i += 1
```

Bu script çalıştırıldığında çıktıda döngü `2` değerinden sonra takılı kalır:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-3$ python while_loop.py 
0
1
2
^CTraceback (most recent call last):
  File "/home/berkay/Desktop/Python-All/Python-For-Network-Engineers/Week-3/while_loop.py", line 6, in <module>
    continue
KeyboardInterrupt
```

* `i = 0`, `1`, `2` değerlerinde sayaç normal şekilde `i += 1` ile artar ve sayılar ekrana basılır.
* Sayaç `3` değerine ulaştığında `if i == 3:` bloğu devreye girer ve `continue` çalıştırılır.
* `continue` ifadesi altındaki `print(i)` ve `i += 1` satırlarını atlayarak anında döngünün en başına zıplar.
* Sayaç artırılamadığı için `i` değeri sürekli `3` olarak kalır ve `3 <= 5` koşulu daima `True` döndüğünden program sonsuz döngüye girer. Programı durdurmak için terminalden `CTRL+C` (`KeyboardInterrupt`) ile müdahale etmek zorunda kalınır.

**Sonsuz Döngünün Düzeltilmesi:**

Bu sorunu çözmek için `continue` çağrılmadan hemen önce sayacın manuel olarak artırılması gerekir:

```python
#!/usr/bin/env python3

i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("'break' olmadı ?!")
```

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-3$ python while_loop.py 
0
1
2
4
```

`i == 3` olduğunda önce `i += 1` yapılarak değer `4`'e çıkarılır, ardından `continue` çalıştırılır. Böylece `3` değeri ekrana basılmadan atlanır ve döngü kilitlenmeden devam eder. `i == 5` olduğunda ise `break` tetiklenerek döngü sonlanır.

---

### 4.3 Akış Denetimi Benzerlikleri: `break`, `continue` ve `else`

For döngülerinde kullanılan akış denetim ifadeleri while döngülerinde de tamamen aynı şekilde çalışır:

* **`break`:** Döngüyü anında sonlandırır ve while bloğunun dışına çıkar.
* **`continue`:** Mevcut iterasyonun geri kalanını atlayarak doğrudan while koşul kontrolüne geri döner.
* **`else` Bloğu:** For döngüsünde olduğu gibi while döngüsünün sonuna da opsiyonel bir `else` bloğu eklenebilir. Bu blok, **döngü hiçbir `break` ifadesiyle karşılaşmadan** koşulun `False` olmasıyla doğal yoldan tamamlandığında çalışır. Yukarıdaki scriptte `i == 5` olduğunda `break` çalıştığı için `else` bloğu yürütülmemiştir.

---

### 4.4 `while True` Kalıbı

While döngülerinde yaygın olarak kullanılan bir diğer yapı, koşul kısmına doğrudan `True` yazılarak kurulan **`while True:`** kalıbıdır.

```python
while True:
    if condition:
        break

    # do something
    pass
```

Bu yapıda koşul ifadesi hiçbir zaman `False` değerine düşmeyeceği için döngünün tek çıkış yolu blok içerisinde bir **`break`** keyword'ü ile karşılaşmaktır. Çıkış şartı sağlandığında `break` tetiklenir ve döngü kırılır.

---

### 4.5 Nested Loops 

While döngüleri kendi içlerinde veya for döngüleri ile birlikte iç içe kullanılabilir. Bu yapılar kodun gereksinimine göre birden fazla derinlik seviyesine kadar uzanabilir.

**1) While İçinde While:**

```python
In [1]: base_addr = "192.168"

In [2]: oktet_3 = 0

In [3]: while oktet_3 < 10:
   ...:      oktet_4 = 2
   ...:      while oktet_4 < 255:
   ...:          ip_addr = f"{base_addr}.{oktet_3}.{oktet_4}"
   ...:          print(f"IP Adresi: {ip_addr}")
   ...:          oktet_4 += 1
   ...:      oktet_3 += 1
   ...: 
IP Adresi: 192.168.0.2
IP Adresi: 192.168.0.3
IP Adresi: 192.168.0.4
IP Adresi: 192.168.0.5
IP Adresi: 192.168.0.6
IP Adresi: 192.168.0.7
IP Adresi: 192.168.0.8
IP Adresi: 192.168.0.9
IP Adresi: 192.168.0.10
...
```

Dış döngü `oktet_3` değerini `0`'dan `9`'a kadar yönetirken, içteki while döngüsü her bir 3. oktet için `oktet_4` değerini `2`'den `254`'e kadar döndürür ve sayaçlar manuel olarak (`+= 1`) artırılır.

**2) While İçinde For Loop:**

```python
In [8]: base_addr = "192.168"

In [9]: oktet_3 = 0

In [10]: while oktet_3 < 10:
   ...:      for oktet_4 in range(2, 255):
   ...:          ip_addr = f"{base_addr}.{oktet_3}.{oktet_4}"
   ...:          print(f"IP Adresi: {ip_addr}")
   ...:      oktet_3 += 1
   ...: 
IP Adresi: 192.168.0.2
IP Adresi: 192.168.0.3
IP Adresi: 192.168.0.4
IP Adresi: 192.168.0.5
IP Adresi: 192.168.0.6
IP Adresi: 192.168.0.7
IP Adresi: 192.168.0.8
IP Adresi: 192.168.0.9
IP Adresi: 192.168.0.10
...
```

Burada dış döngü `while` ile kontrol edilirken, iç kısımdaki sayaç yönetimi `range(2, 255)` kullanan bir `for` döngüsüne devredilmiştir.

---

### 4.6 For Loops vs While Loops Karşılaştırması

Kirk Byers iki döngü yapısı arasındaki temel kavramsal farkı şu şekilde özetler:

* **For Loops (Collection-based):** Bir veri koleksiyonu (list, tuple vb.) üzerinde gezinmek için kullanılır. Mantık olarak bir **"for each"** yapısıdır; koleksiyondan sıradaki elemanı alır, işlemlerini yapar ve tüm elemanlar tükenene kadar devam eder.

* **While Loops (Event-based):** Koleksiyonlardan ziyade **olay tabanlıdır**. Belirli bir koşul sağlandığında döngüye girilir ve döngüden çıkmayı tetikleyecek bir olay (koşulun `False` olması veya `break`) gerçekleşene kadar döngü içinde kalınır.

> * *while loop* → belirtilen mantıksal koşul doğru (`True`) kaldığı sürece çalışan olay tabanlı döngü yapısı.
> * *infinite loop* → döngüden çıkış koşulunun hiçbir zaman sağlanamaması sebebiyle programın kilitlenip sonsuza kadar çalışması durumu.
> * *while True* → döngüden çıkışın yalnızca dahili bir `break` ifadesi ile mümkün olduğu kalıp.
> * *while-else* → döngü herhangi bir `break` ile kesilmeden koşulun `False` olmasıyla doğal olarak bittiğinde çalışan blok.
> * *event-based* → döngünün eleman sayısına göre değil, belirli bir durumun/olayın gerçekleşmesine göre çalışıp sonlanması mantığı.

---

test
