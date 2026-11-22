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

## 6. Methods (Metotlar)

Class'ların ve object'lerin bir diğer temel parçası, oluşturduğumuz object'ler üzerinde gerçekleştirebileceğimiz eylemlerdir. 
Bu eylemlere **Methods** adı verilir. En basit tanımıyla method'lar, bir class bağlamı içerisine yerleştirilmiş fonksiyonlardır.

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

    def read(self, sleep=1.5):
        time.sleep(sleep)
        data = self.telnet_conn.read_very_eager().decode()
        return data

    def login(self):
        debug = False
        prompt_terminator = r"#"
```

### 6.1 Method Syntax ve Çalışma Kuralları

Standart method'ların yazım kuralları `__init__` ve normal fonksiyonlarla aynı temele dayanır:

* **`def` Keyword ve İsimlendirme:** Method tanımları `def` anahtar kelimesi ve method adı ile başlar.

* **`self` Parametresi:** Standart class method'larında ilk parametre her zaman `self` olarak tanımlanır. `self`, method içerisinden o object'e bağlı tüm attribute'lere (`self.telnet_conn`, `self.username`, `self.password`) erişmemizi sağlar.

* **Ek Parametreler ve Default Değerler:** `self` sonrasında tıpkı normal fonksiyonlarda olduğu gibi ek parametreler alabilir (`data`) ve bu parametrelere varsayılan değerler (`sleep=1.5`) atanabilir.

* **Nested Object Erişimi:** `self.telnet_conn` attribute'ü, Python'ın `telnetlib` kütüphanesinden türetilmiş kendi başına ayrı bir Telnet object'idir. Bu nedenle method içerisinde `self.telnet_conn.write(byte_data)` veya `self.telnet_conn.read_very_eager()` yazarak o alt object'in kendi method'larını da çağırabiliriz.

* **`return` Davranışı:** Method'lar tıpkı fonksiyonlar gibi `return` ifadesi ile dışarıya veri döndürebilir (`read` method'unun okuduğu metni döndürmesi gibi). Eğer açıkça bir `return` yazılmazsa (`write` method'undaki gibi), Python arka planda örtük olarak `None` döndürür.

### 6.2 Method'ların Kullanılması: Tekil ve Ardışık Çağrılar

Tanımlanan method'ları çağırmak için oluşturulmuş object değişkeni üzerinden **dot notation** ve parantez (`object_name.method_name()`) kullanılır.

#### Tekil Method Çağrısı ve İlk Okuma

İlk olarak bir `TelnetConn` object'i oluşturup tek başına `tc1.read()` method'unu çağırdığımızda cihazdan ilk gelen karşılama verisini alırız:

```python
tc1 = TelnetConn(
    host=host1,
    username=username,
    password=password,
)
data = tc1.read()
print(data)
```

Bu kod çalıştırıldığında elde edilen terminal çıktısı:

```bash
Enter router password:

User Access Verification

Username:
```

#### Ardışık Method Çağrıları ile Oturum Açma

Birden fazla `read()` ve `write()` çağrısını art arda kullanarak router'a kullanıcı adı ve parola gönderip oturum açabiliriz:

```python
tc1 = TelnetConn(
    host=host1,
    username=username,
    password=password,
)
data = tc1.read()
tc1.write(f"{username}\n")
data += tc1.read()
tc1.write(f"{password}\n")
data += tc1.read()
print(data)
```

Bu kod çalıştırıldığında tüm çıktının birikmiş hali ekrana yazdırılır:

```bash
Enter router password:

User Access Verification

Username: pyclass
Password:

cisco1#
```

### 6.3 Adım Adım Okuma Dökümü

Yukarıdaki ardışık çağrıların her bir `read()` adımında tam olarak ne okuduğunu izole edip görmek için `read_number` sayacı ile adım adım analiz yapabiliriz:

```python
tc1 = TelnetConn(
    host=host1,
    username=username,
    password=password,
)

read_number = 1
data = tc1.read()
print(f">>> {read_number=}")
print(data)
print(">>>")
tc1.write(f"{username}\n")
data = tc1.read()
read_number += 1
print(f">>> {read_number=}")
print(data)
print(">>>")
tc1.write(f"{password}\n")
data = tc1.read()
read_number += 1
print(f">>> {read_number=}")
print(data)
print(">>>")
```

Bu kod çalıştırıldığında elde edilen terminal çıktısı:

```bash
Enter router password:
>>> read_number=1

