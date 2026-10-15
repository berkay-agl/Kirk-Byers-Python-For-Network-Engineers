# Lesson 5 Hakkında

## 1. Giriş: Table of Contents

Lesson 5 kapsamında Python'da metin işleme ve veri ayıklama süreçlerinin en kritik araçlarından biri olan **Regular Expressions (Düzenli İfadeler / Regex)** konusu ele alınmaktadır.

Kirk Byers bu derste sırasıyla aşağıdaki konuları işleyeceğini belirtmektedir:

* **Regular Expressions:** Regex nedir, ağ otomasyonundaki veri ayıklama problemlerini çözmek için neden gereklidir ve temel kullanım ilkeleri.

> * *regular expressions (regex)* → metinler içerisinden belirli desenlere (pattern) göre veri aramayı ve ayıklamayı sağlayan özel desen dili.
> * *re module* → Python'da regular expression işlemlerini yürüten dahili standart kütüphane.
> * *re.search()* → verilen deseni metin içerisinde arayan ve ilk eşleşmede bir match object döndüren fonksiyon.
> * *match object* → regex eşleşmesine dair konum (`span`) ve eşleşen metin bilgilerini barındıran nesne.
> * *.group(0)* → match object içerisinden eşleşen metnin tamamını elde etmeyi sağlayan metot.

---

## 2. Regular Expressions Giriş

Kirk Byers, ağ otomasyonunda cihazlardan dönen raw string verilerini işlerken regular expression yapılarının hayati bir role sahip olduğunu vurgulamaktadır.

---

### 2.1 Neden Regular Expressions? Hangi Problemi Çözüyoruz?

Network mühendisliğinde kullanılan cihazlar (örneğin Cisco router/switch çıktıları olan `show version` vb.) otomasyon kodlarına doğrudan string çıktısı döndürür. 
Bu metinlerin içerisine gömülmüş olan IP adresleri, seri numaraları veya konfigürasyon kayıtları gibi spesifik verileri sistematik olarak ayıklamak gerekir.

* **Geleneksel Yöntemlerin Sınırı:** Daha önce öğrenilen `.split()` metodu veya `in` koşul kontrolleri basit senaryolarda iş görse de, daha karmaşık ve değişken metin yapılarından veri çıkarmak için yetersiz kalır.

* **Regex Dili:** Regular expressions, string ifadelerin içine özel karakterler yerleştirerek desenler (patterns) oluşturmamızı sağlayan özel bir "dildir".

* **Kirk Byers'ın Uyarısı & Aforizması:** Kirk Byers, regex yazarken aşırı karmaşık yapılardan kaçınılması gerektiği konusunda esprili ve kritik bir uyarıda bulunur: *"The road to hell is paved with good intentions and complex regular expressions"* (Cehenneme giden yol iyi niyetler ve karmaşık düzenli ifadelerle döşelidir). Koda gereksiz karmaşıklık katmamak esastır.

---

### 2.2 Birebir Karakter Eşleşmesi ve `re.search()`

Regular expression işlemlerini kullanabilmek için öncelikle Python'ın dahili **`re`** kütüphanesi içe aktarılır (`import re`).

`re.search()` fonksiyonu iki temel argüman ile çalışır:

1. **Pattern (Desen):** Aranan özel karakter dizilimi.

2. **Data:** Arama yapılacak metin veya değişken.

En basit kullanım senaryosunda yani burada literal matching, pattern olarak doğrudan aradığımız kelimenin kendisi verilir:

```python
In [1]: import re

In [2]: data = "Configuration register"

In [3]: re.search("Configuration register", data)
Out[3]: <re.Match object; span=(0, 22), match='Configuration register'>
```

* `re.search()` fonksiyonu bir eşleşme bulduğunda geriye bir **`re.Match object`** döndürür.
* Eşleşme nesnesi, eşleşmenin metindeki başlangıç ve bitiş indekslerini (`span=(0, 22)`) ve yakalanan metni (`match='Configuration register'`) gösterir.
* **Boolean Değerlendirme:** Bu match object bir `if` koşuluna verildiğinde; eşleşme varsa `True`, eşleşme yoksa (`None` döndüğünde) `False` olarak değerlendirilir.

---

### 2.3 Match Object ve `.group(0)` Kullanımı

Yakalanan regex nesnesi bir değişkene atandığında, eşleşen metni elde etmek için **`.group(0)`** metodu kullanılır:

```python
In [4]: data = "abc123"

In [5]: match_result = re.search("abc123", data)

In [6]: match_result
Out[6]: <re.Match object; span=(0, 6), match='abc123'>

In [7]: match_result.group(0)
Out[7]: 'abc123'

In [8]: data = "Configuration register"

In [9]: match_result = re.search("Configuration register", data)

In [10]: match_result
Out[10]: <re.Match object; span=(0, 22), match='Configuration register'>

In [11]: match_result.group(0)
Out[11]: 'Configuration register'
```

* `match_result.group(0)` ifadesi, regex pattern'ı tarafından yakalanan metnin tamamını string olarak teslim eder.
* Birebir string araması - literal matching regex'in en yalın halidir; ilerleyen adımlarda özel karakterler ile dinamik pattern'lar kurgulanacaktır.

> * *pattern* → arama yapmak veya veri ayıklamak için tanımlanan karakter dizilimi deseni. 
> * *literal characters* → özel bir anlam taşımayan, metinde birebir aynısı aranan yalın karakterler.
> * *span* → match object içinde eşleşmenin başladığı ve bittiği indeks aralığını belirten nitelik.
> * *group(0)* → yakalanan eşleşmenin tamamını string olarak döndüren metot.

---

