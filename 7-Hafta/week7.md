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