User Access Verification

Username:
>>>
>>> read_number=2
pyclass
Password:
>>>
>>> read_number=3

cisco1#
>>>
```

Yukarıdaki çıktıda her bir okuma adımının cihaz tarafındaki karşılığı şu şekildedir:

1. **`tc1.read()` (`read_number=1`):** Cihaza ilk bağlanıldığında gelen karşılama ekranını ve kullanıcı adı istemini (`User Access Verification` ve `Username:`) okur.

2. **`tc1.write(f"{username}\n")` ve `tc1.read()` (`read_number=2`):** Kullanıcı adını kanala gönderir. İkinci okuma, gönderdiğimiz kullanıcı adının ekrana yansıyan yankısını (echoed username: `pyclass`) ve hemen ardından gelen `Password:` istemini yakalar.

3. **`tc1.write(f"{password}\n")` ve `tc1.read()` (`read_number=3`):** Parolayı kanala gönderir. Güvenlik nedeniyle parola cihaz tarafından ekrana geri yansıtılmaz (echo edilmez); üçüncü okuma doğrudan oturumun açıldığını gösteren router prompt'unu (`cisco1#`) döndürür.

### 6.4 Method İçinden Başka Method'ları Çağırmak

Bir class method'u kendi içerisinden, `self` referansını kullanarak aynı class'a ait diğer method'ları çağırabilir. 
Böylece tüm oturum açma etkileşimini tek bir `login()` method'u içerisine sarabiliriz:

```python
    def login(self):
        debug = False
        prompt_terminator = r"#"

        data = self.read()
        output = data
        if re.search(r"sername", data):
            self.write(self.username + "\n")
            data = self.read()
            output += data
        if re.search(r"ssword", data):
            self.write(self.password + "\n")
            data = self.read()
            output += data

        if debug:
            print(output)

        if re.search(prompt_terminator, data):
            return True
        else:
            return False
```

* **Nested Method Çağrısı:** `login` method'u içerisinde `self.read()` ve `self.write(...)` çağrıları yapılarak okuma-yazma adımları otomatize edilir.

* **Object Attribute'lerinin Kullanımı:** Method içerisinde dışarıdan tekrar kullanıcı adı veya parola almaya gerek kalmadan, object oluşturulurken bağlanan `self.username` ve `self.password` attribute'leri doğrudan kullanılır.

* **Basitleştirilmiş Kullanım:** Tüm oturum açma mantığı `login` içerisine sarıldığı için dışarıdaki kullanım artık sadece şu iki adıma iner:

```python
tc1 = TelnetConn(
    host=host1,
    username=username,
    password=password,
)
tc1.login()
```

> * **method** → Bir class içerisinde tanımlanan, ilk parametresi `self` olan ve object'in attribute'leri ile diğer method'larına erişebilen fonksiyon.
> * **`self.method()`** → Bir method'un kendi içerisinden aynı object'e ait başka bir method'u çağırma yöntemi.
> * **implicit `None**` → İçerisinde `return` ifadesi bulunmayan method'ların çalışması bittiğinde Python tarafından otomatik döndürülen değer.

---

## 7. Static Methods (Statik Metotlar)

Class'lar ve object'ler ile çalışırken bazen sınıfın konusuyla ilişkili bir işlem yapmak isteriz ancak bu işlem sırasında bellekteki object'e veya o object'in verilerine (`self`) **hiç ihtiyaç duymayız**.
Yani class yapısı içerisinde duran ancak tıpkı bağımsız bir fonksiyon gibi çalışan yapılara ihtiyaç duyarız.

```python
@staticmethod
def ornek_method(arg1="Nasılsın?"):
    print(arg1)
```

### 7.1 `@staticmethod` Decorator ve Syntax Kuralları

Bir method'u static method olarak tanımlamak için Python'ın built-in decorator mekanizması kullanılır:

* **`@staticmethod` Decorator:** Method tanımının hemen bir üst satırına `@staticmethod` ifadesi yazılır. Herhangi bir modül veya kütüphane `import` etmeye gerek yoktur; Python'ın built-in bir özelliğidir.

* **`self` Parametresinin Olmaması:** Standart method'ların aksine parametre listesinde `self` referansı yer almaz. Python bu method çağrıldığında ilk argüman olarak object referansını içeri geçirmez; method yalnızca tanımlanan standart parametreleri alır.

