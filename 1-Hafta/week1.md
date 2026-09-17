## 1. Giriş / Neden Python?

### 1.1 Eğitmen Hakkında 

Kurs, **Kirk Byers** tarafından anlatılıyor. Kendisi uzun yıllardır network engineer olarak çalışıyor ve **CCIE #6243 Emeritus** (Cisco'nun en üst seviye sertifikalarından biri olan CCIE'nin "emeritus" — yani süresi dolmuş ama onurlandırılmış — statüsünde) unvanına sahip. Bu, kendisinin sektörde uzun süredir aktif ve deneyimli olduğunu gösteriyor.

Ayrıca Kirk Byers, network automation dünyasında çok bilinen bir Python kütüphanesi olan **Netmiko**'nun yaratıcısı. 
Netmiko, ağ cihazlarına (router, switch vs.) SSH üzerinden bağlanıp komut çalıştırmayı kolaylaştıran bir kütüphanedir — network automation alanında en çok kullanılan araçlardan biridir. 
Bunun yanı sıra **NAPALM** ve **NORNIR** gibi diğer popüler open source network automation kütüphanelerinin geliştirilmesine de katkıda bulunmuş.

Şu anda ana mesleği, network automation eğitmenliği — hem Python hem de Ansible ve Nornir konularında eğitimler veriyor.

> - *network automation* → ağ cihazlarının konfigürasyon, monitoring ve yönetim işlemlerinin elle/manuel değil, yazılım/script'ler aracılığıyla otomatik yapılması.
> - *open source* → kaynak kodu herkese açık, isteyen herkesin inceleyip katkı sağlayabildiği yazılım.

---

### 1.2 Neden Python? 

Son yaklaşık on yıldır Python, network automation alanında **tercih edilen dil** haline geldi. 
Bu alandaki diğer önemli isim ise **Ansible** — ancak Ansible bir programlama dili değil, daha çok bir **automation framework**: kendi **YAML** tabanlı yapılandırma diliyle çalışan, arka planda genellikle Python kullanan bir araçtır. Yani saf bir **programlama dili** olarak bakıldığında, network automation alanında Python büyük ölçüde baskın hale gelmiştir.

Python'un network mühendisleri için bu kadar popüler olmasının birkaç temel nedeni var:

**1) Geniş destek ve büyük ekosistem**

Python'un çok geniş bir kullanıcı kitlesi ve buna bağlı olarak devasa bir **library** ekosistemi var. Yani hemen her ihtiyaç için (dosya işleme, ağ bağlantısı, veri analizi, API'lerle konuşma vb.) hazır, test edilmiş kütüphaneler bulunuyor — sıfırdan her şeyi yazmaya gerek kalmıyor. Network automation alanında da (Netmiko, NAPALM, Nornir gibi) bu iş için özel olarak geliştirilmiş birçok kütüphane mevcut.

**2) Kolay erişilebilirlik**

Python, işletim sisteminden bağımsız olarak (Windows, macOS, Linux fark etmeksizin) kolayca kurulabilir ve kullanılabilir. Bu **cross-platform** özellik, farklı işletim sistemlerinde çalışan network mühendisleri için büyük bir avantaj.

**3) Başlangıç seviyesinden ileri seviyeye kolay geçiş**

Python, yeni başlayan biri için oldukça basit ve anlaşılır bir dille yazılabiliyor; aynı zamanda deneyim arttıkça çok karmaşık ve gelişmiş uygulamalar geliştirmeye de imkân tanıyor. 
Yani dilin "öğrenme eğrisi" baştan çok dik değil, ama dil sizi sınırlamıyor — basit bir script'ten büyük bir otomasyon sistemine kadar aynı dille ilerleyebiliyorsunuz.

**4) Sürdürülebilirlik**

