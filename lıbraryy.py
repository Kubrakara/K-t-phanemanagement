import random
import modul



print("----Kütüphane Yönetim Sistemine Hoşgeldiniz----")
while True:
    sorgu = int(input("Sisteme Kayit olmak icin (1) - Sisteme Giris icin (2)\n"))
    if(sorgu == 1):
        modul.kayit_ol()
    elif(sorgu == 2):
        modul.sisteme_giris()
    else:
        break

