* **Decorator Mantığı:** Decorator'lar, fonksiyonların veya method'ların varsayılan davranışlarını değiştiren özel düzenleyicilerdir. `@staticmethod` decorator'ı, normalde ilk argüman olarak `self` bekleyen bir class method'unun bu varsayılan davranışını değiştirerek onu `self` almayan bir yapıya dönüştürür.

### 7.2 Object'e İhtiyaç Duyulmadığında 3 Tasarım Seçeneği

Bir class ile ilişkili bir eylem gerçekleştirirken `self` referansına ihtiyaç duymadığımız durumlarda önümüzde üç farklı mimari seçenek bulunur:

#### Seçenek 1: Class Dışında Standart Fonksiyon Kullanmak

İşlemi class blueprint'inin tamamen dışında bağımsız bir Python fonksiyonu olarak tanımlayıp doğrudan çağırmak:

```python
def ornek_func(param):
    print("Merhaba")
```

#### Seçenek 2: `self` İçeren Ama Kullanmayan Standart Method Yazmak

İşlemi class blueprint'i içerisinde normal bir method olarak tanımlamak, parametre listesine `self` eklemek ancak method gövdesinde `self` referansını hiç kullanmayıp tamamen görmezden gelmek:

```python
class MyClass:
    def ornek(self, param):
        print("Merhaba")
```

#### Seçenek 3: `@staticmethod` Kullanmak

İşlemi class blueprint'i içerisinde tutmak ancak `@staticmethod` decorator'ı kullanarak `self` referansını tamamen ortadan kaldırmak:

```python
class MyClass:
    @staticmethod
    def ornek(param):
        print("merhaba")
```

### 7.3 Seçenekler Arası Karşılaştırma ve Mimari Tercihler

#### Neden Standart Method Yerine Static Method Seçilir? (Seçenek 3 vs. Seçenek 2)

Class hiyerarşisi içinde kalmaya karar verdiğimizde, kullanılmayan bir `self` parametresi tutmak yerine static method kullanmanın iki temel avantajı vardır:

1. **Daha Temiz Kod:** İçeride hiç kullanılmayacak bir `self` parametresini tanımlamak hem kod okunabilirliğini bozar ("Bu `self` burada neden var?") hem de linter araçlarının kullanılmayan değişken uyarıları üretmesine yol açar.

2. **Daha Düşük Kaynak Tüketimi:** Static method'lar, object'e bağlanan standart method'lara kıyasla arka planda çok küçük bir farkla da olsa daha az sistem kaynağı tüketir.

#### Neden Class Dışında Fonksiyon Yerine Static Method Seçilir? (Seçenek 3 vs. Seçenek 1)

Class dışında standart bir fonksiyon yazmak çoğu senaryoda tamamen geçerli bir seçenek olsa da, static method kullanmayı gerektiren iki önemli mimari neden vardır:

1. **Class Hiyerarşisi ve Inheritance:** Farklı ağ cihazı platformları (Cisco IOS, Juniper Junos, Fortinet vb.) için bir base class ve bu base class'tan türeyen alt driver class'ları oluşturduğumuzda, her platformun kendine özgü davranışını alt class içinde ilgili static method'u yeniden yazarak yönetebiliriz. Class dışında standart fonksiyonlar kullansaydık, platform türüne göre doğru fonksiyonu seçmek için `if/elif` bloklarından oluşan ek bir **dispatcher** fonksiyonu yazmak ve class hiyerarşisini manuel olarak taklit etmek zorunda kalırdık:

```python
def dispatcher_func(platform):
    if platform == "cisco_ios":
        return ios_func()
    elif platform == "juniper_junos":
        return junos_func()
    elif platform == "fortinet":
        return fortinet_func()
```

2. **Yapısal Organizasyon:** Halihazırda bir class blueprint'i ve yapısı üzerinde çalışılıyorsa, o class ile doğrudan ilgili yardımcı bir işlemi başka bir dosyaya veya dışarıya taşıyıp tekrar `import` etmek yerine doğrudan kendi class yapısı içinde organize etmek kodu çok daha düzenli hale getirir.

### 7.4 Gerçek Dünya Örneği: Netmiko `BaseFileTransfer`

Network otomasyonu kütüphanesi **Netmiko** içerisinde, Secure Copy (SCP) dosya transferlerini yöneten `BaseFileTransfer` sınıfında uzak cihaza aktarılan dosyanın checksum'unu doğrulamak için `@staticmethod` kullanılır:

```python
    @staticmethod
    def process_md5(md5_output, pattern=r"=\s+(\S+)"):
        """
        Process the string to retrieve the MD5 hash

        Output from Cisco IOS (ASA is similar)
        .MD5 of flash:file_name Done!
        verify /md5 (flash:file_name) = 410db2a7015eaa42b1fe71f1bf3d59a2
        """
        match = re.search(pattern, md5_output)
        if match:
            return match.group(1)
        else:
            raise ValueError(f"Invalid output from MD5 command: {md5_output}")
```

* **Neden `self` Yok?** `process_md5` method'u yalnızca cihazdan dönen metin çıktısını (`md5_output`) alıp regex ile MD5 hash değerini ayıklar. Bağlantı object'ine veya object attribute'lerine (`self`) hiçbir ihtiyacı yoktur.

* **Platforma Göre Tanımlama:** Bu varsayılan davranış Cisco IOS ve Cisco ASA çıktıları (`verify /md5 ... = <hash>`) için geçerlidir. Farklı çıktı formatlarına sahip diğer vendor'lerin alt class'larında bu static method kendi formatlarına göre yeniden tanımlanır.

> * **`@staticmethod`** → Bir class içerisinde tanımlanan ancak object referansı (`self`) almayan ve bağımsız bir fonksiyon gibi çalışan method'ları tanımlayan built-in decorator.
> * **decorator** → Fonksiyon veya method'ların varsayılan çalışma davranışını değiştiren özel yapı.
> * **dispatcher pattern** → Gelen parametreye veya platform türüne göre ilgili alt fonksiyonu koşullu ifadelerle (`if/elif`) seçip yönlendiren fonksiyon yapısı.

---

## 8. Special İsimlendirmeler

Python'da **Properties** konusuna geçmeden önce, class ve object bağlamında kullanılan üç özel isimlendirme kuralını bilmemiz gerekir:

* `_private_attribute` (Tek alt çizgi ile başlayan private attribute'ler)

* `__name_mangled` (Çift alt çizgi ile başlayan name mangling attribute'leri)

* `__magic__` (Başında ve sonunda çift alt çizgi bulunan dunder/magic method'lar)

```python
class NetDevice:
    def __init__(self, device_type, host, username, password, port=22):
        # Name mangling
        self.__device_type = device_type
        self.host = host
        # private attrs (somewhat private)
        self._username = username
        self._password = password
        self.port = port

    def __str__(self):
        return f"NetDevice Object {self.host}:{self.port}"
```

### 8.1 Private Attributes (`_private_attribute`)

Bir attribute adının başına tek bir alt çizgi (`_`) koyduğumuzda (`self._username`, `self._password`), o attribute'ün class'a private olduğunu belirtmiş oluruz.

* **Programlama Niyeti:** Tek alt çizgi ile yapılan bu isimlendirme, diğer geliştiricilere *"Bu attribute class'ın iç işleyişine aittir, dışarıdan doğrudan erişmemelisiniz ve geliştirici istediği zaman bu yapıyı değiştirebilir"* mesajını veren bir niyet beyanıdır.

* **Güvenlik Önlemi Değildir:** Python bu erişimi teknik olarak engellemez; sadece isim değiştiği için doğrudan `nd.username` şeklinde erişmeye çalıştığımızda `AttributeError` alırız, ancak `nd._username` yazdığımızda veriyi yine okuyabilir ve değiştirebiliriz.

```python
nd = NetDevice(
    host="test1.domain.com",
    device_type="cisco_ios",
    username="admin",
    password="cisco123",
)
import pdbr; pdbr.set_trace()
```

`pdbr` debugger üzerinde erişim testi:

```text
(Pdbr) nd.username
*** AttributeError: 'NetDevice' object has no attribute 'username'
(Pdbr) nd._username
'admin'
```

### 8.2 Name Mangling (`__name_mangled`)

Bir attribute adının başına çift alt çizgi (`__`) koyup sonuna çift alt çizgi koymadığımızda (`self.__device_type`), Python **Name Mangling** (isim bozma/değiştirme) davranışını devreye sokar.

* **Otomatik İsim Dönüşümü:** Python, class içerisinde `__device_type` olarak tanımlanan bu attribute'ün adını arka planda otomatik olarak `_ClassName__attribute_name` formatına (`_NetDevice__device_type`) dönüştürür.

* **Python Resmi Dokümantasyon Kuralı:** En az iki başlangıç alt çizgisi ve en fazla bir bitiş alt çizgisi içeren `__spam` biçimindeki herhangi bir tanımlayıcı, metinsel olarak `_classname__spam` biçimiyle değiştirilir (burada `classname`, başındaki alt çizgiler soyulmuş mevcut class adıdır). (Not: Kirk, konuşmasında "double underscore ve ardından orijinal isim" ifadesini kullanırken, orijinal ismin zaten çift alt çizgi içerdiğini hatırlatarak bu ifadeyi notunda ayrıca netleştirmiştir.)

* **Kullanım Amacı:** Yalnızca niyet belirten tek alt çizginin aksine, name mangling Python'ın attribute adını fiziksel olarak değiştirmesi işlemidir. Buradaki temel amaç, bu class'tan türetilecek alt class'ların yanlışlıkla bu attribute'ün üzerine yazmasını yani **override** etmesini engellemektir. Pratikte çok nadir karşılaşılan uç bir özelliktir.

`pdbr` debugger üzerinde name mangling erişim testi:

```text
(Pdbr) nd.__device_type
*** AttributeError: 'NetDevice' object has no attribute '__device_type'
(Pdbr) nd._NetDevice__device_type
'cisco_ios'

```

### 8.3 Magic Methods / Dunder Methods (`__magic__`)

Hem başında hem de sonunda çift alt çizgi bulunan method'lara **Magic Methods**, **Special Methods** veya **Dunder Methods** adı verilir. 
Python'da özel bir anlama sahiptirler ve belirli olaylar gerçekleştiğinde arka planda otomatik olarak çalıştırılırlar.

* **`__init__` (dunder-init):** Yeni bir object oluşturulduğunda otomatik çalışarak object'in başlangıç attribute'lerini hazırlar.

* **`__str__` (dunder-str):** Oluşturulan object `print()` fonksiyonuna verildiğinde veya string'e dönüştürüldüğünde ekrana ne yazdırılacağını belirler. `NetDevice` içerisinde tanımladığımız `__str__` sayesinde `print(nd)` çağrısı doğrudan özelleştirilmiş formatı döndürür:

```text
(Pdbr) print(nd)
NetDevice Object test1.domain.com:22
```

> * **private attribute (`_attr`)** → Başına tek alt çizgi konularak class içi kullanıma özel olduğu belirtilen, ancak teknik bir erişim engeli bulunmayan attribute.
> * **name mangling (`__attr`)** → Başına çift alt çizgi konulan attribute'lerin Python tarafından otomatik olarak `_ClassName__attr` biçimine dönüştürülerek alt class çakışmalarından korunması.
> * **magic / dunder methods (`__method__`)** → Başında ve sonunda çift alt çizgi bulunan, Python tarafından özel durumlarda otomatik tetiklenen built-in method'lar.

---

## 9. Properties (Özellikler)

Class'larımızda başlangıçta standart attribute'ler (`host`, `username`, `password`) tanımlarız; ancak zamanla bu attribute'lere erişildiğinde veya değerleri değiştirildiğinde arka planda ekstra bir eylemin gerçekleşmesini isteyebiliriz.

Yani bir attribute'ün dışarıdan standart bir veri gibi görünmesini, ancak arka planda bir **method** gibi çalışmasını isteriz.

```python
class TelnetConn:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self.host)
```

> **Senaryo:** `host` attribute'üne her erişildiğinde sadece değerinin döndürülmesini değil, aynı zamanda ekrana `"Hello World"` mesajının yazdırılmasını ve ardından `host` attribute değerinin döndürülmesini istiyoruz.

### 9.1 Klasik Çözüm: Getters ve Setters Yaklaşımı

Birçok programlama dilinde bu problem **Getters** (değer okuyan method'lar) ve **Setters** (değer atayan method'lar) pattern'i ile çözülür. Bu yaklaşımda gerçek veri `_host` gibi private bir attribute içerisine gizlenir ve dışarıdan erişim `get_host()` ile `set_host()` method'ları üzerinden sağlanır:

```python
class TelnetConn:
    def __init__(self, host, username, password):
        self._host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self._host)

    def get_host(self):
        print("Hello world")
        return self._host

    def set_host(self, value):
        self._host = value
```

`pdbr` debugger üzerinde getter ve setter davranışı:

```text
(Pdbr) tc.host
*** AttributeError: 'TelnetConn' object has no attribute 'host'
(Pdbr) tc.get_host()
Hello world
'rtr2.lasthop.io'
```

### 9.2 Getters ve Setters Yaklaşımının 2 Büyük Problemi

Python'da getter ve setter method'ları yazmak genellikle tercih edilmeyen bir yöntemdir çünkü iki ciddi soruna yol açar:

1. **Gereksiz Boilerplate Kod:** Sadece ileride ihtiyaç duyulabilir düşüncesiyle her bir attribute (`host`, `username`, `password`) için ayrı ayrı `get_*` ve `set_*` method'ları yazmak ciddi miktarda gereksiz şablon (**boilerplate**) kod üretir.

2. **Mevcut Kodu ve Programatik Arayüzü Kırmak:** Başlangıçta `tc.host` şeklinde doğrudan attribute erişimi sunan bir class veya library sonradan `get_host()` / `set_host()` yapısına geçirilirse, eski arayüzü kullanan tüm dış kodlar bozulur:

* Eski kodlar `tc.host` okumaya çalıştığında `AttributeError` hatası alır.

* Geliştirici `tc.host = "foo"` şeklinde doğrudan atama yapmaya çalışırsa, Python object üzerinde `host` adında yeni ve bağımsız bir attribute oluşturur; içeride kullanılan gerçek `tc._host` attribute'ü (`'rtr2.lasthop.io'`) hiç değişmeden kalır:

```text
(Pdbr) tc.host = "foo"
(Pdbr) tc.host
'foo'
(Pdbr) tc._host
'rtr2.lasthop.io'
```

### 9.3 Python Çözümü: `@property` Decorator

Python bu problemi **Properties** mekanizmasıyla çözer. Properties, veri attribute'lerini aynı programatik arayüzü (`tc.host`) koruyarak getter/setter method'larına dönüştürmemizi sağlar. Böylece en başta gereksiz boilerplate kod yazmadan, sadece gerçekten ihtiyaç duyduğumuz attribute'ü sonradan property'ye çevirebiliriz.

```python
class TelnetConn:
    def __init__(self, host, username, password):
        self._host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self._host)

    @property
    def host(self):
        print("Hello world")
        return self._host
```

#### `@property` Kurulum Adımları

1. **Private Attribute Tanımlama:** `__init__` içerisinde gerçek veriyi tutacak private attribute oluşturulur (`self._host = host`).

2. **Aynı İsimli Method Yazma:** Orijinal attribute ile birebir aynı ada sahip bir method tanımlanır (`def host(self):`).

3. **`@property` Decorator Ekleme:** Method tanımının hemen üstüne `@property` decorator'ı eklenir.

#### Çalışma Davranışı ve Read-Only Özelliği

* **Erişim Anında Otomatik Tetiklenme:** Dışarıdan `tc.host` şeklinde standart attribute erişimi yapıldığında arka plandaki `host(self)` method'u otomatik olarak çalıştırılır:

```text
(Pdbr) tc.host
Hello world
'rtr2.lasthop.io'
```

* **Read-Only Koruma:** Yalnızca `@property` tanımlandığında (henüz bir setter tanımlanmadığında), bu attribute dışarıdan yanlışlıkla değiştirilemeyen **read-only** bir yapıya dönüşür. Dışarıdan değer atamaya çalışıldığında Python doğrudan `AttributeError` fırlatır:

```text
(Pdbr) tc.host = "foo"
*** AttributeError: property 'host' of 'TelnetConn' object has no setter
```

* **Diğer Attribute'lerin İzolasyonu:** `username`, `password` ve `telnet_conn` gibi diğer standart attribute'ler hiçbir değişikliğe uğramadan klasik dot notation ile okunmaya ve değiştirilmeye devam eder.

> * **`@property`** → Bir class method'unu standart bir attribute gibi erişilebilir hale getiren ve programatik arayüzü bozmadan arka planda kod çalıştırmayı sağlayan built-in decorator.
> * **boilerplate code** → Gerçek bir işlevsel karşılığı olmadan yalnızca mimari kalıbı doldurmak için yazılan tekrarlı şablon kod.
> * **read-only property** → Yalnızca `@property` getter'ı tanımlanmış, setter'ı bulunmayan ve dışarıdan üzerine değer yazılmasına izin vermeyen attribute.

---
