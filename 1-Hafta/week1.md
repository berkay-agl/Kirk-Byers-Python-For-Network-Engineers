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
