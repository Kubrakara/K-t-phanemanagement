class musteri():
    yeni_uye = {}
    ad = ''
    soyad = ''
    password = 12345
    sec = ''
    menu = ''
    i=0
    kitaplar = {}
    kategori = ''
    uyeler = ''
    new = ''

def kayit_ol():
    yeni_uye = {}
    for musteri.i in range(0, len(yeni_uye)):
        musteri.ad = input("Adınız: ")
        musteri.soyad = input("Soyadınız: ")
        musteri.yeni_uye.setdefault(musteri.ad, musteri.soyad)
    print(musteri.yeni_uye)
    musteri.yeni_uye = musteri.new
    musteri.uyeler = open("uyeler.text", "a")
    musteri.uyeler.write(musteri.new)

def kitap_ekle():
    musteri.kitaplar = {}
    for musteri.i in range(0,len(musteri.kitaplar)):
        musteri.kategori = input("Yeni kategori ekleyiniz: ")
        musteri.kitapadi = input("Kitap adini giriniz: ")
        musteri.kitaplar.setdefault(musteri.kategori,musteri.kitapadi)
    print(musteri.kitaplar)
    kitaplarr = open("kitaplar.text", "a")
    kitaplarr.write(musteri.kitaplar)

def tum_uye():
    print(musteri.yeni_uye)
    uyeler = open("uyeler.text", "a")
    uyeler.write(musteri.yeni_uye)

def sisteme_giris():
        musteri.ad = input("Isim giriniz: ")
        musteri.password = input("Sifrenizi Giriniz:")  # if sifre suysa kabul
        musteri.soyad = input("Soyadinizi Giriniz: ")
        while():
            if (musteri.password == True):
                musteri.sec = input("Kitap eklemek icin 'E', Tüm üyeler görüntülemek için 'T', Çıkış 'Q' ")

                if musteri.sec == 'E':
                    kitap_ekle()
                elif musteri.sec == 'T':
                    tum_uye()
                elif musteri.sec == 'Q':
                    break

