# Network Mühendisleri İçin Python - Türkçe Notlar

[![Status](https://img.shields.io/badge/Status-Devam_Ediyor-green.svg)]()
[![Course](https://img.shields.io/badge/Course-Kirk_Byers_Learning_Python-blue.svg)]()
[![Language](https://img.shields.io/badge/Language-Python_3-yellow.svg)]()

Merhaba! Bu repository, network otomasyonu dünyasına adım atmak isteyen Türk network mühendisleri için Türkçe bir kaynak oluşturmak amacıyla hazırlanmıştır. 

Sanıyorum ki Türkiye'de bu spesifik kursu hafta hafta Türkçe notlandırıp açık kaynak olarak sunan ilk repo. 
Amacım, benimle aynı yoldan geçen veya network otomasyonunu öğrenmek isteyen meslektaşlarıma faydalı bir referans noktası sunmaktır.

## Kurs Hakkında

Bu repodaki notlar ve kodlar, **Twin Bridges Technology** kurucusu ve **Netmiko** kütüphanesinin yaratıcısı olan **Kirk Byers**'ın 10 haftalık e-posta tabanlı [Learning Python](https://pynet.twb-tech.com/) kursu takip edilerek **15 Eylül** itibarıyla oluşturulmaya başlanmıştır. 

*   **Hedef Kitle:** Temel programlama mantığına aşina, Python öğrenmek isteyen Network Mühendisleri.
*   **Ortam:** Herhangi bir network cihazına (switch/router) bağlanma zorunluluğu yoktur; dersler Python temelleri üzerine kuruludur.
*   **Orijinal Kayıt:** Kursun orijinaline ve güncel İngilizce materyallerine [buradan](https://pynet.twb-tech.com/free-python-course.html) kayıt olabilirsiniz.

### Çalışma Metodolojisi ve İçerik Üretim Süreci

Bu depodaki içerikler, İngilizce bilmeyen veya teknik detayları Türkçe olarak eksiksiz kavramak isteyen networkçüler için şu şekilde hazırlıyorum:

* **Video ve Transkript Analizi:** Kirk Byers'ın e-posta ile paylaştığı ders videoları (Vimeo linkleri) baştan sona izlenmekte, ardından altyazı ve transkript dökümleri çıkarılmaktadır.
  
* **Türkçeleştirme ve Formatlama:** Videolarda anlatılan tüm teorik mantık, Claude/Gemini(öğrenci olduğum için Pro sürümünde genelde onu tercih ediyorum) yapay zeka desteğiyle adım adım Türkçeye çevrilmekte, hiçbir kritik detay atlanmadan `weekX.md` formatında okunabilir ve yapılandırılmış ders notlarına dönüştürülmektedir.
  
* **Uygulamalı Kod ve Egzersizler:** Videolardaki kod örnekleri ve hafta sonu egzersizleri otomatik çeviriye bırakılmadan, **bizzat tarafımdan baştan sona test edilerek çalıştırılmakta** ve çözümleri doğrulanmış kod blokları halinde repoya eklenmektedir.

> Böylece ingilizce seviyeniz ne olursa olsun, kursun orijinal içeriğinden hiçbir şey kaçırmadan doğrudan Türkçe dökümanlar ve çalışan kod örnekleri üzerinden ilerleyebilirsiniz.

---

## Ders Programı ve İlerleme Durumu

Kurs 10 haftalık bir süreci kapsıyor. Tamamlanan haftaların üzerine tıklayarak ilgili dersin Türkçe notlarına ve kodlarına ulaşabileceksiniz:

- [ ] [**Hafta 1: Neden Python?, REPL, ve Strings**](/1-Hafta/week1.md)
  - Python'un özellikleri, Yorumlayıcı Shell, Standart Input/Output, `dir` ve `help` komutları.
- [ ] **Hafta 2: Sayılar, Booleans, Dosyalar, Listeler ve Tuple'lar**
  - Mutable ve Immutable object mantığı.
- [ ] **Hafta 3: Koşullu İfadeler, Döngüler ve List Comprehensions**
  - `if/elif/else`, `for`, `while` döngüleri ve Generator ifadeleri.
- [ ] **Hafta 4: Kümeler (Sets), Dictionaries ve Exceptions**
  - Veri yapıları arasında geçişler, dict kullanımları ve `try/except` blokları.
- [ ] **Hafta 5: Regular Expressions - RegEx**
  - Özel karakterler, Capture Groups, Anchors ve `re` kütüphanesi.
- [ ] **Hafta 6: Fonksiyonlar**
  - Fonksiyon tanımlama ve Lambda ifadeleri.
- [ ] **Hafta 7: Bölüm 1 Classes and Objects**
  - Nesne Yönelimli Programlamaya (OOP) giriş, `__init__` metodu, Attributes ve Metotlar.
- [ ] **Hafta 8:  Bölüm 2 Classes and Objects**
  - Data Class'lar, Kalıtım (Inheritance) ve Kompozisyon.
- [ ] **Hafta 9: Kütüphaneler, Virtual Environments ve pip**
  - `sys.path`, paket yönetimi (`pip`) ve izole Python ortamları yaratma.
- [ ] **Hafta 10: Modules and Packages**
  - `__name__` variable'ı, `main()` fonksiyonu ve kendi Python paketlerimizi oluşturma.

## Yasal Uyarı & Teşekkür

Bu repo tamamen **eğitim ve topluluk paylaşımı** amacıyla kişisel bir çabayla hazırlanmıştır. Kursun fikri mülkiyeti ve orijinal materyalleri **Kirk Byers / Twin Bridges Technology**'ye aittir. Network otomasyonu topluluğuna yaptığı bu devasa katkılardan dolayı Kirk'e teşekkürler.

- BERKAY AĞGÜL
