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

## 4. Dosya İşlemleri: Dosyadan Okuma Yapma 

Python'da dosya işlemleri ağ otomasyonunda cihaz çıktılarını, konfigürasyonları ve logları işlerken en temel konulardan biridir.

Kirk Byers bu bölümde dosyaları okumanın ilk ve temel yöntemini — henüz bir **context manager** yani `with` yapısı kullanmadan — ele alıyor. 
Python'da `with` bloğu kullanmak daha standart ve doğru kabul edilen yöntem olsa da, dosya mekanizmasının temelini kavramak adına ilk olarak bu basit yapı incelenmektedir.

---

### 4.1 Dosyayı Açma ve Default Mod

Bir dosyayı açmak için `open()` fonksiyonu kullanılır ve parametre olarak dosya ismi verilir:

```python
In [1]: f = open("show_version.txt")
```

Python burada dosya yolu verilmediğinde, dosyayı doğrudan komut satırını çalıştırdığınız **current working directory** yani mevcut çalışma dizini içinde arar.

`open()` çağrıldığında geriye `f` şeklinde bir **file handle** döner. Bu değişken doğrudan incelendiğinde dosyanın özellikleri görülür:

```python
In [5]: f
Out[5]: <_io.TextIOWrapper name='show_version.txt' mode='r' encoding='UTF-8'>
```

* **Default Mode (`mode='r'`):** `open()` fonksiyonuna herhangi bir mod belirtilmediğinde dosya default olarak **read** yani okuma modunda açılır.

* **Text File:** Dosya default olarak bir metin dosyası şeklinde işleme alınır.

* **Explicit Tanımlama:** İstenirse mod açık bir şekilde `mode="r"` olarak da belirtilebilir:

```python
In [6]: f = open("show_version.txt", mode="r")
```

---

### 4.2 Dosya İçeriğini Okuma Yöntemleri

Dosyadaki verileri okumak için farklı metotlar mevcuttur:

**1) `.read()` Metodu:**

Dosyanın tüm içeriğini baştan sona tek bir **string** olarak okur. 
Okunan veri bir variable'a atanır ve ardından dosya kapatılır:

```python
In [1]: f = open("show_version.txt")

In [2]: data = f.read()

In [3]: f.close()

In [4]: data
Out[4]: 'Switch> show version\nCisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE4, RELEASE SOFTWARE (fc1)\nTechnical Support: http://cisco.com\nCopyright (c) 1986-2013 by Cisco Systems, Inc.\nCompiled Wed 26-Jun-13 02:49 by prod_rel_team\n\nROM: Bootstrap program is 2960 Boot Loader\nBOOTLDR: C2960 Boot Loader version 12.2(44)SE5, RELEASE SOFTWARE (fc1)\n\nSwitch uptime is 39 minutes\nSystem returned to ROM by power-on\nSystem image file is "flash:c2960-lanbasek9-mz.150-2.SE4.bin"\nLast reload reason: Power-on\n\n\n\nThis product contains cryptographic features and is subject to United\nStates and local country laws governing import, export, transfer and\nuse. Delivery of Cisco cryptographic products does not imply\nthird-party authority to import, export, distribute or use encryption.\nImporters, exporters, distributors and users are responsible for\ncompliance with U.S. and local country laws. Malicious use of this\nsoftware is a violation of U.S. and international law.\n\nCisco WS-C2960-24TT-L (PowerPC405) processor (revision B0) with 65536K bytes of memory.\nProcessor board ID FOC1432Y101\nLast reset from power-on\n1 Virtual Ethernet interface\n24 FastEthernet interfaces\n2 Gigabit Ethernet interfaces\n64K bytes of flash-simulated non-volatile configuration memory.\nBase ethernet MAC Address       : 00:2A:6A:3B:4C:D0\nMotherboard assembly number     : 73-9834-08\nPower supply part number        : 341-0097-02\nMotherboard serial number       : FOC143105X5\nPower supply serial number      : LIT14280E1A\nModel revision number           : B0\nMotherboard revision number     : A0\nModel number                    : WS-C2960-24TT-L\n\nConfiguration register is 0xF\n'
```

**2) `.readline()` Metodu:**

Dosyayı satır satır okumayı sağlar. Metot her çağrıldığında sıradaki tek bir satırı string olarak döndürür:

```python
In [6]: f = open("show_version.txt", mode="r")

In [7]: f.readline()
Out[7]: 'Switch> show version\n'
```

**3) `.seek()` ile Başa Dönme:**

Dosyadan veri okundukça imleç dosya içinde ileriye doğru hareket eder. Dosyayı kapatıp yeniden açmadan tekrar en başa sarmak gerektiğinde `seek(0)` kullanılır:

```python
In [8]: f.seek(0)
Out[8]: 0

In [17]: f = open("show_version.txt")

In [18]: f.readline()
Out[18]: 'Switch> show version\n'

In [19]: f.readline
Out[19]: <function TextIOWrapper.readline(size=-1, /)>

In [20]: f.seek(0)
Out[20]: 0

In [21]: f.readline()
Out[21]: 'Switch> show version\n'
```

**4) `.readlines()` Metodu:**

Sonunda çoğul eki olan `s` harfi bulunur. Dosyadaki tüm satırları okur ve her bir satırı ayrı bir string eleman olacak şekilde tek bir **list** haline getirir.

Elde edilen bu liste üzerinde for loop kurarak gezinebilir veya satırlara indeks numaraları ile erişebilirsiniz:

```python
In [9]: data = f.readlines()

In [10]: data
Out[10]: 
['Switch> show version\n',
 'Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE4, RELEASE SOFTWARE (fc1)\n',
 'Technical Support: http://cisco.com\n',
 'Copyright (c) 1986-2013 by Cisco Systems, Inc.\n',
 'Compiled Wed 26-Jun-13 02:49 by prod_rel_team\n',
 '\n',
 'ROM: Bootstrap program is 2960 Boot Loader\n',
 'BOOTLDR: C2960 Boot Loader version 12.2(44)SE5, RELEASE SOFTWARE (fc1)\n',
 '\n',
 'Switch uptime is 39 minutes\n',
 'System returned to ROM by power-on\n',
 'System image file is "flash:c2960-lanbasek9-mz.150-2.SE4.bin"\n',
 'Last reload reason: Power-on\n',
 '\n',
 '\n',
 '\n',
 'This product contains cryptographic features and is subject to United\n',
 'States and local country laws governing import, export, transfer and\n',
 'use. Delivery of Cisco cryptographic products does not imply\n',
 'third-party authority to import, export, distribute or use encryption.\n',
 'Importers, exporters, distributors and users are responsible for\n',
 'compliance with U.S. and local country laws. Malicious use of this\n',
 'software is a violation of U.S. and international law.\n',
 '\n',
 'Cisco WS-C2960-24TT-L (PowerPC405) processor (revision B0) with 65536K bytes of memory.\n',
 'Processor board ID FOC1432Y101\n',
 'Last reset from power-on\n',
 '1 Virtual Ethernet interface\n',
 '24 FastEthernet interfaces\n',
 '2 Gigabit Ethernet interfaces\n',
 '64K bytes of flash-simulated non-volatile configuration memory.\n',
 'Base ethernet MAC Address       : 00:2A:6A:3B:4C:D0\n',
 'Motherboard assembly number     : 73-9834-08\n',
 'Power supply part number        : 341-0097-02\n',
 'Motherboard serial number       : FOC143105X5\n',
 'Power supply serial number      : LIT14280E1A\n',
 'Model revision number           : B0\n',
 'Motherboard revision number     : A0\n',
 'Model number                    : WS-C2960-24TT-L\n',
 '\n',
 'Configuration register is 0xF\n']
```

**5) File Handle Üzerinde For Loop Kurma:**

Dosyayı satır satır okumak için ara bir liste variable oluşturmadan, doğrudan `open()` ile oluşturulan file handle (`f`) üzerinde döngü kurulabilir ve her satır tek tek yazdırılabilir:

```python
for line in f:
    print(line)

f.close()

...

Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE4, RELEASE SOFTWARE (fc1)

Technical Support: http://cisco.com

Copyright (c) 1986-2013 by Cisco Systems, Inc.

Compiled Wed 26-Jun-13 02:49 by prod_rel_team
...
```

---

### 4.3 Dosyayı Kapatma (`close`)

Bu kullanım şeklinde en önemli kural, dosya ile işlemler tamamlandıktan sonra `close()` çağrısı yapılarak dosyanın mutlaka kapatılmasıdır.

```python
In [15]: f.close()
```

> * *file handle* → açılan bir dosyaya işaret eden ve dosya üzerinde işlemler yapmayı sağlayan object.
> * *current working directory* → komut satırının veya Python interpreter'ın o an çalıştığı mevcut dizin.
> * *read()* → dosya içeriğinin tamamını tek bir string olarak okuyan metot.
> * *readline()* → dosyadan her defasında bir sonraki satırı okuyan metot.
> * *readlines()* → dosyadaki tüm satırları okuyup string elemanlardan oluşan bir list haline getiren metot.
> * *seek(0)* → dosya okuma imlecini dosyanın en başına geri saran metot.
> * *close()* → açılmış dosyayı kapatan ve ayrılan sistem kaynaklarını serbest bırakan metot.

---

## 5. Dosya İşlemleri: Dosyaya Yazma Yapma 

Python'da bir dosyaya veri yazmak için de okuma işlemine benzer şekilde built-in gelen `open()` fonksiyonu kullanılır.

Bu işlemde dosya ismi belirtildikten sonra ikinci parametre olarak açık bir şekilde **`mode="w"`** (write mode) tanımlanır. 
Dosya yolu verilmediğinde yine **current working directory**'de dosya oluşturulur.

---

### 5.1 Dosyaya Yazma ve `.write()` Metodu

Dosyayı yazma modunda açtıktan sonra dönen file handle nesnesi üzerinden **`.write()`** metodu çağrılır:

```python
In [1]: f = open("test_file.txt", "w")

In [2]: f.write("Merhaba...\n")
Out[2]: 11

In [3]: f.write("Merhaba...\n")
Out[3]: 11
```

* `.write()` metodu parametre olarak verilen string'i olduğu gibi dosyaya yazar; satır sonu eklemesi yapmaz. Alt satıra geçilmesi isteniyorsa string'in sonuna açıkça **`\n`** (newline) eklenmelidir.

* Çıktı olarak dönen sayısal değer (`11`), yazılan toplam karakter yani byte sayısını belirtir.

---

### 5.2 Buffer, `.flush()` ve Dosyanın Kapanması

İşletim sistemleri dosya yazma işlemlerinde performans amacıyla veriyi hemen diske yazmak yerine bellekte bir süre **cache** içinde tutabilir.

Kirk Byers'ın videosunda da gösterildiği gibi, iki kez `.write()` çağrılmasına rağmen dosya henüz kapatılmadığında veya bellekte tutulduğunda dosya sisteminde dosyanın boyutu **0 byte** görünebilir:

```bash
[py311_venv] ktbyers@pydev2 ~/learning_python/lesson2/files
$ ls -ltr
total 8
-rw-rw-r-- 1 ktbyers ktbyers 3171 Feb  1 21:15 show_version.txt
-rw-rw-r-- 1 ktbyers ktbyers   35 Feb  1 21:19 simple_file.txt
-rw-rw-r-- 1 ktbyers ktbyers    0 Mar 27 18:09 test_file.txt
```

Veriyi diske zorla yazdırmak için iki yöntem bulunur:

1. **`.flush()` Metodu:** Dosyayı kapatmadan, buffer'da bekleyen verileri doğrudan diske basar.

2. **Dosyayı Kapatmak (`close` veya `exit`):** Dosya kapatıldığında (`f.close()`) ya da Python interpreter oturumu sonlandırıldığında (`exit`), bekleyen buffer otomatik olarak diske aktarılır.

> Kendi ortamımızda IPython'dan çıkış yapıldığında (`exit`), oturum kapanırken dosya nesnesi otomatik kapatıldığı için `.flush()` çağrılmasa dahi 22 byte verinin diske eksiksiz yazıldığı görülür:

```bash
In [1]: f = open("test_file.txt", "w")

In [2]: f.write("Merhaba...\n")
Out[2]: 11

In [3]: f.write("Merhaba...\n")
Out[3]: 11

In [4]: exit

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ ls -la | grep test_file.txt 
-rw-rw-r-- 1 berkay berkay   22 Sep 27 18:02 test_file.txt

# Exit demeden yeni bir terminalde kontrol edersek:

berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ ls -l | grep test.txt 
-rw-rw-r-- 1 berkay berkay    0 Sep 27 18:10 test.txt
```

