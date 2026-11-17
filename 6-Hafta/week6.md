## 1. Giriş: Table of Contents

Lesson 6 kapsamında Python'da modüler programlamanın temel taşı olan **Functions** ve tek satırlık anonim fonksiyon yapıları olan **Lambda Expressions** konuları ele alınmaktadır.

Kirk Byers bu derste sırasıyla aşağıdaki konuları işleyeceğini belirtmektedir:

* **Functions:** Fonksiyonların tanımlanması, parametre aktarımı, değişken kapsamları ve yeniden kullanılabilir kod blokları inşa etme ilkeleri.
* **Lambda Expressions:** Kısa ve isimsiz fonksiyon ifadelerinin yazım kuralları ve kullanım alanları.

> * *function* → bir kez yazılıp programın farklı noktalarında defalarca çağrılabilen yeniden kullanılabilir kod bloğu. 
> * *def keyword* → Python'da yeni bir fonksiyon tanımlamasını başlatan anahtar kelime.
> * *parameters* → fonksiyon tanımında parantez içine yazılan ve sadece fonksiyon içinde geçerli olan local değişkenler.
> * *return statement* → fonksiyonun ürettiği sonucu çağrıldığı noktaya geri döndüren ifade.

---

## 2. Function Basics: Temel Kavramlar ve Syntax

Kirk Byers, programlamanın sunduğu iki büyük güce dikkat çekerek fonksiyonların neden vazgeçilmez olduğunu açıklamaktadır:

---

### 2.1 Neden Fonksiyon Kullanırız? Kodun Yeniden Kullanılabilirliği

Programlama öğrenirken ilk kazanılan yetenek, manuel olarak yapılan bir görevi kod yazarak otomatikleştirmektir. 
Ancak asıl büyük güç, çözülen bu problemleri farklı senaryolarda da kullanılabilecek **yeniden kullanılabilir yapı taşlarına** dönüştürebilmektir.

* **Bir Kez Yaz, Defalarca Kullan:** Aynı mantığı farklı veriler üzerinde çalıştırmak için kodu kopyalayıp yapıştırmak yerine, o mantığı bir fonksiyon içine hapsedip ihtiyaç duyulan her yerde çağırırız.

* **Araç Kutusu Yaklaşımı:** Oluşturulan her fonksiyon zamanla büyüyen bir kod araç kutusuna dönüşür ve yeni problemleri çözme süresini ciddi oranda kısaltır.

---

### 2.2 Fonksiyon Tanımlama Syntax'ı ve Bileşenleri

Python'da bir fonksiyon oluşturmak ve çalıştırmak için izlenen yapı şu bileşenlerden oluşur:

1. **`def` Anahtar Kelimesi:** Fonksiyon tanımlamasının başladığını belirtir.
   
2. **Fonksiyon Adı:** `def` kelimesinden sonra gelen ve fonksiyonu çağırırken kullanacağımız isimdir.

3. **Parametreler:** Fonksiyon adının yanındaki parantezler içinde tanımlanır. Bu parametreler yalnızca fonksiyonun kendi kapsamı içinde var olan **local değişkenlerdir**. Fonksiyon dışında aynı isimde değişkenler olsa bile birbirlerinden tamamen bağımsızdırlar.

4. **Indented Blok:** İki nokta üst üste `:` işaretinden sonra girintili olarak yazılan ve fonksiyon çağrıldığında çalıştırılacak olan asıl işlemlerdir.

5. **`return` İfadesi:** Fonksiyonun ürettiği değeri dışarıya aktarır. Eğer fonksiyon içinde açıkça bir `return` yazılmazsa, Python varsayılan olarak **`None`** değerini döndürür.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [1]: def toplama_function(arg1, arg2, arg3=None):
   ...:     print("Bu bir fonksiyon.")
   ...:     print(f"arg1 değeri --> {arg1}")
   ...:     print(f"arg2 değeri --> {arg2}")
   ...:     return arg1 + arg2
   ...: 

