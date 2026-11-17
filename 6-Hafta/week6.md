## 1. Giriş: Table of Contents

Lesson 6 kapsamında Python'da modüler programlamanın temel taşı olan **Functions** ve tek satırlık anonim fonksiyon yapıları olan **Lambda Expressions** konuları ele alınmaktadır.

Kirk Byers bu derste sırasıyla aşağıdaki konuları işleyeceğini belirtmektedir:

* **Functions:** Fonksiyonların tanımlanması, parametre aktarımı, değişken kapsamları ve yeniden kullanılabilir kod blokları inşa etme ilkeleri.
* **Lambda Expressions:** Kısa ve isimsiz fonksiyon ifadelerinin yazım kuralları ve kullanım alanları.

> * *function* → bir kez yazılıp programın farklı noktalarında defalarca çağrılabilen yeniden kullanılabilir kod bloğu. 
> * *def keyword* → Python'da yeni bir fonksiyon tanımlamasını başlatan anahtar kelime.
> * *parameters* → fonksiyon tanımında parantez içine yazılan ve sadece fonksiyon içinde geçerli olan local değişkenler.
> * *return statement* → fonksiyonun ürettiği sonucu çağrıldığı noktaya geri döndüren ifade.

---

## 2. Function Basics: Temel Kavramlar ve Sözdizimi

Kirk Byers, programlamanın sunduğu iki büyük güce dikkat çekerek fonksiyonların neden vazgeçilmez olduğunu açıklamaktadır:

---

### 2.1 Neden Fonksiyon Kullanırız? Kodun Yeniden Kullanılabilirliği

Programlama öğrenirken ilk kazanılan yetenek, manuel olarak yapılan bir görevi kod yazarak otomatikleştirmektir. 
Ancak asıl büyük güç, çözülen bu problemleri farklı senaryolarda da kullanılabilecek **yeniden kullanılabilir yapı taşlarına** dönüştürebilmektir.

* **Bir Kez Yaz, Defalarca Kullan:** Aynı mantığı farklı veriler üzerinde çalıştırmak için kodu kopyalayıp yapıştırmak yerine, o mantığı bir fonksiyon içine hapsedip ihtiyaç duyulan her yerde çağırırız.

* **Araç Kutusu Yaklaşımı:** Oluşturulan her fonksiyon zamanla büyüyen bir kod araç kutusuna dönüşür ve yeni problemleri çözme süresini ciddi oranda kısaltır.

---

### 2.2 Fonksiyon Tanımlama Syntax'ı ve Bileşenleri

Python'da bir fonksiyon oluşturmak ve çalıştırmak için izlenen yapı şu bileşenlerden oluşur:

1. **`def` Anahtar Kelimesi:** Fonksiyon tanımlamasının başladığını belirtir.
   
2. **Fonksiyon Adı:** `def` kelimesinden sonra gelen ve fonksiyonu çağırırken kullanacağımız isimdir.

3. **Parametreler:** Fonksiyon adının yanındaki parantezler içinde tanımlanır. Bu parametreler yalnızca fonksiyonun kendi kapsamı içinde var olan **local değişkenlerdir**. Fonksiyon dışında aynı isimde değişkenler olsa bile birbirlerinden tamamen bağımsızdırlar.

4. **Indented Blok:** İki nokta üst üste `:` işaretinden sonra girintili olarak yazılan ve fonksiyon çağrıldığında çalıştırılacak olan asıl işlemlerdir.

5. **`return` İfadesi:** Fonksiyonun ürettiği değeri dışarıya aktarır. Eğer fonksiyon içinde açıkça bir `return` yazılmazsa, Python varsayılan olarak **`None`** değerini döndürür.

---

#### IPython Uygulaması

Kirk Byers'ın derste gösterdiği yapı ve benim IPython REPL ortamındaki uygulamam:

```python
In [1]: def toplama_function(arg1, arg2, arg3=None):
   ...:     print("Bu bir fonksiyon.")
   ...:     print(f"arg1 değeri --> {arg1}")
   ...:     print(f"arg2 değeri --> {arg2}")
   ...:     return arg1 + arg2
   ...: 

In [2]: toplama_function(10, 20)
Bu bir fonksiyon.
arg1 değeri --> 10
arg2 değeri --> 20
Out[2]: 30
```

* **Tanımlama vs. Çağırma:** `def` bloğu yazıldığında fonksiyon yalnızca belleğe tanımlanır, henüz çalıştırılmaz. Kodun çalışması için `toplama_function(10, 20)` şeklinde argümanlar gönderilerek **çağrılması** gerekir.

* `10` değeri `arg1` parametresine, `20` değeri ise `arg2` parametresine aktarılır. `arg3` için varsayılan değer `None` tanımlandığından çağrı sırasında argüman gönderilmesi zorunlu tutulmamıştır.

> * *reusable code* → bir kez yazıldıktan sonra farklı girdilerle tekrar tekrar kullanılabilen modüler kod yapısı.
> * *local scope* → fonksiyon parametrelerinin ve içeride tanımlanan değişkenlerin yalnızca o fonksiyon sınırları içinde geçerli olması durumu.
> * *implicit return None* → içinde `return` deyimi bulunmayan fonksiyonların Python tarafından otomatik olarak `None` döndürmesi.
> * *function call* → tanımlanmış bir fonksiyonu adı ve parantez içindeki argümanlarıyla tetikleyip çalıştırma işlemi.

---
