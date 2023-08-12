# Spoti Mix Web App

Bu uygulama, Spotify API'sini kullanarak en çok dinlediğiniz sanatçıların rastgele şarkılarından oluşan bir çalma listesi oluşturan bir web uygulamasıdır.


## Gerekli bağlılıkları yükleyin:

```bash
pip install -r requirements.txt
```


## Nasıl Kullanılır

1. Uygulamayı çalıştırın:

```bash
python playlist.py
```

2. Tarayıcınızı açın ve [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine gidin.

3. Ana sayfada, Spotify Developer Hesabınızın istemci kimliği (Client ID) ve istemci sırrını (Client Secret) girin.

4. "Oluştur" düğmesine basarak çalma listesini oluşturun.

5. Eğer istemci kimliği ve sırrı boş geçerseniz, uyarı mesajı alırsınız ve çalma listesi oluşturulmaz.

6. Çalma listesi başarıyla oluşturulduğunda, "Playlist oluşturuldu" mesajı görüntülenir ve **playlist.html** sayfasına yönlendirilirsiniz.

7. Playlist.html sayfasında oluşturulan çalma listesini görebilirsiniz.




