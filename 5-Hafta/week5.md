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

## 3. Regular Expressions: Special Characters 

Kirk Byers, regular expression dilinde pattern kurgularken kullandığımız özel metakarakterlerin (special characters) çalışma mantığını ve kritik detaylarını derinleştirmektedir.

---

### 3.1 Nicelik Belirteçleri (Quantifiers): Greedy vs. Non-Greedy (Lazy) Match

Metakarakterlerin arkasına eklenen quantifier'lar, ilgili karakterin kaç kez tekrarlanacağını ve regex motorunun metni tarama davranışını belirler.

* **`.` (Any single character):** Herhangi bir tekil karakterle eşleşir. Boş karakter (`null string`) ile eşleşmez; ortamda mutlaka en az 1 karakter bulunmalıdır.

* **`.*` (Zero or more times):** Önündeki karakterin **0 veya daha fazla** tekrarlanmasıdır. Boş metin (`null string`) ile eşleşebildiği gibi, metindeki karakter dizilimini yakalar.

* **`.+` (One or more times):** Önündeki karakterin **en az 1 veya daha fazla** tekrarlanmasıdır. `.*` ifadesinden farklı olarak `null string` ile eşleşmez.

* **`?` Modifikatörü ve `.?` Yapısı:** `?` işareti, kendinden önce gelen karakteri veya grubu opsiyonel hale getirir (`a?` ifadesi `"a"` harfiyle veya `null string` ile eşleşir). `.?` ifadesi ise 0 veya 1 karakter yakalar; greedy yapısı gereği imkan varsa 1 karakteri eşleştirmeyi tercih eder.


#### Greedy (Açgözlü) Davranış

* Python regex motoru varsayılan olarak **greedy** çalışır.

* `.*` ve `.+` ifadeleri, pattern'ı genel anlamda bozmayacak şekilde metin içerisindeki **mümkün olan en uzun karakter bloğunu** yakalamaya çalışır.

#### Non-Greedy (Lazy) Match (`*?` ve `+?`)

* Quantifier'ların arkasına `?` eklendiğinde (`*?` veya `+?`), regex motoru **non-greedy (lazy)** moda geçer.

* Non-greedy yapı, genel deseni `True` tutacak şekilde koşulu sağlayan **en az sayıda karakteri (mümkün olan en kısa metin bloğunu)** eşleştirmeyi hedefler.

---

### 3.2 Karakter Sınıfları ve Kombinasyonlar

Built-in karakter sınıfları metindeki belirli türdeki karakter gruplarını hızlıca hedeflemeyi sağlar.

#### Built-in Karakter Sınıfları

* **`\s` (Whitespace character class):** Boşluk (`space`), tab (`\t`), yeni satır (`\n`), carriage return (`\r`) ve diğer unicode boşluk karakterlerini kapsar.

* **`\S` (Non-whitespace character class):** Boşluk karakteri olmayan (`\s` dışındaki) tüm karakterlerle eşleşir.

* **`\w` (Word character class):** Kelime karakterlerini kapsar. Küçük/büyük harfler (`a-z`, `A-Z`), rakamlar (`0-9`) ve alt çizgi (`_`) karakterlerini içerir.

* **`\d` (Digit character class):** Sayısal karakterlerle (`0-9`) eşleşir.


#### Quantifier'lar ile Karakter Sınıfı Kombinasyonu

Karakter sınıflarının arkasına `*` veya `+` eklenerek tekrarlı yapılardan veri ayıklanır:

* **`\s*`** → Sıfır veya daha fazla boşluk karakteri.
* **`\s+`** → En az bir veya daha fazla yan yana boşluk karakteri.
* **`\d+`** → Yan yana gelen bir veya daha fazla rakam bloğu.

#### Özel Karakter Sınıfı Oluşturma (`[]`)

Köşeli parantezler `[]` kullanılarak kendi karakter sınıfımızı tanımlayabiliriz.

* **IP Adresi Senaryosu Örneği:** `[0-9\.]` ifadesi, `0` ile `9` arasındaki tüm rakamlar ile literal nokta (`.`) karakterini barındıran özel bir karakter sınıfı tanımlar. Network cihazlarının çıktılarından IP adresi yakalarken son derece pratik bir çözümdür.

---

### 3.3 Çıpalar (Anchors) ve `re.MULTILINE` Flag'i

Çıpalar (anchors), arama pattern'ı aratılırken konum sabitlemesi yapmamızı sağlar.

* **`^` (Beginning of line/string):** Aramanın dizginin veya satırın başında olmasını şart koşar.
* **`$` (End of line/string):** Aramanın dizginin veya satırın sonunda olmasını şart koşar.

> **Kritik Davranış / `re.MULTILINE` Flag'i:**
> Varsayılan durumda `^` ve `$`, verilen string verisinin en başı ve en sonu ile eşleşir. Eğer çok satırlı bir network cihazı çıktısı üzerinde satır satır baş/son araması yapılmak isteniyorsa, regex aramasına **`re.MULTILINE`** flag'i verilir. Bu flag, `^` ve `$` çıpalarının her yeni satır başında (`\n`) yeniden tetiklenmesini sağlar. 

---

### 3.4 Gruplama, Mantıksal VEYA ve Escape Karakteri

* **`()` (Capturing / Grouping):** Pattern içerisindeki belirli parçaları hafızada tutmak ve daha sonra ayıklayıp almak için parantez kullanılır. Birden fazla parantez grubu kurgulanabilir.

* **`(|)` (Logical OR):** Parantez içerisinde alternatif mantıksal seçenekler sunar (`(GigabitEthernet|FastEthernet)` gibi).

* **`\` (Escape sequence):** Regex dilinde metakarakter olan sembolleri (örneğin `.`, `?`, `*`) özel anlamlarından arındırıp metindeki doğrudan yalın sembol halleriyle eşleştirmek için kullanılır.

> * *quantifier* → bir karakterin veya grubun kaç kez tekrarlanacağını belirten nicelik sembolleri (`*`, `+`, `?`).
> * *greedy* → pattern'ı doğrulayan en uzun metin bloğunu yakalama eğilimi (`.*`, `.+`). 
> * *non-greedy (lazy)* → pattern'ı doğrulayan olabilecek en kısa metin bloğunu yakalama eğilimi (`*?`, `+?`).
> * *custom character class* → `[]` köşeli parantezleri ile kullanıcı tarafından özel tanımlanan karakter kümesi.
> * *anchor* → arama konumunu başa (`^`) veya sona (`$`) sabitleyen çapa simgeleri.
> * *re.MULTILINE* → çıpaların tüm metin yerine satır bazlı çalışmasını sağlayan regex seçeneği/flag'i.

---