Manuel olarak `.flush()` çağrıldığında ise oturumu kapatmaya gerek kalmadan veriler anında diske yazılır:

```bash
In [1]: f = open("test_file.txt", "w")

In [2]: f.write("Merhaba...\n")
Out[2]: 11

In [3]: f.write("Merhaba...\n")
Out[3]: 11

In [4]: f.flush()

In [5]: exit

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ ls -la | grep test_file.txt 
-rw-rw-r-- 1 berkay berkay   22 Sep 27 18:04 test_file.txt

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ cat test_file.txt 
Merhaba...
Merhaba...
```

---

### 5.3 Write İşleminin Destructive Doğası 

Dosya işlemlerinde **`mode="w"`** kullanımı kesinlikle **destructive** yani yıkıcı bir işlemdir.

Mevcut ve içinde veri bulunan bir dosya yeniden `mode="w"` ile açıldığında, dosyanın önceki tüm içeriği silinir ve üzerine yeni yazılan içerik kaydedilir:

```python
In [1]: f = open("test_file.txt", "w")

In [2]: f.write("yeni mesaj\n")
Out[2]: 12

In [3]: f.close()
```

Terminalden dosya içeriği kontrol edildiğinde önceki satırların tamamen silindiği ve yalnızca yeni mesajın kaldığı görülür:

```bash
$ cat test_file.txt
yeni mesaj
```

> * *mode="w"* → dosyayı sıfırdan yazma modunda açar; dosya varsa eski içeriğini tamamen silerek açan destructive moddur.
> * *write()* → belirtilen string veriyi dosyaya yazan metot. 
> * *flush()* → bellekte/önbellekte bekleyen tampon verileri dosyayı kapatmadan diske yazmaya zorlayan metot.
> * *destructive* → var olan dosya içeriğinin üzerine yazılarak eski verilerin geri dönüşsüz şekilde kaybolması durumu.

---

## 6. Dosya İşlemleri: Dosyanın Sonuna Veri Ekleme 

Python'da bir dosyaya veri eklemek istediğimizde, önceki derste gördüğümüz destructive `mode="w"` yönteminin aksine **append** modu kullanılır.

Bu işlem için yine built-in gelen `open()` fonksiyonu kullanılır; ancak bu kez mod parametresi olarak **`mode="a"`** (append mode) belirtilir. 
Dosya yolu girilmediğinde dosya yine **current working directory'de** aranır veya yoksa oluşturulur.

---

### 6.1 Dosyayı Append Modunda Açma ve Yazma

Dosya `mode="a"` ile açıldığında, dosyanın önceki içeriği kesinlikle silinmez. Yazılan yeni veriler doğrudan dosyanın en sonuna eklenir:

**1) İlk olarak dosyanın `mode="w"` ile oluşturulup ilk satırın yazılması:**

```python
In [1]: f = open("test_file.txt", "w")

In [2]: f.write("Merhaba!\n")
Out[2]: 9

In [3]: f.flush()

In [4]: f.close()

In [5]: exit
```

Terminalden kontrol ettiğimizde dosyanın ilk hali görülür:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ cat test_file.txt 
Merhaba!
```

**2) Dosyanın `mode="a"` ile açılıp yeni satırın eklenmesi:**

```python
In [1]: f = open("test_file.txt", "a")

In [2]: f.write("Tekrar merhaba!\n")
Out[2]: 16

In [3]: f.flush()

In [4]: f.close()

In [5]: exit
```

Terminalden dosya içeriği yeniden kontrol edildiğinde eski satırın korunduğu ve yeni metnin dosyanın sonuna eklendiği görülür:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-2$ cat test_file.txt 
Merhaba!
Tekrar merhaba!
```

---

### 6.2 Dosya Yazma İşlemlerinde En İyi Yaklaşımlar 

Kirk Byers dosyalara veri yazarken genel olarak iki ana yöntemi öneriyor:

1. **Destructive Yazma (`mode="w"`):** Yazılacak tüm verileri önceden hazırlayıp tek seferde dosyanın üzerine yazmak (mevcut içeriği tamamen silerek yeni veriyi kaydetmek).

2. **Sonuna Ekleme (`mode="a"`):** Var olan dosyanın içeriğini bozmadan sadece sonuna yeni satırlar/metinler eklemek.

Kirk Byers bir dosyanın **ortasına** doğrudan string eklemeye veya güncellemeler yapmaya çalışılmaması gerektiğine dikkat çekiyor. 
Eğer dosya içinde arama yapıp aradaki verileri sürekli güncellemeniz gereken durumlar ortaya çıkıyorsa, düz metin dosyaları yerine **database** — özellikle dosya tabanlı basit bir çözüm olan **SQLite / SQLite3** — kullanmanın çok daha doğru bir çözüm olacağını belirtiyor.

> * *mode="a"* → dosyayı append modunda açar; dosyanın mevcut içeriğini silmeden yeni verileri dosyanın sonuna ekler.
> * *append* → var olan bir dosya veya listenin sonuna yeni veri iliştirme işlemi.
> * *SQLite / SQLite3* → dosya içerisinde arama ve orta kısımlarda güncelleme gerektiren karmaşık senaryolarda dosya yerine tercih edilmesi önerilen hafif ve dosya tabanlı veritabanı.

---

## 7. Python Kod Blokları ve Indentation Yapısı 

Kursun bir sonraki adımında dosya işlemlerini daha güvenli ve standart hale getiren **context manager** yani `with` yapısına geçeceğiz. 
Ancak `with` ifadesi, Python'da ilk defa bir **indented block** ile karşılaşacağımız yerdir.

Kirk Byers, context manager konusunun detaylarına girmeden önce Python'daki kod bloklarının çalışma mantığını ve syntax kurallarını bu kısa bölümde ayrıntılandırıyor.

---

### 7.1 İki Nokta ve Girintileme

Python'da bir kod bloğunun başladığını belirten işaret satırın en sonundaki **iki nokta üst üste (`:`)** karakteridir; buna **colon terminator** denir.

Context manager syntax'ı üzerinden incelersek:

```python
with open("show_version.txt", mode="r") as f:
    data = f.read()
```

* **`with` ve `as f`:** Context manager yapısını kuran anahtar kelimelerdir; dosya nesnesi `as f` ile bir file handle değişkenine atanır.
  
* **Colon Terminator (`:`):** Satır sonundaki `:` karakteri, Python'a hemen ardından girintili bir kod bloğunun geleceğini bildirir.

* **Dört Boşluk:** Bloğun içindeki satırlar mutlaka **4 boşluk** girinti ile yazılmalıdır; tab tuşu kullanılmamalıdır.

* **Blok Kapsamı:** Bu bloğun içine tek bir satır yazılabileceği gibi onlarca hatta yüzlerce satır kod da yazılabilir. Aynı blok seviyesindeki tüm satırlar aynı 4 boşluk hizasını korumalıdır.

---

### 7.2 İç İçe Bloklar ve Bloğun Sona Ermesi

Python'da kod blokları birbirinin içerisine istenilen derinlikte yerleştirilebilir buna **nested** bloklar deniliyor.

Bir bloğun bittiğini göstermek için özel bir kapanış karakteri (örneğin süslü parantez `}`) kullanılmaz. 
Sadece satır başındaki indentation'ı bir önceki seviyeye çekmek veya tamamen sıfırlamak bloğun sonlandığını belirtmek için yeterlidir.

Kirk Byers'ın IPython üzerinde gösterdiği iç içe blok örneği:

```python
In [1]: if True:
   ...:     print("Hello")
   ...:     print("Something")
   ...:     for x in range(10):
   ...:         print(x)
   ...:         print(x)
   ...:     print("Else")
   ...: print("something else")
```

Bu yapı adım adım şöyle işler:

1. **`if True:`** satırının sonundaki `:` karakteri ilk bloğun başladığını gösterir.
2. Altındaki `print("Hello")` ve `print("Something")` satırları **4 boşluk** içeridedir.
3. Ardından gelen **`for x in range(10):`** loop kendi sonundaki `:` karakteri ile yeni bir **nested** blok başlatır.
4. Bu **nested** bloğun satırları olan `print(x)` komutları bir 4 boşluk daha içeriye girerek toplam **8 boşluk** seviyesine geçer.
5. Döngü bittiğinde indentation tekrar bir kademe geri çekilerek 4 boşluk seviyesindeki `print("Else")` satırına dönülür (bu satır hâlâ `if` bloğunun içindedir).
6. En altta indentation'ın tamamen sıfırlandığı `print("something else")` satırına gelindiğinde ise artık ana programa dönülmüş olur ve `if` bloğu tamamen sona erer.

> Bu aşamada `if` koşullarının veya `for` döngülerinin mekaniğine odaklanmaya gerek yoktur; buradaki temel amaç iki nokta (`:`) karakterinin yeni bir blok başlattığını ve girintinin geri çekilmesinin o bloğu kapattığını görmektir.

> * *colon terminator (`:`)* → Python'da indentation bir kod bloğunun başlayacağını belirten iki nokta üst üste karakteri.
> * *indented block* → iki nokta karakterinden sonra 4 space boşluk bırakılarak yazılan ve ilgili yapıya ait olan kod satırları.
> * *nested blocks* → blokların birbiri içerisine hiyerarşik olarak yerleştirilmesi.

---

## 8. Python Context Managers ve `with` Statement

Python'da belirli bir kaynağı açmak, üzerinde işlem yapmak ve ardından bu kaynağı kapatmak çok yaygın bir operasyon desenidir. 
Dosya işlemleri de doğrudan bu kalıba uyar: Dosya açılır (`open`), üzerinde okuma/yazma/ekleme yapılır ve iş bitince dosya kapatılır (`close`).

Bu desen sadece dosyalarda değil; veritabanı bağlantılarında (bağlantı açma, sorgu çalıştırma, bağlantıyı kapatma), API oturumlarında (authenticate olma, işlemleri yapma, bağlantıyı kapatma) ve ağ cihazlarına bağlanırken de birebir karşımıza çıkar.

Python, bu süreci güvenli ve otomatik yönetmek için **context manager** adı verilen özel bir yapı sunar; bu yapının anahtar kelimesi **`with`** statement'tır.

---

### 8.1 `with` Statement Syntax'ı ve Otomatik Kapanma

Önceki bölümlerde gördüğümüz `f = open(...)` ve manuel `f.close()` yapısı yerine context manager şu şekilde kurulur:

```python
with open("show_version.txt", mode="r") as f:
    data = f.read()
```

* **`with open(...)`:** Dosyayı açar; buradaki `mode="r"` opsiyoneldir, belirtilmezse default olarak read modunda açılır.
* **`as f`:** Açılan dosyaya işaret eden file handle değişkeni satırın sonuna eklenir.
* **Colon Terminator (`:`):** Satır sonundaki iki nokta üst üste karakteri, ardından bir indented block geleceğini bildirir.
* **Otomatik Kapanma ve Flush:** 4 boşluk girintili bloğun içerisindeki işlemler tamamlanıp girintili blok bittiğinde, Python **dosyayı otomatik olarak kapatır**. Dosya kapatıldığı için otomatik olarak bir **flush** işlemi de tetiklenir; yani `mode="w"` veya `mode="a"` kullanılırken yazılan tüm veriler diske basılmış olur.

Kendi ortamımızda çalıştırma:

```python
In [1]: with open("show_version.txt", mode="r") as f:
   ...:     data = f.read()
   ...:     print(data)
   ...: 
Switch> show version
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE4, RELEASE SOFTWARE (fc1)
Technical Support: http://cisco.com
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Wed 26-Jun-13 02:49 by prod_rel_team
...
Configuration register is 0xF
```

---

### 8.2 Hata - Exception Durumunda Kaynak Temizliği

Context manager kullanmanın en kritik avantajı beklenmedik bir **exception** durumunda ortaya çıkar.

Eski yöntemde (`open` yapıp ardından kod çalıştırırken) aradaki bir işlem programı crash ederse veya beklenmedik bir hata fırlatılırsa, alttaki `f.close()` satırına hiçbir zaman ulaşılamaz; dosya, veritabanı veya network bağlantısı sistem üzerinde açık kalır.

