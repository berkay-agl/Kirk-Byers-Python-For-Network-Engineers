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