Python, zamanla üzerinde çalışılması, güncellenmesi ve başkaları tarafından anlaşılması kolay kod yazmaya elverişli bir dil. 
Bunun nedenlerinden biri, dilin çeşitli **abstraction** yani soyutlama mekanizmaları sunması: yani karmaşık işlemleri, tekrar tekrar yazmak yerine fonksiyonlar, class'lar ve modüller hâlinde paketleyip tekrar kullanılabilir hâle getirebiliyorsunuz. Bu da özellikle uzun ömürlü, üzerinde sürekli değişiklik yapılan otomasyon projeleri için çok değerli bir özellik.

**5) High-level dil olması**

Python, **high-level** bir programlama dilidir — yani genellikle bilgisayarın low-level çalışma mekaniğiyle (RAM yönetimi, işlemci detayları gibi) doğrudan uğraşmanıza gerek kalmaz. 
Dil, bu detayları sizin adınıza soyutlar; siz daha çok "ne yapmak istediğinize" odaklanırsınız, "bilgisayarın bunu tam olarak nasıl yaptığına" değil. 
Bu da özellikle otomasyon script'leri yazan network mühendisleri için, öğrenmeyi ve üretken olmayı hızlandıran bir etken.

### Not: 2. Yüklenen Videoda Vimeo Hakkında 1 Dakikalık Kısa Bir Açıklama Vardı, O yüzden 3. Yüklenen Videodan Devam Ediyorum.

---

## 2. Python Ortamı ve Virtual Environment Kurulumu

### 2.1 Eğitmenin Kullandığı Ortam

Eğitmen, derslerdeki kodları göstermek için **Python 3.11.0** sürümünü kullanıyor. 
Kursun ilerleyen kısımlarında küçük güncellemeler olabileceğini ama temel olarak 3.11 sürümü üzerinden ilerleyeceğini belirtiyor. (Bu arada ben 3.13 kullanıyorum.)
Bilgisayarınızda Python 3.11 veya nispeten yeni bir Python 3 sürümü — 3.9, 3.10 gibi — kuruluysa bu eğitim için fazlasıyla yeterli. 
Kurulum için python.org adresine gidip Windows, macOS veya Linux işletim sisteminize uygun paketi indirip kurabilirsiniz.

---

### 2.2 Virtual Environment Nedir ve Neden Kullanılır?

Python dünyasında çalışırken karşımıza çıkan en kritik kavramlardan biri **virtual environment**.

Virtual environment, temelde sisteminizden büyük ölçüde izole edilmiş, kendi içinde bağımsız çalışan küçük bir **sandbox** — yani korunaklı bir çalışma alanı sunar.

Bunun sağladığı en büyük avantajlar şunlardır:

**1) Sistem seviyesinde çakışmaları önlemek**

Gereken bağımlılıkları sadece bu ortama yüklersiniz. Böylece hem işletim sisteminizin genelinde çalışan uygulamaları bozma riskiniz ortadan kalkar hem de sistem düzeyinde yapılan bir güncellemenin sizin projenizi bozmasının önüne geçersiniz.

**2) Proje bazlı bağımlılık yönetimi**

Aynı makinede birden fazla işle uğraşıyor olabilirsiniz. Örneğin API'lerle çalışırken `requests` kütüphanesinin belirli bir sürümüne ihtiyaç duyabilirsiniz; network otomasyonu için ise `netmiko` ve onun gerektirdiği farklı bağımlılıkları kullanmanız gerekebilir. Her iki iş için ayrı sanal ortamlar açarak kütüphane sürümlerinin birbirine girmesini engellersiniz. 
Bu sayede hem ders için temiz bir ortamınız olur hem de diğer projeleriniz bundan etkilenmez.

> * *virtual environment* → işletim sisteminden izole, projeye özel bağımsız Python çalışma alanı.
> * *bağımlılıklar/dependencies* → bir script'in veya projenin çalışabilmesi için dışarıdan ihtiyaç duyduğu paket ve kütüphaneler.
> * *sandbox* → dış dünyayı etkilemeyen ve dışarıdan etkilenmeyen, güvenli ve izole edilmiş çalışma alanı.

---

### 2.3 Linux Ortamında Sanal Ortam Kurulumu

