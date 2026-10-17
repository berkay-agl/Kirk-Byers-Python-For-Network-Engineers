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

## 4. Regular Expressions: Pratikte Regex Kullanımı ve Basit Örnekler

Kirk Byers bu bölümde, bir önceki videoda teorisini anlattığı metakarakterleri ve karakter sınıflarını `show_version.txt` dosyası üzerinden canlı IPython REPL ortamında adım adım denemektedir.

---

### 4.1 `re.search()` Fonksiyon Yapısı ve Parametre Detayları

`re.search()` fonksiyonunun arka plandaki tam imzası şu şekildedir:

$$\text{re.search(pattern, string, flags=0)}$$

* **`pattern`:** Metin içinde aranacak regex desen ifadesi.
* **`string`:** Aramanın yapılacağı raw veri değişkeni.
* **`flags` (Opsiyonel):** Arama davranışını değiştiren bayraklar (Varsayılan değer: `0`).

---

### 4.2 Veri Hazırlığı: `show_version.txt` Dosyasını Okuma ve Satır Seçimi

Kirk Byers ilk olarak dosyayı okur ve `splitlines()` ile satırlara böler:

```python
In [1]: f = open("show_version.txt")

In [2]: data = f.read()

In [3]: line = data.splitlines()[0]

In [4]: line
Out[4]: 'Cisco IOS XE Software, Version 16.12.03'

In [5]: print(line)
Cisco IOS XE Software, Version 16.12.03

In [6]: line = data.splitlines()[1]

In [7]: print(line)
Cisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)
```

> **Kirk'ün Mantık Açıklaması:** Kirk ilk olarak 0. indeksteki ilk satırı alır (`line = data.splitlines()[0]`). Ancak daha zengin bir metin üzerinde regex denemeleri yapmak için fikrini değiştirip 1. indeksteki ikinci satırı (`line = data.splitlines()[1]`) seçer.

---

### 4.3 Nokta (`.`) ve Quantifier (`*`, `+`) Deneyleri: Greedy vs. Non-Greedy

#### Tekil Karakter Eşleşmesi Mantığı (`.` ve `..`)

```python
In [8]: import re

In [9]: re.search(".", line)
Out[9]: <re.Match object; span=(0, 1), match='C'>

In [10]: re.search("..", line)
Out[10]: <re.Match object; span=(0, 2), match='Ci'>
```

* **Neden sadece 'C' yakalandı?** Kirk Byers burada kritik bir noktayı vurgular: `.` tek bir karakter şartı koşar. Regex motoru metnin en başından başlar, ilk karakter olan `'C'` ile karşılaşır, pattern şartı doğrulandığı an aramayı sonlandırır (devamındaki karakterleri taramaz).

* `".."` yazıldığında ise yan yana iki karakter şartı arandığı için en baştaki `'Ci'` bloğunu yakalar.

#### Greedy `.*` Eşleşmesi ve IPython Ekran Kırpma Detayı

```python
In [11]: re.search(".*", line)
Out[11]: <re.Match object; span=(0, 124), match='Cisco IOS Software [Gibraltar], ISR Software (ARM>

In [12]: m = re.search(".*", line)

In [13]: m.group(0)
Out[13]: 'Cisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)'
```

* `.*` ifadesi "0 veya daha fazla her karakter" anlamına gelir ve varsayılan olarak **greedy** davrandığı için satırın başından sonuna kadar olabilecek en uzun metni (124 karakter) yakalar.

* **IPython REPL Kırpma Davranışı:** `Out[11]` çıktısında metnin sonu `ARM>` şeklinde kırpılmıştır. Kirk, IPython ekranının çıktıyı göstermek için kısaltma yaptığını, ancak `m.group(0)` çağrıldığında yakalanan 124 karakterlik metnin **tamamının** eksiksiz olarak döndürüldüğünü gösterir.

#### Non-Greedy (Lazy) `.*?` ve `.+?` Farkı

```python
In [14]: line
Out[14]: 'Cisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)'

In [15]: m = re.search(".*?", line)

In [16]: m.group(0)
Out[16]: ''

In [17]: m = re.search(".+?", line)

In [18]: m.group(0)
Out[18]: 'C'
```

