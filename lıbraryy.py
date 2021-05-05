import random
ad = 0
soyad = 0
password = 0
def kayit_ol():
    ad = input("isminiz:\n")
    soyad = input("Soyad:\n")
    tel = input('Telefon no :\n')
    email = input('Email : \n')

    return ad, soyad, tel, email

# ID bilgisi atama     #    no = print(random.randint(1, 100000))
#    print("ismim"+ ad + "dir")
#   print(ad +' '+ soyad +' '+ "Oluşturulan ID:"+ No)




def sisteme_giris():
    print("Isim giriniz: ")# if id ile dogurlanirsa giris
    password = print("Sifrenizi Giriniz:")#if sifre suysa kabul
    return password





print("----Kütüphane Yönetim Sistemine Hoşgeldiniz----")
sorgu = int(input("Sisteme Kayit olmak icin (1) - Sisteme Giris icin (2)\n"))
if(sorgu == 1):
    kayit_ol()
#if(sorgu == 2):
#    sisteme_giris()















"""
seç = int(input('Enter your choice ...: '))

if seç == 1:
    add_book()
if seç == 2:
    add_member()
if seç == 3:
    modify_book()
if seç == 4:
    modify_member()
if seç == 5:
    issue_book()
if seç == 6:
    return_book()
if seç == 7:
    search_menu()
if seç == 8:
    report_menu()
if seç == 9:
    special_menu()
if seç == 0:
    break
"""