Linux üzerinde sanal ortam oluşturma ve çalıştırma adımları şu şekildedir:

**1) Python sürümünü ve yolunu kontrol etme:**

```bash
berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ which python3.13
/usr/bin/python3.13
```

**2) `venv` modülü ile sanal ortam oluşturma:**

Burada Python'un built-in olan `venv` modülü çağrılır ve ortama bir isim verilir:

```bash
berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ python3.13 -m venv py313_venv

```

**3) Sanal ortamı aktifleştirme:**

Ortamı devreye almak için `bin` klasöründeki `activate` script'i çalıştırılır:

```bash
berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ source py313_venv/bin/activate
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ 
```

Komut çalıştıktan sonra komut satırının başında `[py313_venv]` ibaresi görünür; bu da sanal ortamın başarıyla aktif olduğunu gösterir.

---

### 2.4 Windows Ortamında Sanal Ortam Kurulumu

Windows tarafında süreç çok benzer olsa da komutlarda ufak farklar bulunur. (Bu kısım videodan.)
Windows üzerinde çalışırken Python komutlarını yönetmek için Windows'a özgü **`py` launcher** aracı kullanılır.

**1) Python sürümünü kontrol etme:**

Terminalde doğrudan `py` yazarak doğru sürümün çalıştığından emin olunur:

```cmd
py
```

```text
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

---

**2) Sanal ortam oluşturma:**

Windows için `py` wrapper'ı üzerinden `venv` modülü çalıştırılır:

```cmd
C:\Users\Administrator\VENV>py -m venv py311_venv
```

**3) Sanal ortamı aktifleştirme:**

Windows dosya yapısında sanal ortam script'leri `Scripts` klasörü altındadır:

```cmd
C:\Users\Administrator\VENV>py311_venv\Scripts\activate
```

Aktifleştirme tamamlandığında komut satırının başında `(py311_venv)` görünür. Artık doğrudan `python` komutu verildiğinde bu ortama bağlı 3.11 sürümünün çalıştığı görülür:

```cmd
(py311_venv) C:\Users\Administrator>python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```
---

## 3. PIP ve Dependencies Kurulumu

### 3.1 Kurulu Paketleri Kontrol Etme

Python ve sanal ortam kurulumundan sonra ilk yapılması gereken işlem, ortamda hangi paketlerin yüklü olduğunu kontrol etmektir. Bunun için doğrudan `pip list` komutu kullanılabilir.

Ancak bazen kullandığınız Python sürümü ile sistemdeki `pip` aracı birbiriyle doğrudan eşleşmeyebilir; yani çalıştırdığınız `pip`, o anki Python ortamına ait olmayabilir. Bu durumun önüne geçmek ve en güvenli yoldan ilerlemek için komutu `python -m pip` şeklinde çalıştırmak gerekir:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ python -m pip list
Package Version
------- -------
pip     25.1.1
```

> Alternatif ve güvenli kullanım: `python -m pip list`. Yeni oluşturulan temiz bir sanal ortamda varsayılan olarak yalnızca `pip` ve `setuptools` paketleri yer alır. (Bende setuptools yoktu çıktıdaki gibi.)

---

### 3.2 PIP Aracını Güncelleme 

`pip list` çalıştırdığınızda veya paket yüklemeye çalıştığınızda, pip sürümünüz eskiyse terminalde bir uyarı mesajı çıkabilir ve güncelleme yapmanızı isteyebilir.

Pip'i güncellemek için uyarı mesajında belirtilen en güncel sürüm numarasıyla şu komut çalıştırılır:

```bash
[py311_venv] ktbyers@pydev2 ~/VENV
$ pip install pip==22.3.1
Collecting pip==22.3.1
  Using cached pip-22.3.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3
    Uninstalling pip-22.3:
    Successfully uninstalled pip-22.3
Successfully installed pip-22.3.1
```