* **`.*?` Durumu:** `*` işareti 0 veya daha fazla tekrar demektir. Arkasındaki `?` non-greedy moda geçirir (en az karakteri yakala). 0 karakter (boş metin `''`) deseni doğruladığı için sonuç boş string olur.

* **`.+?` Durumu:** `+` işareti "en az 1 karakter bulunmalı" şartı koşar. Non-greedy mod en az sayıda karakter aradığı için `null string` üretemez, en küçük geçerli blok olan tek bir karakteri (`'C'`) yakalar.

---

### 4.4 Karakter Sınıfları (`\s`, `\S`, `\w`), Raw String (`r""`) ve Çoklu Boşluk Testi

Regex pattern'larında ters eğik çizgilerin (`\`) Python tarafından özel kaçış karakteri olarak yorumlanmasını engellemek için **Raw String (`r"..."`)** notasyonu kullanılır.

#### `\s` (Whitespace) ile Kelime Arası Arama

```python
In [27]: line
Out[27]: 'Cisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)'

In [28]: m = re.search(r"Cisco\s.*Gibraltar", line)

In [29]: m.group(0)
Out[29]: 'Cisco IOS Software [Gibraltar'
```

* `r"Cisco\s.*Gibraltar"` pattern `"Cisco"` ile başlar, arada tek bir boşluk (`\s`) arar ve ardından `Gibraltar` kelimesine kadar olan tüm bloğu yutar.

#### Çoklu Boşluk İçeren Test Satırı (`alt_line`)

Kirk, `\s+` yapısının greedy şekilde birden fazla boşluğu nasıl yuttuğunu göstermek için 3 adet boşluk içeren özel bir alternatif satır tanımlar (`alt_line = "Cisco   Fuji"`):

```python
In [30]: alt_line = "Cisco   Fuji"

In [31]: m = re.search(r"Cisco\s+Fuji", alt_line)

In [32]: m.group(0)
Out[32]: 'Cisco   Fuji'

In [33]: m = re.search(r"\S+\s+Fuji", alt_line)

In [34]: m.group(0)
Out[34]: 'Cisco   Fuji'

In [35]: m = re.search(r"\w+\s+Fuji", alt_line)

In [36]: m.group(0)
Out[36]: 'Cisco   Fuji'
```

1. **`r"Cisco\s+Fuji"`:** `"Cisco"` ile `"Fuji"` arasındaki 3 adet boşluğun tamamı `\s+` (greedy boşluk kümesi) tarafından yutulur.

2. **`r"\S+\s+Fuji"`:** `"Cisco"` ismi sabit yazılmak yerine `\S+` (boşluk olmayan karakterler dizisi) ile esnekleştirilir, ardından 3 boşluk ve `"Fuji"` yakalanır.

3. **`r"\w+\s+Fuji"`:** `"Cisco"` kelimesi `\w+` (word characters dizisi) ile yakalanır, ardından 3 boşluk ve `"Fuji"` eşleştirilir.