In [2]: toplama_function(10, 20)
Bu bir fonksiyon.
arg1 değeri --> 10
arg2 değeri --> 20
Out[2]: 30
```

* **Tanımlama vs. Çağırma:** `def` bloğu yazıldığında fonksiyon yalnızca belleğe tanımlanır, henüz çalıştırılmaz. Kodun çalışması için `toplama_function(10, 20)` şeklinde argümanlar gönderilerek **çağrılması** gerekir.

* `10` değeri `arg1` parametresine, `20` değeri ise `arg2` parametresine aktarılır. `arg3` için varsayılan değer `None` tanımlandığından çağrı sırasında argüman gönderilmesi zorunlu tutulmamıştır.

> * *reusable code* → bir kez yazıldıktan sonra farklı girdilerle tekrar tekrar kullanılabilen modüler kod yapısı.
> * *local scope* → fonksiyon parametrelerinin ve içeride tanımlanan değişkenlerin yalnızca o fonksiyon sınırları içinde geçerli olması durumu.
> * *implicit return None* → içinde `return` deyimi bulunmayan fonksiyonların Python tarafından otomatik olarak `None` döndürmesi.
> * *function call* → tanımlanmış bir fonksiyonu adı ve parantez içindeki argümanlarıyla tetikleyip çalıştırma işlemi.

---

## 3. Functions: Positional ve Named Arguments

Kirk Byers bu bölümde, fonksiyon tanımlama ve çağırma süreçlerindeki terminoloji farkını, argüman aktarım yöntemlerini ve positional ile named arguments yapılarının birlikte kullanımındaki katı kuralları ele almaktadır.

---

### 3.1 Parameter vs. Argument Terminoloji Ayrımı

Programlamada sıkça birbirinin yerine kullanılan iki temel kavram arasında net bir sınır vardır:

* **Parameter:** Fonksiyon tanımlanırken parantez içine yazılan değişkenlerdir. Bu değişkenler yalnızca o fonksiyonun kendi local kapsamında var olur ve dış dünyadan tamamen izoledir.

* **Argument:** Fonksiyon çağrılırken parantez içine yazılıp fonksiyona gönderilen gerçek verilerdir. Çağrı anında bu argümanlar, fonksiyon tanımındaki ilgili parametrelere bağlanır.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [1]: def output_function(output):
   ...:     print()
   ...:     print("#" * 10)
   ...:     print("Output: ")
   ...:     print(output)
   ...:     print("#" * 10)
   ...:     print()
   ...: 

In [2]: output_function("nasılsın?")

##########
Output: 
nasılsın?
##########
```

---

### 3.2 Positional Arguments

Fonksiyona veri aktarmanın en temel ve doğrudan yolu positional arguments kullanmaktır.

* **Sıralı Eşleşme Mantığı:** Çağrı sırasında gönderilen argümanlar, fonksiyon tanımındaki parametrelere sırasıyla bağlanır. İlk gönderilen argüman birinci parametreye, ikinci gönderilen argüman ise ikinci parametreye atanır.

* Sıralama tamamen konuma dayalı olduğu için argümanların yazım sırası doğrudan çıktıyı belirler.
  
---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [3]: def output_function(msg1, msg2):
   ...:     print()
   ...:     print("#" * 10)
   ...:     print(f"Output 1: {msg1}")
   ...:     print("-" * 10)
   ...:     print(f"Output 2: {msg2}")
   ...:     print("#" * 10)
   ...:     print()
   ...: 

In [4]: output_function("nasılsın?", "iyiyim")

##########
Output 1: nasılsın?
----------
Output 2: iyiyim
##########
```

---

### 3.3 Named Arguments

Argümanları gönderirken konum sırasına bağlı kalmak istemediğimizde named arguments yöntemini kullanırız.

* **İsim Bazlı Bağlama:** Fonksiyon çağrılırken doğrudan parametre adı belirtilerek değer ataması yapılır.

* **Sıra Bağımsızlığı:** Python'a hangi değerin hangi parametreye gideceği açıkça söylendiği için, argümanların çağrı parantezi içindeki yazım sırası artık önemini yitirir. Önce ikinci parametrenin, sonra birinci parametrenin değeri gönderilebilir.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [5]: def output_function(msg1, msg2):
   ...:     print()
   ...:     print("#" * 10)
   ...:     print(f"Output 1: {msg1}")
   ...:     print("-" * 10)
   ...:     print(f"Output 2: {msg2}")
   ...:     print("#" * 10)
   ...:     print()
   ...: 

In [6]: output_function(msg2="nasılsın?", msg1="iyiyim")

##########
Output 1: iyiyim
----------
Output 2: nasılsın?
##########
```

---

### 3.4 Positional ve Named Arguments Karışık Kullanımı ve Hata Analizi

Python, tek bir fonksiyon çağrısında hem positional hem de named arguments kullanılmasına izin verir ancak bu işlem için kesin bir kural uygular:

> **Kritik Python Kuralı:**
> Bir fonksiyon çağrısında **tüm positional arguments en başta yer almalı, named arguments ise onlardan sonra gelmelidir**. Önce named argument yazıp ardından positional argument göndermek Python'da syntax hatasına yol açar.

#### Kullanılabilir Parametre Havuzu Mantığı

Kirk Byers, Python'ın bu eşleştirmeyi arka planda nasıl yönettiğini kullanılabilir parametreler kümesi üzerinden açıklar:

1. Fonksiyon çağrıldığında elimizde boşta duran bir parametre havuzu bulunur.

2. İlk sıradaki positional argümanlar, tanım sırasına göre havuzdaki ilk parametrelere bağlanır ve o parametreler havuzdan düşülür.

3. Geriye kalan boş parametreler için named arguments kullanılarak istenen sırada değer ataması yapılabilir.