> Yine daha güvenli ve tavsiye edilen alternatif yöntem: `python -m pip install pip==22.3.1`. (Bu arada https://pypi.org/project/pip/ - pip 26.2.1 sürümü en son.)

---

### 3.3 Kurs Bağımlılıklarını (requirements.txt) Yükleme

Eğitmenin videolarda gösterdiği kodları ve ortamı birebir uygulayabilmek için dersin ihtiyaç duyduğu bağımlılıkların yüklenmesi gerekir.

Bunun için eğitmenin GitHub deposundaki `requirements.txt` dosyasını temin etmek gerekiyor (ister `git clone` ile tüm depoyu çekerek, ister doğrudan dosyanın içeriğini kopyalayarak):

* **Kursun GitHub Deposu:** [github.com/twin-bridges/learning_python](https://github.com/twin-bridges/learning_python)

Ben yine şuraya da eklemek istiyorum:

```text
ipython==8.6.0
pylama==8.4.1
black==23.3.0
rich==13.3.3
netmiko==4.2.0
emoji==2.2.0
```

İsterseniz uğraşmayın **wget** ile çekin:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ wget https://raw.githubusercontent.com/twin-bridges/learning_python/main/requirements.txt
```

Dosyayı aldıktan sonra projenin ana dizininde şu komut çalıştırılarak dosya içindeki tüm dependencies topluca kurulur:


```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ python -m pip install -r requirements.txt 

Collecting ipython==8.6.0 (from -r requirements.txt (line 1))
  Downloading ipython-8.6.0-py3-none-any.whl.metadata (5.7 kB)
Collecting pylama==8.4.1 (from -r requirements.txt (line 2))
  Downloading pylama-8.4.1-py3-none-any.whl.metadata (15 kB)
...
```

> * *pip* → Python'un resmi paket yönetim aracı; harici kütüphaneleri indirip kurmayı sağlar.
> * *requirements.txt* → bir projenin ihtiyaç duyduğu tüm kütüphanelerin ve sürümlerinin listelendiği standart metin dosyası.
> * *pip install -r* → parametre olarak verilen dosyadaki tüm bağımlılıkları sırayla okuyup kuran komut.

---

## 4. IPython AutoComplete Özelliğini Kapatma

### 4.1 Neden Kapatıyoruz?

Kursun ilerleyen kısımlarında **Python REPL** — yani **Python interpreter shell** olarak **IPython** kullanılacak.

Ancak IPython'ın yeni sürümlerinde kod yazarken sürekli araya giren ve Kirk Byers'ın tabiriyle oldukça kullanışsız olan kötü bir **autocomplete** özelliği bulunuyor. 
Kod yazarken sadece önümüze engel çıkardığı için bu davranışı devre dışı bırakıyoruz.

Bunun için IPython'ın config dosyasına iki satırlık bir ayar eklemek gerekiyor.

> * *IPython* → Python ile etkileşimli çalışmak için kullanılan gelişmiş interpreter shell.
> * *REPL* → Read-Eval-Print Loop; girilen kodu anında çalıştırıp çıktısını veren interaktif ortam.
> * *autocomplete* → kod yazarken otomatik tamamlama ve öneri getiren özellik.

---

### 4.2 MacOS ve Linux Ortamında Yapılandırma

Linux ve macOS sistemlerde ilgili dosya kullanıcının home dizini altındaki `.ipython` klasöründe yer alır.

Düzenlenecek dosya yolu: `~/.ipython/profile_default/ipython_config.py`

Eğer yoksa şu adımları uygulayın:

```bash
berkay@berkay:~$ python -m pip install ipython --break-system-packages
berkay@berkay:~$ ipython profile create
```

Bu dosyanın içerisine şu iki satırı ekliyoruz:

```python
c = get_config()
c.TerminalInteractiveShell.autosuggestions_provider = None
```

Dosyaya eklemenin doğru yapıldığını terminalden `cat` komutuyla kontrol edebiliriz:

```bash
berkay@berkay:~$ cat .ipython/profile_default/ipython_config.py 
```
---

### 4.3 Windows Ortamında Yapılandırma

Windows tarafında eğer bu config dosyası varsayılan olarak henüz oluşturulmadıysa önce terminalden profili oluşturmak gerekiyor. (Bu kısım videodan.)

**1) Default konfigürasyon profilini oluşturma:**

Terminalde sanal ortam aktifken şu komut çalıştırılır:

```cmd
(py311_venv) C:\Users\Administrator\.ipython\profile_default>ipython profile create
[ProfileCreate] Generating default config file: WindowsPath('C:/Users/Administrator/.ipython/profile_default/ipython_config.py')
```

**2) Dosyayı bulma ve düzenleme:**

Oluşan dosya kullanıcının home dizini altındaki `.ipython\profile_default\` klasöründe yer alır. Klasör içeriği `dir` komutuyla kontrol edildiğinde dosya listelenir:

```cmd
(py311_venv) C:\Users\Administrator\.ipython\profile_default>dir
...
11/18/2022  12:31 AM            45,975 ipython_config.py
...
```

Oluşan `ipython_config.py` dosyası bir metin düzenleyiciyle açılır ve Linux tarafında eklenen iki satırın aynısı bu dosyanın içerisine eklenir:

```python
c = get_config()
c.TerminalInteractiveShell.autosuggestions_provider = None
```

Bu ayarlar eklendikten sonra IPython başlatıldığında araya giren o kötü autocomplete davranışı tamamen kapatılmış olur.

---

## 5. REPL and Assignment

### 5.1 Python Interpreter Shell

Python'da kodları doğrudan çalıştırmak, kod parçacıklarını denemek veya hızlıca testler yapmak için **interpreter shell** (REPL) kullanılır.

Kirk Byers bu ortam için standart shell yerine **IPython** (ya da duruma göre `pdb` / `pdbr`) kullanmayı tercih ediyor. Windows, macOS ve Linux fark etmeksizin sanal ortam aktifken doğrudan `python -m IPython` yazılarak interpreter shell başlatılır.

Interpreter shell, yazdığınız kodu anında evaluate eden yani değerlendiren bir ortamdır. 
Burada variable assign edebilir, print statement'lar çalıştırabilir ya da for loop'lar kurabilirsiniz.

Kendi ortamımızda IPython interpreter shell'i başlatma:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ python -m IPython
Python 3.13.5 (main, Aug 10 2026, 12:06:59) [GCC 14.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.6.0 -- An enhanced Interactive Python. Type '?' for help.

```

---

### 5.2 Assignment ve Variable Names

Python'da bir variable'a değer atamak için tek eşittir (`=`) kullanılır; buna **assignment operator** denir.

**1) Assignment işlemi ve type kontrolü:**

```python
In [1]: my_var = 10

In [2]: my_var
Out[2]: 10

In [3]: type(my_var)
Out[3]: int

```

> Atanan değerin türünü görmek için `type()` kullanılır; burada değer bir integer.

**2) Variable isimlendirmede alphanumeric ve alt çizgi kuralı:**

