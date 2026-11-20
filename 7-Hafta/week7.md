# Lesson 7 Hakkında

**Lesson 7**'de (Classes and Objects: Part 1), Python'da yeniden kullanılabilir kod blokları oluşturmanın ikinci ve en temel yolu olan **Classes** ve **Objects** konusuna giriş yapılmaktadır. 
Bu dersin ilk bölümünde, fonksiyon tabanlı yaklaşımlardaki "**shared data**" probleminin object-oriented yaklaşımla nasıl çözüldüğü ve class taslaklarının (**blueprint**) çalışma mantığı ele alınmıştır.

---

## 1. Giriş: Table of Contents

Ders kapsamında işlenecek temel başlıklar şunlardır:

1. **Overview** (Genel Bakış ve Kullanım Amacı)
2. **Dunder-Init** (`__init__` Constructor Metodu)
3. **Attributes** (Nitelikler / Öznitelikler)
4. **Creating Objects** (Object Oluşturma Süreci)
5. **Methods** (Metotlar)
6. **Static Methods** (Statik Metotlar)

> * **class** → Object'lerin yapısını ve hangi method'lara sahip olacağını belirleyen taslak (blueprint).
> * **object** → Bir class'tan türetilen, bellekte yaşayan ve kendi verilerini (attributes) tutan yapı.
> * **method** → Bir class içinde tanımlanan ve o object'in verileri üzerinde işlem yapan fonksiyon.
> * **shared state / shared data** → Birden fazla fonksiyonun veya işlemin ortaklaşa erişip kullandığı durum bilgisi ve veriler.

---

## 2. Classes ve Objects: Neden Kullanırız?

Python'da daha önce yeniden kullanılabilir kod blokları oluşturmak için **functions** kullandık. Class'lar ve object'lar ise bize bu alanda ikinci bir yapı taşı sunar.

### 2.1 Fonksiyonlardaki "Shared Data" Problemi

Sadece fonksiyonları kullandığımız senaryolarda, aynı veriyi veya durumu birden fazla fonksiyon arasında sürekli olarak argüman olarak taşıdığımızı fark ederiz.

Örneğin, bir ağ cihazına **Telnet** üzerinden bağlanıp okuma (`read`), yazma (`write`) ve oturum açma (`login`) işlemleri yapan üç farklı fonksiyonumuz olsun:

```python
def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = tn.read_very_eager().decode()
    return data

def write(telnet_conn, data):
    byte_data = data.encode()
    telnet_conn.write(byte_data)

def login(telnet_conn, username, password):
    debug = False
    prompt_terminator = r"#"
```

Yukarıdaki yapıda dikkat çeken temel durumlar şunlardır:

* Her üç fonksiyonun da ilk argümanı aynıdır: `telnet_conn` (Telnet bağlantı object'i).

* Cihazla etkileşime geçecek hemen her fonksiyon bu bağlantıya ihtiyaç duyar.

* Sonuç olarak elimizde **shared data** (`telnet_conn`) ve bu ortak veriyi kullanan bir dizi fonksiyon vardır.

> **Temel Problem:** Aynı argümanı veya veri kümesini fonksiyonlar arasında sürekli olarak elden ele geçirmek kod tekrarını artırır ve yönetimi zorlaştırır. Class'lar ve object'ler tam olarak bu problemi çözmek için tasarlanmıştır. 

### 2.2 Object ve Method Çözümü 

Class'lar ve object'lar kullanıldığında, veriyi dışarıdan fonksiyonlara sürekli parametre olarak göndermek yerine şu mimariye geçilir:

1. **Objects (Shared data taşıyan konteynerler):** Paylaşılan verileri (örneğin `host`, `username`, `password` ve `telnet_conn`) içinde tutan, bellekte yer kaplayan bir veri konteyneri oluşturulur.

2. **Methods (Shared data hakkında bilgi sahibi olan fonksiyonlar):** Bu konteynerin sahip olduğu verilere doğrudan erişebilen ve bunlar üzerinde işlem yapan fonksiyonlar (class içindeki adıyla **metotlar**) tanımlanır.

Bu yapı kurulduğunda veriler doğal olarak object'e bağlı hale gelir. Metotlar, object'i doğrudan tanıdığı için paylaşılan verilere ekstra parametre geçirmeye gerek kalmadan doğrudan erişebilir.

---

## 3. Class Tanımlama: Blueprint Mantığı

Class ve object oluşturma süreci birbirinden bağımsız iki aşamadan meydana gelir: **Class Tanımlama (Blueprint)** ve **Object Türetme (Instantiation)**.

```python
class TelnetConn:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self.host)

    def write(self, data):
        byte_data = data.encode()
        self.telnet_conn.write(byte_data)
```

### Blueprint ve Object Yaşam Döngüsü Kuralları

* **Blueprint (Taslak):** `class TelnetConn:` bloğu tek başına çalışan bir bağlantı değildir; object'lerin nasıl oluşturulacağını (genellikle `__init__` metodu ile) ve oluşturulan her object'in hangi yeteneklere (metotlara, örneğin `write`) sahip olacağını belirleyen bir şablondur.

* **Eşzamanlı Çoklu Object:** Class tanımından bağımsız olarak, bu taslak çağrılarak 1, 5 veya 100 farklı object üretilebilir.

* **Bağımsız Yaşam Süresi:** Oluşturulan bu object'lerin hepsi bellekte **aynı anda** var olabilir. Yeni bir bağlantı object'i oluşturmak için önceki object'i kullanıp yok etmeye gerek yoktur; her cihaz bağlantısı kendi verilerini izole bir şekilde kendi konteynerinde tutar.

> * **blueprint** → Object'lerin oluşturulma kurallarını ve sahip olacağı metotları belirleyen class tanımı. 
> * **`__init__`** → Bir class'tan yeni bir object türetildiğinde, o object'in başlangıç verilerini (attributes) hazırlayan özel metot.
> * **concurrent objects** → Aynı class taslağından üretilmiş ve bellekte aynı anda birbirinden bağımsız olarak yaşayabilen object'ler.

---

## 4. Class Syntax ve `__init__` (Dunder-Init)

Bir class tanımlarken, oluşturulacak object'lerin blueprint'ini ve sahip olacağı method'ları belirli kurallara göre yazarız.

```python
class TelnetConn:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self.host)
```

### 4.1 Class Tanımlama Kuralları

* **`class` Keyword ve İsimlendirme:** Class tanımı `class` anahtar kelimesi ile başlar. İsimlendirme standardı olarak **PascalCase** kullanılır; yani her kelimenin ilk harfi büyük yazılır, geri kalan harfler küçük olur ve kelimeler arasında alt çizgi (`_`) kullanılmaz.

* **Inheritance ve Parantezler:** Class isminden sonra parantez açılarak hangi class'tan inheritance yani kalıtım alınacağı belirtilebilir. Ancak başka bir class'tan inheritance alınmıyorsa, Python'daki temel `object` yapısından varsayılan olarak inheritance alındığı için parantez yazmaya gerek yoktur ve doğrudan `:` (iki nokta) ile blok başlatılır.

* **Method Syntax'ı:** Class içerisindeki method'lar, normal fonksiyonlarla tamamen aynı şekilde `def` anahtar kelimesi ile tanımlanır.

### 4.2 `__init__` Method'u ve Attribute Bağlama 

İki alt çizgi ile başlayıp iki alt çizgi ile biten `__init__` (dunder-init), yeni bir object bellekte oluşturulduktan hemen sonra Python tarafından otomatik olarak çağrılan özel initialization yani başlatma method'udur.

* **`self` Parametresi:** `__init__` (ve diğer tüm standart method'ların) ilk parametresi neredeyse her zaman `self` olur. `self` dışındaki diğer parametreler (`host`, `username`, `password`) normal fonksiyon kurallarına tabidir ve default değerler alabilir.

* **Argümanları Object'e Bağlama:** `__init__` içerisindeki en temel işlem, dışarıdan gönderilen argümanları bellekteki object'in kendisine bağlamaktır. Bunun için **dot notation** (`self.host = host`) kullanılır.

* **Attributes Yapısı:** `self.host`, `self.username` ve `self.password` ifadeleri, bellekteki object'in üzerine yapıştırılmış değişkenler (**attributes**) gibidir. Dışarıdan bu verilere erişmek için object referansı üzerinden `tc.host` veya `tc.username` şeklinde nokta notasyonu kullanılır.

* **Ek Başlatma İşlemleri:** `__init__` içerisinde sadece dışarıdan gelen argümanları bağlamakla kalmayıp, `self.telnet_conn = Telnet(self.host)` örneğinde olduğu gibi uzak sisteme doğrudan bağlantı başlatan yeni attribute'ler de oluşturabiliriz.

> * **PascalCase** → Class isimlendirmelerinde kullanılan, kelimelerin ilk harfinin büyük yazıldığı ve alt çizgi içermeyen yazım standardı.
> * **`__init__` (dunder-init)** → Object bellekte oluşturulduktan hemen sonra çalışan ve object'in başlangıç attribute'lerini hazırlayan özel method.
> * **attribute** → Bir object'e nokta notasyonu ile bağlanan ve o object'in durumunu tutan değişken.

---

## 5. Object Oluşturma Süreci

Tanımladığımız class blueprint'ini kullanarak gerçek bir object oluşturmak için class adını tıpkı bir fonksiyon gibi çağırır ve `__init__` method'unun beklediği argümanları göndeririz.

```python
tc = TelnetConn(
    host="host1.domain.com",
    username="admin",
    password="cisco123",
)
```

> **Kritik Python Kuralı:** Object oluştururken parantez içine kesinlikle `self` argümanı **gönderilmez**. `self` referansı Python tarafından arka planda otomatik olarak geçirilir. Diğer tüm argümanlar (`host`, `username`, `password`) fonksiyonlarda olduğu gibi positional, named veya ikisinin karışımı şeklinde gönderilebilir.

### 5.1 Arka Planda `self`, `__new__` ve `__init__` Akışı

Python'da `tc = TelnetConn(...)` satırı çalıştırıldığında bellekte şu adımlar sırasıyla gerçekleşir:

1. **`__new__` Çağrısı:** Python ilk olarak arka planda built-in `__new__` method'unu çağırır. Bu method bellekte boş bir object konteyneri ayırır (genellikle müdahale edilmez ve yeniden yazılmaz).

2. **`__init__` Çağrısı ve `self` Aktarımı:** Python hemen ardından `__init__` method'unu çağırır ve bellekte az önce oluşturduğu o object'in referansını ilk argüman olarak (`self` değişkenine bağlayarak) içeri gönderir. İlk parametrenin adının `self` olması zorunlu bir syntax kuralı değil, çok güçlü bir topluluk standardıdır.

3. **Referans Eşleşmesi (`self` ve `tc`):** `__init__` içindeki tüm atamalar tamamlandığında, dışarıdaki `tc` değişkeni bellekteki aynı object'i işaret etmeye başlar. Yani class içindeki `self` ile dışarıdaki `tc` bellekteki birebir aynı konteynere referans verir.

4. **Verilere Erişim:** İşlem bittiğinde `tc.host` (`"host1.domain.com"`), `tc.username` (`"admin"`), `tc.password` (`"cisco123"`) ve `tc.telnet_conn` attribute'leri üzerinden object'in verilerine doğrudan erişilebilir.

### 5.2 Aynı Anda Birden Fazla Object Yaşatmak

Aynı class blueprint'ini kullanarak bellekte aynı anda birbirinden tamamen bağımsız birden fazla object oluşturabiliriz:

```python
tc1 = TelnetConn(
    host="host1.domain.com",
    username="admin",
    password="cisco123",
)

tc2 = TelnetConn(
    host="host2.domain.com",
    username="admin",
    password="cisco123",
)
```

* `tc1` ve `tc2` aynı `TelnetConn` blueprint'ini kullanır ancak bellekte tamamen farklı iki ayrı object konteynerini işaret eder.

* Tıpkı listeler ve dictionary'ler gibi object'ler de uzun ömürlüdür ve kod çalıştığı sürece bellekte aynı anda varlıklarını sürdürürler.

> * **`__new__`** → Python'da object oluşturma sürecinin en başında çalışan ve bellekte boş object konteynerini yaratan built-in method.
> * **`self`** → Class içerisindeki method'lara ilk argüman olarak otomatik gönderilen ve bellekteki o anki object'i işaret eden referans.
> * **dot notation** → Object'lerin sahip olduğu attribute veya method'lara `object.attribute` şeklinde erişim sağlayan nokta yazımı.

---
