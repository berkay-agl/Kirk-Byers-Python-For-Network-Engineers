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