Python'da variable name belirlerken **alphanumeric** karakterler (harf ve sayılar) ile **alt çizgi** (`_`) kullanılabilir. Büyük harf kullanımı da geçerlidir:

```python
In [4]: my_var1 = "test"

In [5]: _my_var2 = "test"

In [6]: my_VAR3 = "test"

```

**3) Sayı ile başlama kuralı:**

Variable name içinde sayı kullanılabilir ama **asla bir sayı ile başlayamaz**. Rakamla başlayan bir variable name girildiğinde Python syntax hatası verir:

```python
In [7]: 4my_var = "test"
  Cell In [7], line 1
    4my_var = "test"
    ^
SyntaxError: invalid decimal literal

```

**4) Convention:**

Python'da genel kural olarak variable isimleri tamamen **lowercase** yazılır ve kelimeleri ayırmak için `_` kullanılır (snake_case). Python bunu zorunlu kılmaz ama topluluk standardı budur:

```python
In [10]: my_ip_addr = "192.168.88.7"

In [11]: sf_dc_svr9 = "svr9a.lasthop.io"

In [12]: global_delay_factor = 4

```

> `sf_dc_svr9` örneğinde görüldüğü gibi, ilk karakter olmadığı sürece variable name içerisinde sayı bulunması tamamen geçerlidir.