Context manager ise blok içerisinde ölümcül bir hata meydana gelse dahi, arka planda **cleanup** yani kaynak temizliği işleminin daima çalışmasını garanti eder. 
Hata çıksa bile dosya güvenle kapatılır ve flush işlemi gerçekleştirilir.

Kirk Byers'ın ve kendi terminalimizin gösterdiği test:

```python
In [3]: with open("show_version.txt", mode="r") as f:
   ...:     print(no_var)
   ...: 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 2
      1 with open("show_version.txt", mode="r") as f:
----> 2     print(no_var)

NameError: name 'no_var' is not defined
```

Tanımlanmamış bir variable ekrana yazdırılmaya çalışıldığında Python bir `NameError` exception'ı üretir ve blok çöker.

Ancak bu çökmeden hemen sonra file handle üzerinden okuma yapmaya çalıştığımızda dosyanın arka planda başarıyla kapatıldığını doğrularız:

```python
In [4]: f.read()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[4], line 1
----> 1 f.read()

ValueError: I/O operation on closed file.
```

Hatanın bildirdiği `I/O operation on closed file` mesajı, `with` bloğunun crash anında dahi devreye girip dosyayı kapattığını gösterir.

> * *context manager* → kaynakların açılması, kullanılması ve işlem bitiminde (veya hata anında) güvenle serbest bırakılmasını otomatikleştiren yapı.
> * *with statement* → Python'da context manager protokolünü çağıran anahtar ifade.
> * *exception* → programın çalışma esnasında karşılaştığı ve akışı kesen beklenmedik hata durumu.
> * *gracefully cleanup* → hata çıksa dahi açık kalan kaynakların (dosya, soket, veritabanı) arka planda düzgünce kapatılması.

---

## 9. List Basics

Şimdiye kadar Python'da sayılar (integers ve floats), strings, booleans ve özel `None` veri tipi gibi temel veri yapıları ele alındı.

Listeler ise Python'da daha karmaşık veri yapılarına attığımız ilk adımdır. 
Listeler, kendi içinde doğal bir sıralaması olan elemanlar topluluğudur; yani birinci eleman, ikinci eleman, üçüncü eleman şeklinde listenin sonuna kadar uzanan sıralı bir yapı barındırırlar. 
Diğer programlama dillerinde bu yapılar genellikle **arrays** olarak adlandırılır.

---

### 9.1 Liste Tanımlama ve Farklı Veri Tipleri

Python'da liste oluşturmak için **köşeli parantez `[]**` kullanılır. Liste içindeki elemanlar birbirinden virgül (`,`) ile ayrılır ve liste kapatma köşeli parantezi ile sonlandırılır.

Python listelerinin en önemli özelliklerinden biri, **içerisinde yer alan elemanların veri tiplerinin aynı olma zorunluluğunun bulunmamasıdır**. 
Bir listenin içine aynı anda string, integer, float, boolean, `None` ve hatta başka bir boş ya da dolu listeyi gömebilirsiniz.

Kendi ortamımızda çalıştırma:

```python
In [1]: my_list = ["berkay", 1, "network", [], None, 1.9]

In [2]: type(my_list)
Out[2]: list

In [3]: my_list
Out[3]: ['berkay', 1, 'network', [], None, 1.9]
```

Built-in `type()` fonksiyonu ile kontrol edildiğinde nesnenin tipinin `list` olduğu görülür.

---

### 9.2 Zero-Based İndeksleme 

Listeler sequential yani sıralı yapılardır ve elemanlarına erişmek için **sıfır tabanlı indeksleme** kullanılır:

* Listenin en başındaki ilk elemana ulaşmak için `0` indeksi kullanılır (`my_list[0]`).
* İkinci eleman için `1`, üçüncü eleman için `2`, dördüncü eleman için `3` şeklinde sırayla devam edilir.

```python
In [4]: my_list[0]
Out[4]: 'berkay'
```

---

### 9.3 Liste Elemanlarını Güncelleme

Listeler doğrudan güncellenebilir yapılardır. Bir indeks numarası belirtilip karşısına yeni bir değer assign edildiğinde, o indeksteki eski veri silinir ve yerine yeni değer geçer:

```python
In [5]: my_list[2] = "NetworkRose"

In [6]: my_list
Out[6]: ['berkay', 1, 'NetworkRose', [], None, 1.9]
```

Bu güncelleme sırasında veri tipini korumak zorunda değilsiniz. Örneğin daha önce string olan bir elemanın yerine bir integer ya da başka bir veri tipi atayabilirsiniz; Python buna izin verir.

---

### 9.4 Negatif İndeksler ile Sondan Erişme

Listenin sonundaki elemanlara ulaşmak istediğimizde negatif sayılar kullanılır.

Negatif indeksleme listenin en sonundan geriye doğru çalışır:

* **`-1` İndeksi:** Listenin en sonundaki son elemanı verir (`my_list[-1]`).
* **`-2` İndeksi:** Sondan bir önceki elemanı verir.
* **`-3`, `-4`:** Listenin sonundan başına doğru geriye doğru sayarak erişim sağlar.

```python
In [7]: my_list[-1]
Out[7]: 1.9
```

> * *list* → farklı veri tiplerini bir arada tutabilen, sıralı ve değiştirilebilir koleksiyon veri yapısı. 
> * *array* → diğer programlama dillerinde listelere karşılık gelen dizi yapısı.
> * *zero-based index* → eleman sayımının ve konum erişiminin sıfırdan başladığı indeksleme sistemi.
> * *negative index* → bir listenin son elemanından (`-1`) başlayarak geriye doğru elemanlara erişmeyi sağlayan indeksleme yöntemi.

---

## 10. Lists: Len, Range ve Membership

Bu bölümde listelerin diğer pratik özellikleri olan eleman sayısı kontrolü, dinamik liste üretimi ve liste içi eleman sorgulama mekanizmaları incelenmektedir.

---

### 10.1 `len()` ile Liste Uzunluğunu Bulma

Bir listenin kaç tane eleman barındırdığını öğrenmek için built-in gelen **`len()`** fonksiyonu kullanılır. 
Fonksiyona parametre olarak liste verildiğinde, geriye listedeki toplam eleman sayısını belirten bir integer değer döner.

Kendi ortamımızda çalıştırma:

