import datetime

## Kullanicidan isim, yas ve ogrenim durumu bilgilerini isteyib Jandarma ola bilme durumunu kontrol ediniz
#jandarma ola bilme kosulu ise en az 21 yasinda ve oyrenim durumu orta okul ve ya lise olmalidir 

# isim = input("Lutfen isminizi giriniz: ")
# yas = int(input("Yasinizi giriniz: "))
# oyrenim_durumu = input("Oyrenim durumunuzu giriniz: (Misal: ilk okul, orta okul,lise ve s.) :")

# oyrenim_durum_gecerlilik = ["lise","orta okul"]

# if yas >= 21:
#     if oyrenim_durumu in oyrenim_durum_gecerlilik:
#         print(f"{isim} sizin yas ve oyrenim durumu bilgileriniz jandarma olarak alinmaniz icin gecerli.")
#     else:
#         print(f"{isim} sizin oyrenim durumunu bilgileriniz Jandarma olaraq alinmaniz icin gecersiz.")
# else:
#     print(f"{isim} sizin yasiniz 21 den kucuk oldugu ucun jandarma olarak alinamazsiniz.")

## Bir oyrencinin iki sinav, bir sozlu notunu alib hesablanan ortalamaya gore not araliqina not puani yazdiriniz 
# 0 - 25 => 0
# 25 - 45 => 1
# 45 - 55 => 2
# 55 - 70 => 3
# 70 - 85 => 4
# 85 - 100 => 5

# not0 = 0
# not1 = 1
# not2 = 2
# not3 = 3
# not4 = 4
# not5 = 5

# ilk_sinav = int(input("Ilk sinav notunuzu giriniz: "))
# ikinci_sinav = int(input("Ikinci sinav notunuzu giriniz: "))
# sozlu_notu = int(input("Sozlu notunuzu giriniz: "))

# ortalama = ( ilk_sinav + ikinci_sinav + sozlu_notu ) / 3

# if ortalama > 0 and ortalama <= 25:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not0}")
# if ortalama > 25 and ortalama <= 45:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not1}")
# if ortalama > 45 and ortalama <= 55:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not2}")
# if ortalama > 55 and ortalama <= 70:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not3}")
# if ortalama > 70 and ortalama <= 85:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not4}")
# if ortalama > 85 and ortalama <= 100:
#     print(f"Sizin notunuzun ortalamasi {ortalama} ve not puaniniz: {not5}")
# if ortalama > 100:
#     print(f"Qaliba notunuzda bi yalnislik var: \nIlk notunuz: {ilk_sinav} \nIkinci notunuz: {ikinci_sinav} \nSozlu notunuz {sozlu_notu} ")

## Kullaniciya satilan ve kullanima baslama zamani (gun hesabina gore alicaz *365) alinan bir buzdolabinin servis zamani 
# - asagidaki bilgilere gorehesablayiniz

# ilk_bakim = 1 
# ikinci_bakim = 2 
# son_bakim = 3 

# simdiki_tarix = datetime.datetime.now()

# yil = int(input("Luften buzdolabini hangi yilda aldiginizi giriniz:"))
# ay = int(input("Luften buzdolabini hangi ayda aldiginizi giriniz:"))
# gun = int(input("Luften buzdolabini hangi gunde aldiginizi giriniz:"))

# alinma_tarixi = datetime.datetime(yil, ay, gun)

# aradaki_gun = (simdiki_tarix - alinma_tarixi).days

# bakim_yili = aradaki_gun/365

# if bakim_yili < ilk_bakim and bakim_yili > 0:
#     print(f"{aradaki_gun} gun. Sizin buzdolabinin {ilk_bakim}. yil servis zamani")
# if bakim_yili < ikinci_bakim and bakim_yili > ilk_bakim:
#     print(f"{aradaki_gun} gun. Sizin buzdolabinin {ikinci_bakim}. yil servis zamani")
# if bakim_yili < son_bakim and bakim_yili > ikinci_bakim:
#     print(f"{aradaki_gun} gun. Sizin buzdolabinin {son_bakim}. yil servis zamani")
# if bakim_yili > son_bakim:
#     print(f"{aradaki_gun} gun. Sizin buzdolabinin son bakim servis zamani bitmisdir")
# if bakim_yili < 0:
#     print(f"Qaliba bir hata olusdu")

## Sure hesabini alinan gun-ay-il bilgisine gore gun bazli hesablayiniz 
# DateTime modulunu kullanalim (2012/9/3)