---

### 5.3 Özel Anlamı Olan Variable İsimleri

Python'da alt çizgi kullanımı bazı durumlarda özel anlamlar taşır:

**1) Tek başına alt çizgi (`_`):**

Tek başına `_` tamamen valid yani geçerli bir variable name'dir:

```python
In [8]: _ = "geçerli variable"

In [9]: _
Out[9]: 'geçerli variable'

```

Convention olarak tek başına `_`, **ıvır zıvır** ya da **kullanılmayacak** variable'lar için kullanılır. 
Bunun en büyük avantajı **linter** araçlarının hata vermesini engellemesidir. Normalde bir variable tanımlayıp hiç kullanmazsanız linter uyarır, ancak `_` kullanıldığında linter bunu otomatik olarak görmezden gelir.

**2) Tek önde gelen alt çizgi (`_variable`):**

Başında tek alt çizgi olan variable veya method'lar (`_private_var`), kütüphanelerde **private attribute** veya **private method** olduğunu belirtir. 
Yani geliştirici, "ne yaptığını tam bilmiyorsan bunu dışarıdan kullanma" mesajı verir.

**3) Başında çift alt çizgi (`__variable`):**

Başında çift alt çizgi olan durumlar **name mangling** için kullanılır. Kirk Byers pratikte buna neredeyse hiç ihtiyaç duymadığını ve bundan uzak durduğunu belirtiyor.

**4) Çift alt çizgi ile başlayıp bitenler (`__dunder__`):**

Başında ve sonunda çift alt çizgi olan yapılar **Dunder methods** ya da **magic methods** olarak adlandırılır (Dunder = Double Underscore):

```python
In [10]: __name__
Out[10]: '__main__'
```

Bu tarz isimler (`__name__` gibi) Python'un kendi mekanizmalarına ait özel anlamlar taşıdığı için, kendi yazdığınız kodlarda bu formatta variable name tanımlamaktan kaçınmanız gerekir.

> * *assignment operator* → variable'lara değer atamak için kullanılan tek eşittir (`=`) operatörü. 
> * *linter* → kodu convention ve syntax standartlarına göre denetleyen araç.
> * *dunder* → başında ve sonunda çift underscore bulunan (`__name__`, `__init__` vb.) özel Python yapıları.

---

## 6. Python Naming Conventions

Python topluluğunda kod yazarken takip edilen belirli **naming conventions** yani isimlendirme standartları vardır. 
Python bu kuralları default olarak zorunlu kılmaz; ancak genel kabul görmüş bir convention olarak uygulanır.

---

### 6.1 Temel Naming Conventions Kuralları

* **snake_case_lower:** Tamamen lowercase harflerden oluşur ve kelime ayırıcı olarak alt çizgi (`_`) kullanılır. **Variable names** ve **functions** için kullanılır. İçerisinde sayılar yer alabilir; ancak sayılar asla ismin başında bulunamaz.

* **PascalCase:** Kelimelerin büyük harfle ayrıldığı formatıdır. Her kelimenin ilk harfi büyük yazılır (örneğin Pascal'ın P'si ve Case'in C'si gibi) ve kelimeler arasında alt çizgi kullanılmaz. Kursun ilerleyen kısımlarında anlatılacak olan **class names** için kullanılır.

* **SNAKE_CASE_UPPER:** Tamamen uppercase ve kelime ayırıcı olarak alt çizgi kullanılan formattır. **Constants** yani sabit değerler için kullanılır. Python'da default olarak bir şeyi zorla sabit yapacak yerleşik bir kural yoktur; bu tamamen "bu değer sabittir" mesajı veren bir convention olarak kullanılır.