```python
In [1]: my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]

In [2]: my_list
Out[2]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True]

In [3]: len(my_list)
Out[3]: 9
```

---

### 10.2 `range()` Built-in Fonksiyonu ve İndeks İlişkisi

Python'da **`range()`** fonksiyonu, dinamik olarak sayı dizileri üretmek ve özellikle listelerle birlikte çalışmak için oldukça kullanışlı bir built-in fonksiyondur.

`range()` tek bir argüman ile çağrıldığında default olarak `0` değerinden başlar ve belirtilen sayının bir eksiğine (`n-1`) kadar gider. 
Üretilen bu sayı dizisini doğrudan görebilmek için sonuç `list()` fonksiyonu ile cast edilir:

```python
In [4]: list(range(10))
Out[4]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**İndekslerle Birebir Örtüşme Mantığı:**

`range(10)` fonksiyonunun ürettiği `0, 1, 2, 3, 4, 5, 6, 7, 8, 9` sayıları, tam olarak 10 elemanlı bir listenin indeks numaralarına karşılık gelir.
Aynı şekilde 7 elemanlı bir liste için `range(7)` çağrıldığında `0`'dan `6`'ya kadar olan sayılar elde edilir; bu da o listenin sıfırdan yedinci elemana kadar olan tüm indekslerini birebir temsil eder.

**Başlangıç Değerini Değiştirme:**

`range()` fonksiyonuna iki argüman verilerek başlangıç değeri değiştirilebilir.
İlk argüman başlangıç değerini, ikinci argüman ise bitiş sınırını belirler; ancak bitiş sınırındaki sayı sonuca dahil edilmez:

```python
In [5]: list(range(5, 10))
Out[5]: [5, 6, 7, 8, 9]
```

---

### 10.3 List Membership Kontrolü (`in`)

Bir elemanın liste içerisinde var olup olmadığını denetlemek için **`in`** anahtar kelimesi ile **membership check** yapılır.

Sorgulanan elemanın adı yazılır, ardından `in` anahtar kelimesi ve liste adı belirtilir. Bu işlem sonucunda geriye bir **boolean** (`True` ya da `False`) döner:

```python
In [6]: "network" in my_list
Out[6]: True

In [7]: "test123" in my_list
Out[7]: False
```

**Duplicate Elements:**

Listeler aynı elemandan birden fazla barındırabilir buna duplicate elements deniliyor. `in` operatörü aranan elemanın listede kaç defa geçtiğini saymaz; yalnızca o elemanın listenin herhangi bir yerinde bulunup bulunmadığını kontrol ederek `True` veya `False` yanıtını verir.

> * *len()* → bir veri koleksiyonunun barındırdığı toplam eleman sayısını döndüren built-in fonksiyon.
> * *range()* → sıfırdan veya belirlenen bir başlangıç değerinden başlayarak bitiş değerinin bir eksiğine kadar ardışık sayı dizisi üreten fonksiyon.
> * *casting* → bir veri tipinin başka bir tipe (örneğin range nesnesinin listeye) açıkça dönüştürülmesi.
> * *membership check (`in`)* → bir elemanın liste içerisinde yer alıp almadığını denetleyen ve geriye boolean sonuç döndüren kontrol işlemi.
> * *duplicate elements* → bir liste içinde aynı değere sahip birden fazla elemanın bulunması durumu.

---

## 11. List Methods

Python'da listeler üzerinde işlem yapabilmemiz için birçok yerleşik metot bulunur. 
Bu bölümde en sık kullanılan temel liste metotları, listelerin bellekteki davranışları ve birleştirme yöntemleri ele alınmaktadır.

---

### 11.1 `.append()` Metodu ve Mutable Yapı

Muhtemelen en yaygın kullanılan liste metodu **`.append()`** metodudur. Bir listenin sonuna tek bir yeni eleman eklemek için kullanılır.

```python
In [1]: my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]

In [2]: my_list
Out[2]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True]

In [3]: my_list.append("yeni eleman")

In [4]: my_list
Out[4]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True, 'yeni eleman']
```

> **Önemli Kural:** `.append()` metodu geriye yeni bir liste döndürmez; doğrudan mevcut listeyi modifiye eder. Bu durum listelerin **mutable** yani değiştirilebilir bir veri tipi olmasından kaynaklanır. Kursun ilerleyen bölümlerinde detaylandırılacak olan mutable/immutable ayrımının temel mantığı buraya dayanır: Listeler bellekteki yerinde doğrudan güncellenebilir.

---

### 11.2 `.clear()` ve `.count()` Metotları

Daha seyrek kullanılan iki yardımcı metot:

* **`.clear()`:** Liste içindeki tüm elemanları temizleyerek boş bir liste (`[]`) haline getirir. Kirk Byers boş bir liste elde etmek için `clear()` yerine listeyi doğrudan boş listeye yeniden assign etmenin (`my_list = []`) daha yaygın ve daha anlaşılır bir pratik olduğunu belirtiyor.

```python
In [5]: my_list.clear()

In [6]: my_list
Out[6]: []
```

* **`.count()`:** Belirli bir elemanın liste içerisinde kaç defa geçtiğini sayar.

```python
In [7]: my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]

In [9]: my_list.count("network")
Out[9]: 1
```

---

### 11.3 `.copy()` Metodu ve Bellek Adresleri 

Python'da bir listeyi başka bir değişkene kopyalamak istediğimizde sadece `new_list = my_list` yazarsak yeni bir liste oluşmaz. 
Bu işlem yalnızca bellekteki aynı listeye işaret eden ikinci bir isim yani referans tanımlar. Birinde yapılacak değişiklik diğerini de bozar.

Bağımsız bir kopya üretmek için **`.copy()`** metodu kullanılır:

```python
In [11]: new_list = my_list.copy()

In [12]: new_list
Out[12]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True]
```

Bu kopyalama işleminin bellekte farklı bir nesne oluşturup oluşturmadığını doğrulamak için Python'un built-in **`id()`** fonksiyonu kullanılır:

```python
In [13]: id(my_list)
Out[13]: 140422702361792

