kartŞifresi = 0000
bakiye = 1000
login = False

while True:
    if login == False:
        sifre = int(input("Hoşgeldiniz Lütfen Şifrenizi giriniz."))
    if sifre == kartŞifresi:
        login = True
        print("""
1 Para Çekme
2 Para Yarıma
3 Bakiye Sorgulama
4 Kart iade
        """)
        secim = int(input("Hangi işlemi yapmak İstiyorsunuz"))
        if secim == 1:
            miktar = int(input("Miktar Giriniz"))
            if bakiye < miktar:
                print("Yeterli Bakiyeniz bulunmamaktadır.")  
            continue
            bakiye -= miktar
        elif secim == 2:
            miktar = int(input("Kaç TL yatırmak istiyorsunuz"))
            bakiye += miktar
        elif secim == 3:
            print("Bakiyeniz {} TL".format(bakiye))
        elif secim == 4:
            print("İyi günler dileriz.")
            break
        else:
            print("Lütfen 1 ile 4 arasında bir seçim yapınız.")
