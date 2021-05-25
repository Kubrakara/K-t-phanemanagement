class musteri():
    ad = ''
    soyad = ''
    password = 12345
    tel = 0
    email = ''
    sec = ''
    menu = ''
def kayit_ol():
    musteri.ad = input("isminiz:\n")
    musteri.soyad = input("Soyad:\n")
    musteri.tel = input('Telefon no :\n')
    musteri.email = input('Email : \n')
    musteri.menu = input("")

def kitap_ekle():

def tum_uye():

def sisteme_giris():
        musteri.ad = input("Isim giriniz: ")  # if id ile dogurlanirsa giris
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