In [14]: id(new_list)
Out[14]: 140422702443200
```

`id()` çıktılarının farklı olması, `new_list`'in bellekte ayrı bir alanda tutulduğunu kanıtlar. Böylece `my_list` üzerinde yapılacak bir değişiklik `new_list`'i etkilemez.

> Bu kopyalama yöntemi bir **shallow copy** işlemidir. Nested listeler barındıran daha karmaşık yapılarda shallow copy ile deep copy farkı mutable/immutable tartışmasında detaylandırılacaktır.

---

### 11.4 List Concatenation ve `.extend()` Metodu

Stringlerde olduğu gibi listelerde de artı (**`+`**) operatörü ile **list concatenation** yapılabilir:

```python
In [15]: "network" + "rose"
Out[15]: 'networkrose'

In [16]: "network" + " rose"
Out[16]: 'network rose'

In [18]: my_list + [10, "string"]
Out[18]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True, 10, 'string']
```

> `+` operatörü orijinal `my_list` değişkenini değiştirmez; iki listenin birleşiminden yeni bir liste üretir. Bu sonucu korumak için yeni bir değişkene atamak veya mevcut listeye yeniden assign etmek gerekir.

**`.extend()` Metodu:**

Birleştirme işlemini listeyi yerinde değiştirerek yapmak istediğimizde **`.extend()`** metodu kullanılır.

Metot parametre olarak tek bir veri koleksiyonu örneğin bir liste bekler:

```python
In [19]: my_list.extend('test', 54)
TypeError: list.extend() takes exactly one argument (2 given)
```

Elemanlar liste içerisinde `['test', 54]` şeklinde tek bir argüman olarak verildiğinde, listenin sonuna her iki eleman da ayrı ayrı eklenir:

```python
In [20]: my_list.extend(['test', 54])

In [21]: my_list
Out[21]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True, 'test', 54]
```
---

### 11.5 `.pop()` Metodu

Append metodundan sonra muhtemelen en çok kullanılan ikinci liste metodu **`.pop()`** metodudur.

`pop()` metodu iki işi aynı anda yapar: Belirtilen indeksteki elemanı listeden tamamen çıkarır ve çıkarılan bu değeri geri döndürür. Dönen bu değer doğrudan bir değişkene atanabilir.

**1) Listenin Sonundan Eleman Çıkarma:**

Parantez içine hiçbir parametre verilmediğinde listenin en sonundaki elemanı çıkarır ve teslim eder:

```python
In [22]: val1 = my_list.pop()

In [23]: val1
Out[23]: 54

In [24]: my_list
Out[24]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True, 'test']
```

**2) Listenin Başından Eleman Çıkarma (`pop(0)`):**

Parantez içine `0` indeksi verildiğinde listenin ilk elemanını çıkarıp teslim eder:

```python
In [25]: val2 = my_list.pop(0)

In [26]: val2
Out[26]: 'berkay'

In [27]: my_list
Out[27]: [1, 'network', [], None, 1.9, [1, 2, 3], 'test', True, 'test']
```

> Kirk Byers'ın pratik tavsiyesi: `pop()` işlemini yalnızca **listenin en sonundan** veya **en başından** yapın; listenin ortasındaki rastgele yerlerden pop yapmaktan kaçının.

---

### 11.6 Diğer Liste Metotları

Python'da listeler üzerinde kullanılabilecek diğer hazır metotlar şunlardır:

* **`.sort()`:** Listenin elemanlarını kendi içinde sıralar.
* **`.reverse()`:** Listenin eleman sıralamasını tersine çevirir.
* **`.insert()`:** Listenin belirlenen bir indeksine araya eleman sokar.
* **`.remove()`:** Belirtilen değere sahip ilk elemanı listeden siler.
* **`.index()`:** Belirtilen bir değerin listedeki indeks numarasını bulur.

> * *append()* → listenin sonuna tek bir eleman ekleyen ve listeyi doğrudan modifiye eden metot. 
> * *mutable* → tanımlandıktan sonra bellekteki içeriği doğrudan değiştirilebilen veri tipi özelliği.
> * *shallow copy* → listenin bellekte yeni bir kopyasını oluşturan ancak nested yani iç içe referansları kopyalamayan yüzeysel kopyalama.
> * *id()* → bir nesnenin bellekteki benzersiz kimlik/adres numarasını döndüren built-in fonksiyon.
> * *extend()* → parametre olarak verilen listenin elemanlarını mevcut listenin sonuna ekleyerek listeyi yerinde genişleten metot.
> * *pop()* → listenin sonundan veya belirtilen indeksinden elemanı silip geriye o değeri döndüren metot.

---

## 12. List Slices

Python'da **list slices**, var olan bir listeden dinamik olarak parçalar çıkarıp yeni listeler üretmenin yoludur.

Tek bir indeks numarası belirtilerek yapılan eleman erişiminin aksine, slicing işleminde genellikle iki sayı belirtilir. 
Bu iki sayı yeni listenin başlangıç ve bitiş sınırlarını tanımlar.

---

### 12.1 Başlangıç ve Bitiş İndeksi Mantığı

Slicing işleminde iki indeks arasına iki nokta üst üste (`:`) konulur:

* **İlk Sayı (Başlangıç):** Dilimlemenin başlayacağı indeksi belirtir ve **sonuca dahil edilir** yani included.

* **İkinci Sayı (Bitiş):** Dilimlemenin biteceği indeksi belirtir ancak **sonuçtan hariç tutulur** yani excluded.

Bu kural nedeniyle slice, belirtilen bitiş indeksinin bir eksiğine (`n-1`) kadar gider. 
Kirk Byers bu davranışın arka plandaki matematiksel hesaplamaları kolaylaştırmak amacıyla bu şekilde tasarlandığını belirtiyor.

Kendi ortamımızda çalıştırma:

```python
In [1]: my_list = ["berkay", 1, "network", [], None, 1.9, [1, 2, 3], "test", True]

In [2]: my_list[1:3]
Out[2]: [1, 'network']