* **self:** Kursun ilerleyen bölümlerinde classes ve objects konularına gelindiğinde görülecektir; method'lar içerisinde objenin kendisine yapılan referansı ifade eder.

* **_ (Tek alt çizgi):** Önceki derste de bahsedildiği gibi, kod içinde kullanılmayacak geçici variable'lar için bir **geçici / atılabilir variable** olarak kullanılır.

> * *naming convention* → dil tarafından zorlanmayan, geliştirici topluluğu tarafından kabul görmüş isimlendirme standartları.
> * *constants* → program akışı boyunca değerinin değişmemesi beklenen sabitler.
> * *geçici / atılabilir variable* → kod içinde atanıp sonrasında okunmayacak, önemsiz geçici variable.

---

## 7. Print ve Input

### 7.1 Printing Standard Output

Python'da **standard output**'a bir veri yazdırmak oldukça basittir; bunun için `print` kullanılır. Ekrana bir string basabileceğimiz gibi, aynı şekilde integer değerleri de yazdırabiliriz.

```python
In [1]: print("Hello World!")
Hello World!

In [2]: print(22)
22
```

---

### 7.2 Reading Standard Input

Kullanıcıdan girdi almak için Python'un **built-in** gelen `input` fonksiyonu kullanılır.

`input()` içerisine yazılan metin kullanıcıya gösterilir ve kullanıcıdan bir değer girmesi beklenir. Girilen değer bir variable'a assign edildiğinde, bu değerin **string** tipinde geldiğine dikkat edilmelidir.

```python
In [3]: my_var = input("Bir IP Adresi gir: ")
Bir IP Adresi gir: 192.168.1.1

In [4]: my_var
Out[4]: '192.168.1.1'
```

> * *standard output (stdout)* → programın çıktılarını ekrana veya terminale yazdırdığı standart çıkış kanalı.
> * *standard input (stdin)* → programın kullanıcıdan klavye veya harici bir girdi yoluyla veri aldığı standart giriş kanalı.
> * *built-in* → Python'un içinde harici bir kütüphane yüklemeye gerek kalmadan varsayılan olarak hazır gelen fonksiyonlar.

---

## 8. Python Karakteristikleri

### 8.1 Indentation Mantığı

Python'da kod blokları süslü parantezler (`{}`) yerine doğrudan **indentation** yani girintileme ile belirlenir. 
Bazı yazılımcılar süslü parantezleri çok sevdiği için Python'ın bu yapısından hoşlanmaz; ancak Python'da blok yapısını kurmanın tek yolu girintilemedir.

Girintileme konusunda dikkat edilmesi gereken kurallar şunlardır:

* **Spaces, not tabs:** Girintileme yaparken tab tuşu yerine mutlaka space kullanılmalıdır.

* **Dört Boşluk Kuralı:** Her girintileme seviyesi için tam olarak **4 space** kullanılmalıdır.

* **Takım Çalışması ve Araç Uyumluluğu:** Boşluk kullanmak, başkalarıyla ortak kod yazarken hayatı kolaylaştırır ve kodun düzgün formatlanıp formatlanmadığını denetleyen linter araçlarıyla sorunsuz çalışmayı sağlar.

* **Editör Ayarı:** Kullandığınız metin editöründe Tab tuşuna basıldığında bunu otomatik olarak 4 space karakterine çevirecek ayarları yapabilirsiniz.

---

### 8.2 Python Standartları ve "Pythonic" Yaklaşım

Python geliştiricileri belirli kurallara ve kodun belli bir biçimde yazılmasına oldukça önem verir.

* **PEP 8:** Python programlarının nasıl stillendirilmesi ve yazılması gerektiğini belirten resmi stil kılavuzudur.

* **Pythonic Code:** Python topluluğunda bir kodun sadece çalışması yeterli görülmez; kodun dile en uygun, sade, açık ve genel kabul görmüş standartlara göre yazılması istenir. Bu yazım tarzına ve felsefesine **pythonic** yaklaşım denir.

