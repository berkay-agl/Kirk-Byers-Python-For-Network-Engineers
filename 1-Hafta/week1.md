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

# Not: 2. Yüklenen Videoda Vimeo Hakkında 1 Dakikalık Kısa Bir Açıklama Vardı, O yüzden 3. Yüklenen Videodan Devam Ediyorum.