In [3]: my_list[2:4]
Out[3]: ['network', []]
```

> `my_list[1:3]` ifadesi `1` indeksindeki elemanı dahil eder, `3` indeksini hariç tutar; geriye `1` ve `2` indekslerindeki elemanları döndürür.

---

### 12.2 Başlangıç veya Bitiş İndeksini Boş Bırakma

Dilimleme yaparken sınır değerlerinden biri veya her ikisi birden boş bırakılabilir:

**1) Başlangıç İndeksinin Boş Bırakılması (`[:n]`):**

İlk sayı belirtilmediğinde dilimleme listenin en başından başlar. Sıfırıncı indeksten başlayarak belirtilen bitiş indeksinin bir eksiğine kadar gider:

```python
In [4]: my_list[:3]
Out[4]: ['berkay', 1, 'network']
```

**2) Bitiş İndeksinin Boş Bırakılması (`[n:]`):**

İkinci sayı belirtilmediğinde dilimleme verilen başlangıç indeksinden listenin en sonuna kadar gider; son eleman da dahil edilir:

```python
In [5]: my_list[4:]
Out[5]: [None, 1.9, [1, 2, 3], 'test', True]
```

**3) İki İndeksin de Boş Bırakılması (`[:]`):**

Başlangıç ve bitiş indeksleri yazılmayıp yalnızca iki nokta kullanıldığında, listenin tamamı baştan sona kopyalanır.

Bu işlem, önceki bölümde gördüğümüz `.copy()` metodu gibi bir **shallow copy** üretir:

```python
In [6]: my_list[:]
Out[6]: ['berkay', 1, 'network', [], None, 1.9, [1, 2, 3], 'test', True]
```

---

### 12.3 Negatif İndeksler ile Dilimleme

Slicing işlemlerinde negatif indeks numaraları da kullanılabilir:

```python
In [7]: my_list[4:-1]
Out[7]: [None, 1.9, [1, 2, 3], 'test']

In [8]: my_list[4:-2]
Out[8]: [None, 1.9, [1, 2, 3]]
```

Negatif sayılarda da ikinci sayının hariç tutulması kuralı geçerlidir. `my_list[4:-1]` ifadesinde dilim `4` indeksinden başlar; `-1` listenin en son elemanına karşılık gelse de bitiş indeksi olduğu için hariç tutulur ve son eleman sonuca dahil edilmez.

---

### 12.4 Orijinal Listenin Korunması

List slicing işlemi **orijinal listeyi kesinlikle modifiye etmez**.

Orijinal `my_list` değişkeni bellekte hiçbir değişikliğe uğramadan ilk haliyle kalır. 
Slicing sonucunda dinamik olarak üretilen bu yeni listeyi ileride kullanmak istiyorsak, bunu yeni bir variable'a assign etmemiz gerekir.

> * *list slice* → mevcut bir listeden indeks aralıkları kullanılarak dinamik olarak yeni alt listeler türetme işlemi. 
> * *included* → dilimlemenin başladığı ilk indeksin sonuca dahil edilmesi kuralı.
> * *excluded* → dilimlemenin bittiği ikinci indeksin sonuç listesine dahil edilmemesi kuralı.
> * *[:] (slice copy)* → başlangıç ve bitiş belirtilmeden tüm listeyi shallow copy yöntemiyle kopyalama syntaxı.

---

## 13. Multidimensional Lists

Python'da bir listenin elemanları başka listelerden oluşabilir; bu yapılara **multidimensional lists** yani çok boyutlu listeler denir.
Nested tanımlanan bu listelerde elemanlara erişirken zero-based indeksleme mantığı aynı şekilde geçerliliğini korur.

---

### 13.1 Çok Boyutlu Liste Tanımlama ve Dış Elemanlara Erişim

Bir listenin içerisine eleman olarak yeni listeler yerleştirildiğinde, en dıştaki liste kapsayıcı olarak çalışır.

Kendi ortamımızda iki adet alt liste barındıran bir liste tanımlama:

```python
In [1]: my_list = [[1, 2, 3], ["a", "b", "c"]]
```

Burada `my_list` iki ana elemandan oluşur. En dıştaki listeden bu alt listelere ulaşmak için standart indeksler kullanılır:

* **`my_list[0]`:** Listenin sıfırıncı indeksindeki ilk alt listeyi (`[1, 2, 3]`) döndürür.
* **`my_list[1]`:** Birinci indeksindeki ikinci alt listeyi (`["a", "b", "c"]`) döndürür.

```python
In [2]: my_list[0]
Out[2]: [1, 2, 3]

In [3]: my_list[1]
Out[3]: ['a', 'b', 'c']
```

---

### 13.2 Chain Indices ile İç Elemanlara Ulaşma

Dönen değerin kendisi de bir liste olduğu için, içerideki spesifik bir elemana ulaşmak amacıyla indeksler soldan sağa doğru **zincirleme** şeklinde ardı ardına eklenir:

1. **İlk İndeks:** En dıştaki listeden hangi alt listenin seçileceğini belirler - outermost list.

2. **İkinci İndeks:** Seçilen o iç listenin içerisindeki hangi elemana ulaşılacağını belirler - inner list.

Birinci alt listenin (`[1, 2, 3]`) elemanlarına erişim:

```python
In [5]: my_list[0][0]
Out[5]: 1

In [7]: my_list[0][1]
Out[7]: 2

In [8]: my_list[0][2]
Out[8]: 3
```

İkinci alt listenin (`["a", "b", "c"]`) elemanlarına erişim:

```python
In [4]: my_list[1][0]
Out[4]: 'a'

In [9]: my_list[1][1]
Out[9]: 'b'

In [10]: my_list[1][2]
Out[11]: 'c'
```

---

### 13.3 Alt Listeyi Yeni Bir Değişkene Atama

Zincirleme indeks yazmak yerine, istenirse içteki alt liste bağımsız bir değişkene atanabilir ve ardından o değişken üzerinden doğrudan tek indeksle işlem yapılabilir:

```python
In [10]: str_list = my_list[1]

In [11]: str_list
Out[11]: ['a', 'b', 'c']

In [12]: str_list[1]
Out[12]: 'b'
```

Bu yöntemle önce `my_list[1]` alt listesi `str_list` adında bir değişkene referans olarak atanır, ardından `str_list[1]` denilerek doğrudan `'b'` elemanına erişilir.

> * *multidimensional list* → elemanları başka listelerden oluşan nested liste yapısı.
> * *chain indices* → çok boyutlu yapılarda derinlik seviyelerine göre indeksleri köşeli parantezlerle yan yana (`my_list[0][1]`) bağlama yöntemi.
> * *outermost list* → tüm alt elemanları ve diğer listeleri kapsayan en dıştaki ana liste.
> * *inner list* → ana listenin bir elemanı olarak içeride yer alan alt liste.

---