> * *indentation* → kod bloklarını ve hiyerarşiyi belirlemek için satır başında bırakılan 4 boşlukluk girinti.
> * *PEP 8* → Python kodunun biçimlendirme ve stil standartlarını tanımlayan resmi rehber.
> * *pythonic* → Python'ın kendine has pratiklerine, temizlik ve okunabilirlik felsefesine uygun kod yazma tarzı.

---

## 9. İlk Python Script'ini Oluşturma ve Çalıştırma

### 9.1 Script Oluşturma

Python'da bir script dosyası oluşturup çalıştırmak oldukça basittir. 
Kirk, `my_code.py` adında bir dosya oluşturarak kullanıcıdan IP adresi alan ve bunu ekrana yazdıran basit bir script yazıyor.

`my_code.py` dosyasının içeriği:

```python
my_ip_addr = input("Enter an IP address: ")

print(my_ip_addr)
```

---

### 9.2 MacOS ve Linux Ortamında Çalıştırma

Linux ve macOS üzerinde bir Python script'ini çalıştırmanın iki farklı yolu vardır:

**1) `python` komutu ile çalıştırma:**

Terminalde sanal ortam aktifken doğrudan dosya adı belirtilerek çalıştırılır:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ python my_code.py 
IP Adresi gir: 192.168.1.1
192.168.1.1
```

**2) Shebang satırı ve direct execution:**

Dosyanın başına `python` yazmadan doğrudan `./my_code.py` şeklinde çalıştırabilmek için iki işlem gerekir:

* **Shebang satırı ekleme:** Dosyanın en üst satırına `#!/usr/bin/env python` satırı eklenir. Bu satır, sistemin `PATH` ortam değişkeninde o an aktif olan Python'ı (yani sistem Python'ı yerine aktif olan virtual environment Python'ını) bulup çalıştırmasını sağlar.

```python
#!/usr/bin/env python

my_ip_addr = input("Enter an IP address: ")

print(my_ip_addr)
```

* **Dosyaya çalıştırma yetkisi verme:** Linux/Unix sistemlerde dosyanın çalıştırılabilmesi için yetkilerinin değiştirilmesi gerekir. `chmod 755` komutu ile dosyaya çalıştırma yetkisi verilir:

```bash
(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ ls -al my_code.py 
-rw-rw-r-- 1 berkay berkay 80 Sep 17 15:02 my_code.py

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ chmod 755 my_code.py 

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ ls -al my_code.py 
-rwxr-xr-x 1 berkay berkay 80 Sep 17 15:02 my_code.py

(py313_venv) berkay@berkay:~/Desktop/Python-All/Python-For-Network-Engineers/Week-1$ ./my_code.py 
IP Adresi gir: 192.168.1.1
192.168.1.1
```

---

### 9.3 Windows Ortamında Çalıştırma

Windows ortamında çalıştırmadan önce virtual environment'ın aktif olduğundan emin olunmalıdır. Windows komut satırında script iki şekilde çalıştırılabilir:

**1) `python` komutu ile:**

```cmd
(py311_test) C:\Users\Administrator\CODE\Lesson1>python my_code.py
Enter an IP Address: 1.2.3.4
1.2.3.4
```

**2) Windows için `py` launcher ile:**

```cmd
(py311_test) C:\Users\Administrator\CODE\Lesson1>py my_code.py
Enter an IP Address: 1.2.3.4
1.2.3.4
```

> * *shebang (`#!`)* → Linux/Unix script'lerinin ilk satırında yer alan ve dosyanın hangi interpreter ile çalıştırılacağını belirten karakter dizisi.
> * *chmod 755* → Linux ve Unix sistemlerde dosya sahibine okuma, yazma, çalıştırma; diğer kullanıcılara ise okuma ve çalıştırma yetkisi veren komut.
> * *direct execution* → script'in başına program adını (`python`) yazmadan, doğrudan `./script.py` şeklinde çalıştırılması.

---