4. Ancak positional olarak zaten doldurulmuş bir parametreye, devamında named argument ile tekrar değer atanmaya çalışılırsa Python `TypeError` hatası fırlatır.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [13]: def output_function(msg1, msg2, msg3):
    ...:     print(f"Output 1: {msg1}")
    ...:     print(f"Output 2: {msg2}")
    ...:     print(f"Output 3: {msg3}")
    ...: 

In [14]: output_function("Bu bir test - positional", msg3="message 3 - named args", msg2="message 2 - of positional and")
Output 1: Bu bir test - positional
Output 2: message 2 - of positional and
Output 3: message 3 - named args

In [18]: def output_function(msg1, msg2, msg3):
    ...:     print(f"Output 1: {msg1}")
    ...:     print(f"Output 2: {msg2}")
    ...:     print(f"Output 3: {msg3}")
    ...: 

In [19]: output_function("Bu bir test - positional", "message 3 - named args", msg2="message 2 - of positional and")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[19], line 1
----> 1 output_function("Bu bir test - positional", "message 3 - named args", msg2="message 2 - of positional and")

TypeError: output_function() got multiple values for argument 'msg2'
```

* **Traceback Satır Analizi:**
* `Cell In[19], line 1`: Hata 1. satırdaki fonksiyon çağrısında meydana geldi.
* `TypeError: output_function() got multiple values for argument 'msg2'`: İlk iki argüman positional olarak gönderildiği için `msg1` ve `msg2` parametreleri sırayla doldurulup havuzdan çıkarılmıştır. Havuzda sadece `msg3` boşta kalmışken `msg2` için ikinci kez named argument ile değer gönderilmesi bu hataya yol açmıştır.

> * *parameter* → fonksiyon tanımında parantez içine yazılan ve sadece fonksiyon içinde geçerli olan local değişken. 
> * *argument* → fonksiyon çağrılırken fonksiyona iletilen gerçek veri değeri.
> * *positional arguments* → fonksiyon tanımındaki parametre sırasına göre birebir konum bazlı eşleşen argümanlar. 
> * *named arguments* → parametre adı açıkça belirtilerek atanan ve yazım sırasından bağımsız çalışan argümanlar.
> * *TypeError: got multiple values for argument* → positional olarak zaten değer atanmış bir parametreye aynı çağrıda tekrar named argument ile değer verilmeye çalışıldığında alınan hata.

---

## 4. Functions: Default Values

Kirk Byers bu bölümde, fonksiyon tanımlanırken parametrelere varsayılan değer atanmasını, bu sayede çağrı sırasında ilgili argümanın opsiyonel hale gelmesini ve mevcut kodları bozmadan fonksiyonların zaman içinde nasıl genişletilebildiğini anlatmaktadır.

---

### 4.1 Parametrelere Varsayılan Değer Atama ve Opsiyonel Argüman Mantığı

Fonksiyon tanımında bir parametreye eşittir operatörü ile doğrudan bir başlangıç değeri verilebilir.

* **Opsiyonel Hale Gelme:** Varsayılan değere sahip olan bir parametreye, fonksiyon çağrılırken argüman gönderilmesi artık zorunlu değildir. Eğer çağrı sırasında bu parametre için bir değer belirtilmezse, Python tanımlama aşamasında atanan varsayılan değeri otomatik olarak kullanır.

* **Override Davranışı:** Fonksiyon çağrılırken ilgili parametreye yeni bir argüman gönderilirse, gönderilen bu yeni değer tanımlı olan varsayılan değerin üzerine yazılır ve onu geçersiz kılar.

* **Fonksiyonları Zaman İçinde Genişletme:** Kirk Byers, varsayılan değerlerin mevcut kod tabanını kırmadan fonksiyonlara yeni özellikler ve parametreler eklemek için son derece faydalı bir yöntem olduğunu vurgular. Eski çağrılar yeni eklenen parametreyi göndermese dahi varsayılan değer üzerinden sorunsuz çalışmaya devam eder.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [1]: def output_function(msg1, msg2, msg3="Selam"):
   ...:     print(f"Output 1: {msg1}")
   ...:     print(f"Output 2: {msg2}")
   ...:     print(f"Output 3: {msg3}")
   ...: 

In [2]: output_function(msg2="nasılsın?", msg1="hey!")
Output 1: hey!
Output 2: nasılsın?
Output 3: Selam
```

* `output_function` tanımlanırken `msg3` parametresine `"Selam"` varsayılan değeri atanmıştır.

* Çağrı sırasında yalnızca `msg1` ve `msg2` için named arguments gönderildiğinden, boşta kalan `msg3` parametresi otomatik olarak varsayılan `"Selam"` değerini almıştır.

> * *default value* → fonksiyon tanımında parametreye atanan ve çağrı sırasında argüman gönderilmediğinde devreye giren varsayılan değer.
> * *override* → fonksiyon çağrısında yeni bir argüman gönderilerek parametrenin varsayılan değerinin geçersiz kılınması.
> * *optional parameter* → varsayılan değere sahip olduğu için fonksiyon çağrılırken gönderilmesi zorunlu olmayan parametre.

---