> * *re.search(pattern, string, flags=0)* → regex arama fonksiyonu ve varsayılan parametre yapısı.
> * *raw string (r"...")* → ters eğik çizgi (`\`) kaçışlarını etkisiz kılan string biçimi.
> * *IPython Output Truncation* → uzun regex çıktılarının REPL ekranında `...` ile kısaltılması; `.group(0)` ile verinin tamamının çekilmesi.
> * *\s+* → bir veya daha fazla ardışık boşluk karakterinin greedy şekilde tamamının yakalanması.
> * *\S+* → bir veya daha fazla boşluk olmayan karakter bloğu.
> * *\w+* → harf, rakam ve alt çizgiden oluşan kelime bloğu.

---

## 5. Regular Expressions: Ek Örnekler (Gelişmiş Pattern Oluşturma & Greedy Davranış Tuzakları)

Kirk Byers bu bölümde, digit karakter sınıfı (`\d`), özel karakter sınıfı (`[]`), parantez grupları (`()`), satır başı/sonu çıpaları (`^`, `$`) ve regex yazarken en sık karşılaşılan "greedy (açgözlü) `.*` tuzağını" canlı terminal uygulamaları üzerinden anlatmaktadır.

---

### 5.1 Sayısal Karakter Sınıfı (`\d`) ve Rakam Yakalama

Örnekler üzerinde çalışılan Cisco yazılım sürümü satırı şu şekildedir:

```python
In [1]: line = "Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, RELEASE SOFTWARE (fc3)"

In [2]: import re
```

#### Greedy `.*` Tuzağı ve Tekil Rakam (`\d+`) Arama

Satır başı çıpası (`^`) ve `"Cisco"` ile başlayan, ardından `.*` ve `\d+` gelen ilk pattern denenir:

```python
In [3]: m = re.search(r"^Cisco.*\d+", line)

In [4]: m.group(0)
Out[4]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, RELEASE SOFTWARE (fc3'
```

* **Kirk Byers'ın Mantık Açıklaması ve Kendi Hatasını İtirafı:** Kirk, bu deseni ilk yazdığında `.*` ifadesinin sürüm numarası olan `16.8.1` kısmındaki `1` rakamında duracağını düşündüğünü ancak bunun yanlış olduğunu vurgular.

* **Regex Motorunun Öncelik Kuralı:** Regex motoru öncelikle tüm pattern'ı `True` kılacak durumları arar; ardından soldan sağa doğru greedy parçaları **maksimuma çıkarır**.

* Araya konan `.*` açgözlü olduğu için metnin sonundaki `fc3` kısmında bulunan `3` rakamına kadar olan tüm karakterleri yutar. `\d+` ise sadece sondaki `3` rakamıyla eşleşir.

#### Ardışık İki Rakam (`\d\d`) ile Sürüm Yakalama

```python
In [5]: line
Out[5]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, RELEASE SOFTWARE (fc3)'

In [6]: m = re.search(r"^Cisco.*\d\d", line)

In [7]: m.group(0)
Out[7]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16'
```

* Metinde yan yana iki rakamın (`\d\d`) bulunduğu tek yer `Version 16` kısmındaki `16` sayısıdır (`fc3` kısmında tek rakam vardır).

* Regex motoru pattern'ı `True` tutabilmek adına `.*` ifadesini `16` sayısına kadar genişletmek zorunda kalır ve eşleşme `Version 16` ile sonlanır.

---

### 5.2 Tam Sürüm Formatı ve Parantez ile Yakalama 

Literal nokta (`\.`) ve rakamlar birleştirilerek sürüm yapısı tam olarak hedeflenir:

```python
In [8]: m = re.search(r"^Cisco.*\d\d\.\d\.\d", line)

In [9]: m.group(0)
Out[9]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1'
```

#### Parantez `()` ile Grubun Hafızaya Alınması

Tüm eşleşen metni değil, sadece versiyon numarasını ayıklayıp kaydetmek için ilgili kısım parantez içine alınır:

```python
In [10]: m = re.search(r"^Cisco.*(\d\d\.\d\.\d)", line)

In [11]: m.group(0)
Out[11]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1'

In [12]: m.group(1)
Out[12]: '16.8.1'
```

* `m.group(0)` → Pattern'ın eşleştiği başından sonuna kadar olan **tüm metni** verir.

* `m.group(1)` → Parantez ile oluşturulan **1. yakalama grubunu** yani `'16.8.1'` değerini döndürür.

#### Satır Sonu Çıpası (`$`) Kullanımı

İstenirse desene satır sonu çıpası (`.*$`) eklenerek arama satırın en sonuna kadar uzatılabilir:

```python
In [13]: m = re.search(r"^Cisco.*(\d\d\.\d\.\d).*$", line)

In [14]: m.group(1)
Out[14]: '16.8.1'
```

---

### 5.3 Özel Karakter Sınıfları (`[]`), Hata Analizi ve Doğru Pattern Kurgusu

Rakam ve noktaları kapsayan özel bir karakter sınıfı (`[\d\.]`) tanımlanarak dinamik veri çekilmeye çalışılır.

#### Sınıf Tanımlama ve Greedy Davranış Sorunu

```python
In [16]: m = re.search(r"^Cisco.*([\d\.]+)", line)

In [17]: m.group(0)
Out[17]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, RELEASE SOFTWARE (fc3'

In [18]: m = re.search(r"^Cisco.*[\d\.]", line)

In [19]: m.group(0)
Out[19]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, RELEASE SOFTWARE (fc3'
```

* `[\d\.]` sınıfı tüm rakamlar ve literal nokta karakteriyle eşleşir.

* Ancak öndeki `.*` greedy olduğu için yine `fc3` içindeki `3` rakamına kadar ilerler.

#### Pattern Sınırlandırma ve `IndexError` Hata Analizi

Sürüm numarasından sonra gelen `", REL"` ifadesi desene eklenerek aramanın duracağı yer sınırlandırılmak istenir:

```python
In [20]: m = re.search(r"^Cisco.*[\d\.]+, REL", line)

In [21]: m.group(0)
Out[21]: 'Cisco IOS Software [Fuji], ISR Software (ARMV8EB_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.8.1, REL'

In [22]: m.group(1)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[22], line 1
----> 1 m.group(1)

IndexError: no such group
```

* **Traceback Satır Analizi:**
* `Cell In[22], line 1`: Hata 1. satırdaki `m.group(1)` çağrısında meydana geldi.

* `IndexError: no such group`: Eşleşme başarılı olsa da regex deseninde parantez `()` ile tanımlanmış herhangi bir grup olmadığı için 1. grup çağrılamaz.

#### Yanlış Capturing vs. Tam Çözüm

1. **Parantez Eklendi Ama `.*` Hâlâ Greedy (`group(1)` '1' Döndü):**
```python
In [23]: m = re.search(r"^Cisco.*([\d\.]+), REL", line)

In [24]: m.group(1)
Out[24]: '1'
```

* **Kirk Byers'ın Uyarısı:** `.*` ifadesi o kadar açgözlüdür ki, `Version 16.8.` kısmına kadar olan metni kendisi yutar. `([\d\.]+)` grubuna sadece sürümün son rakamı olan `'1'` kalır.

2. **Dışarıya Sınır Koyarak Tam Çözüm:**
```python
In [25]: m = re.search(r"^Cisco.*ion ([\d\.]+), REL", line)

In [26]: m.group(1)
Out[26]: '16.8.1'
```

* Parantezin hemen dışına `"ion "` (yani `"Version "` kelimesinin sonu) sabitleyicisi konur.

* `.*` açgözlülüğü `"ion "` ifadesini görünce durmak zorunda kalır.

* Parantez içi `([\d\.]+)` sürüm numarasının tamamı olan `'16.8.1'` değerini eksiksiz yakalar.

> * *digit character class (\d)* → 0-9 arası tüm sayısal karakterlerle eşleşen sınıf.
> * *capturing group ()* → regex deseni içinde istenen metin parçalarını gruplayıp `.group(1)`, `.group(2)` şeklinde çekmeyi sağlayan parantez yapısı.
> * *IndexError: no such group* → regex aramasında parantez grubu tanımlanmadığı halde `m.group(1)` çağrıldığında alınan hata.
> * *greedy prefix problem* → `.*` ifadesinin parantez içindeki deseni daraltacak şekilde metnin büyük kısmını yutması durumu.
> * *anchor/boundary constraint* → `.*` açgözlülüğünü dizginlemek için parantez öncesine (`ion `) veya sonrasına (`RELEASE`) eklenen sabit karakter sınırları. 

---

## 6. Regular Expressions: Capture Groups ve Raw Strings

Kirk Byers bu bölümde, parantez ile veri yakalama gruplarını, Python'da **Raw String (`r"..."`)** kullanımının temel sebebini ve greedy aramalarda virgül gibi ayırıcı sınırlandırmaların ek virgül senaryolarında nasıl patladığını `.*?` (non-greedy) çözümüyle ele almaktadır.

---

### 6.1 Configuration Register Örneği ve Capturing Group (`group(1)`)

Cisco IOS/IOS-XE cihaz çıktılarında konfigürasyon kaydını gösteren `Configuration register is 0x2102` satırından hex değerinin ayıklanması örneği incelenir:

```python
In [3]: import re

In [4]: data = """
   ...: License Information for 'c880-data'
   ...:   License Level: advipservices    Type: Permanent
   ...:   Next reboot license Level: advipservices
   ...: 
   ...: Configuration register is 0x2102
   ...: """

In [5]: print(data)

License Information for 'c880-data'
  License Level: advipservices    Type: Permanent
  Next reboot license Level: advipservices

Configuration register is 0x2102

In [6]: m = re.search(r"Configuration register is (.*)", data)

In [7]: m.group(0)
Out[7]: 'Configuration register is 0x2102'

In [8]: m.group(1)
Out[8]: '0x2102'

In [9]:
```

* **`m.group(0)`:** Desenin metinde eşleştiği tüm bloğu (`'Configuration register is 0x2102'`) teslim eder.

* **`m.group(1)`:** Parantez `(.*)` içine alınan ilk **capturing group** alanını yani doğrudan ayıklamak istediğimiz hex değerini (`'0x2102'`) döndürür.

---

### 6.2 Python'da Raw String (`r"..."`) Kullanım Mantığı ve Nedeni

Kirk Byers, regex yazarken string ifadelerinin başına neden ısrarla `r` karakteri (Raw String) konulması gerektiğini şu şekilde açıklar:

1. **Python Special Characters:** Python'ın kendi string mekanizmasında özel kaçış dizilimleri bulunur. Örneğin `"\n"` ifadesi ters eğik çizgi ve 'n' harfi değil, tek başına "yeni satır" karakteridir. Benzer şekilde `"\t"` bir tab karakteridir.

2. **Regex Special Characters:** Regular expression dilinin de kendine ait özel metakarakterleri (`\s`, `\d`, `\w`, `\S` vb.) vardır.

3. **Çakışma Problemi & Çözüm:** Regex pattern yazarken Python'ın kaçış karakterlerinin regex metakarakterleriyle çakışmasını engellemek esastır.

4. **Raw String (`r"..."`):** String ifadesinin başına `r` eki getirildiğinde Python'a *"Metin içindeki kaçış karakterlerinin yorumlanmasını kapat, string'i olduğu gibi ham/raw teslim et ve sadece Regex motorunun özel anlamları çalışsın"* talimatı verilir. Bu nedenle regex kalıplarında istisnasız raw string kullanılması standart bir disiplindir.

---

### 6.3 Greedy Arama vs. Virgül Sınırlandırması

Bir cihaz çıktısındaki OS versiyon bilgisini ayıklarken `.*` ifadesinin greedy davranışı yeniden gözlemlenir:

```python
In [12]: line = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)"

In [13]: line
Out[13]: 'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)'

In [14]: m = re.search(r"Version (.*)", line)

In [15]: m.group(0)
Out[15]: 'Version 15.4(2)T1, RELEASE SOFTWARE (fc3)'

In [16]: m.group(1)
Out[16]: '15.4(2)T1, RELEASE SOFTWARE (fc3)'

In [17]:
```

* `r"Version (.*)"` yazıldığında parantez içindeki `.*` satır sonuna kadar açgözlü şekilde ilerlediği için versiyon numarasıyla birlikte `, RELEASE SOFTWARE (fc3)` kısmını da yutar.

#### Virgül Sınırı Ekleyerek Yakalamayı Durdurma

Aramayı tam versiyon numarasının bittiği yerdeki virgülde durdurmak için parantezin dışına virgül `,` eklenir:

```python
In [17]: m = re.search(r"Version (.*),", line)

In [18]: m.group(1)
Out[18]: '15.4(2)T1'

In [19]: 
```

* Parantez dışındaki virgül `,` bir sınır görevi görür. `.*` ifadesi virgüle kadar olan kısmı yakalar, virgül ise capturing group `m.group(1)` dışında kaldığı için tam olarak `'15.4(2)T1'` versiyonu çekilmiş olur.

---

### 6.4 Çift Virgül Senaryosu ve Non-Greedy (`.*?`) Çözümü

Ancak metnin ilerleyen kısımlarında fazladan bir virgül daha bulunuyorsa (örneğin satır sonunda `,` varsa) parantez dışına tek başına virgül koymak greedy tuzağını çözmeye yetmez:

```python
In [19]: line = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3),"

In [20]: line
Out[20]: 'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3),'

In [21]: m = re.search(r"Version (.*),", line)

In [22]: m.group(1)
Out[22]: '15.4(2)T1, RELEASE SOFTWARE (fc3)'

In [23]:
```

* **Problem:** Satır sonuna eklenen ikinci virgül nedeniyle `.*` açgözlü yapısı gereği metindeki **en son virgüle** kadar uzanır ve aradaki tüm metni yine yutar.

#### Non-Greedy (Lazy) Modifikatörü (`.*?`) ile Çözüm

`.*` joker karakterinin arkasına `?` modifikatörü eklendiğinde açgözlülük kapatılır:

```python
In [23]: m = re.search(r"Version (.*?),", line)

In [24]: m.group(1)
Out[24]: '15.4(2)T1'

In [25]:
```

* **Mekanizma:** `.*?` ifadesi koşulu doğrulayan **en kısa** metin bloğunu arar. `Version ` kelimesinden sonra karşılaştığı **ilk virgülde** durarak yakalamayı sonlandırır ve `'15.4(2)T1'` değerini mükemmel şekilde ayıklar.

> **Kritik Uyarım:** Eğer `.*?` kullanılırken desendeki virgül `,` kaldırılırsa (`r"Version (.*?)"`), non-greedy mod en az karakteri yakalamaya çalışacağı için `m.group(1)` boş string (`''`) döndürür. Dolayısıyla non-greedy ifadelerin arkasında durabileceği somut bir sınır karakteri (virgül, boşluk vb.) bulunmalıdır.

> * *capturing group* → regex deseninde `()` ile çevrelenerek hafızaya alınan ve `.group(1)` ile çekilen veri grubu.
> * *raw string (r"...")* → Python'ın string kaçış dizilimlerini (`\n`, `\t`) devreden çıkarıp Regex metakarakterlerinin yorumlanmasını sağlayan ön takı.
> * *delimiter boundary* → greedy `.*` karakterini belirli bir simgede (örneğin virgül `,`) durdurmak için parantez dışına konan sınır karakteri.
> * *non-greedy wildcard (.*?) * → karşılaşacağı ilk sınır karakterine kadar olan en kısa metin bloğunu yakalayan lazy arama deseni.

---

## 7. Regular Expressions: Anchors ve `re.MULTILINE` Flag'i

Kirk Byers bu bölümde, satır başı (`^`) ve satır sonu (`$`) çıpalarının (anchors) varsayılan davranışlarını, çok satırlı veriler üzerinde çalışırken neden başarısız olduklarını ve **`re.MULTILINE` (`re.M`)** flag'ı ile bu çıpaların satır bazlı çalışacak şekilde nasıl dönüştürüldüğünü anlatmaktadır.

---

### 7.1 Anchors Varsayılan Davranışı

Regular expression dilinde kullanılan iki temel konum çıpası bulunur:

* **`^` (Carrot):** Satır başı çıpası.

* **`$` (Dollar):** Satır sonu çıpası.

> **Kritik Varsayılan Davranış:**
> Python regex motorunda `^` ve `$`, varsayılan olarak **tüm metin bloğunun** en başını ve en sonunu temsil eder. Metnin içerisinde `\n` ile ayrılmış yüzlerce satır bulunsa dahi, `^` yalnızca ilk satırın en başı, `$` ise en son satırın en sonu anlamına gelir.

---

### 7.2 Çok Satırlı Veride Başarısız Arama ve `AttributeError` Analizi

Çok satırlı Cisco `show version` çıktısı barındıran `data` değişkeni üzerinde, metnin sonlarında yer alan `Configuration register is 0x2102` satırı çıpalarla hedeflenir:

```python
In [1]: import re

In [2]: f = open("show_version.txt")

In [3]: data = f.read()

In [4]: f.close()

In [5]: data
Out[5]: 'Cisco IOS XE Software, Version 16.12.03\nCisco IOS Software [Gibraltar], ISR Software (ARMV8EL_LINUX_IOSD-UNIVERSALK9_IAS-M), Version 16.12.3, RELEASE SOFTWARE (fc5)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2020 by Cisco Systems.....ISTERED/AUTHORIZED\ncisco.\nProcessor board ID FGL222290LB\n1 Virtual Ethernet interface\n6 Gigabit Ethernet interfaces\n32768K bytes of non-volatile configuration memory.\n4194304K bytes of physical memory.\n2863103K bytes of flash memory at bootflash:.\n0K bytes of WebUI ODM Files at webui:.\nConfiguration register is 0x2102\n'

In [6]: 
```

#### Çıpalar Yüzünden Aramanın `None` Dönmesi

Aynı arama `Configuration register` satırı için yapıldığında da eşleşme sağlanamaz:

```python
In [6]: m = re.search(r"^Config.*2102$", data)

In [7]: print(m)
None

In [8]: 
```

* **Nedeni:** `r"^Config.*2102$"` pattern; metnin **en başının** `"Config"` ile başlamasını ve metnin **en sonunun** `"2102"` ile bitmesini şart koşar. Oysa `data` metni `"Cisco IOS XE..."` ile başlamakta ve `"...Configuration register is 0x2102"` ile bitmektedir. Aradaki satırlar varsayılan çıpalarla eşleşmez.

---

### 7.3 `re.MULTILINE` (`re.M`) Flag'i ile Satır Bazlı Çıpa Değişimi

Bu davranışı değiştirip çıpaları metindeki her bir satır başında (`\n` sonrası) ve satır sonunda geçerli kılmak için **`flags=re.MULTILINE`** veya kısaltması olan **`flags=re.M`** parametresi verilir:

```python
In [8]: m = re.search(r"^Config.*2102$", data, flags=re.MULTILINE)

In [9]: print(m)
<re.Match object; span=(3436, 3468), match='Configuration register is 0x2102'>

In [10]: m = re.search(r"^Config.*2102$", data, flags=re.M)

In [11]: print(m)
<re.Match object; span=(3436, 3468), match='Configuration register is 0x2102'>

In [12]: 
```

* **`re.MULTILINE` Mekanizması:** Flag aktif edildiğinde `^` ve `$`, metin içindeki her yeni satır karakterinde (`\n`) yeniden değerlendirilir.
* Böylece `Configuration register is 0x2102` satırı, kendi satır başı ve satır sonu çıpalarına uyum sağladığı için match object başarıyla elde edilir.

---

### 7.4 Çıpalar ve Capturing Group Kombinasyonu

Kirk'in Slaytta gösterilen örnek uygulamada, satır başı (`^`) ve satır sonu (`$`) çıpaları, `re.M` bayrağı ve `\S+` (boşluk olmayan karakter kümesi) parantez grubu ile birleştirilerek hex değeri tek adımda ayıklanır:

```python
In [45]: pattern = "^License Info"

In [46]: re.search(pattern, data, flags=re.MULTILINE)
Out[46]: <re.Match object; span=(1640, 1652), match='License Info'>

---

In [25]: pattern = r"^Configuration register is (\S+)$"

In [26]: m = re.search(pattern, data, flags=re.M)

In [27]: m.group(1)
Out[27]: '0x2102'

In [28]:
```

1. **`^Configuration register is `:** Satırın en başında `"Configuration register is "` ifadesi aranır.

2. **`(\S+)`:** Boşluk içermeyen hex karakter bloğu (`0x2102`) parantez içine alınarak 1. gruba kaydedilir.

3. **`$`:** Hex değerinden hemen sonra satırın bitmesi şart koşulur.

4. **`m.group(1)`:** Tüm `show version` çıktısı taranarak tek bir regex sorgusuyla `'0x2102'` değeri çekilmiş olur.

> * *anchor* → aramanın konumunu satır başına (`^`) veya satır sonuna (`$`) sabitleyen çıpa simgesi.
> * *re.MULTILINE (re.M)* → `^` ve `$` çıpalarının tüm string yerine satır bazlı (`line-by-line`) çalışmasını sağlayan bayrak.
> * *line-by-line matching* → çok satırlı metinlerde her `\n` karakterinin yeni bir satır başı/sonu kabul edilerek taranması. 

---
