## 1- Girilen bir sayinin 0-100 arasinda olup olmadiqini kontrol ediniz

# num1 = int(input("Bir rakam giriniz: "))

# result = num1 > 0 and num1 < 100

# print(f"Girilen rakam 0 ile 100 arasinda: {result}")

## 2- Girilen sayinin pozitiv cift sayi olub olmadiqini kontrol ediniz

# num1 = int(input("Bir rakam giriniz: "))

# result = (num1 % 2 == 0) and num1 > 0

# print(f"Girilen rakam pozitiv cift rakam: {result}")

## 3- Email ve parola bilgileri ile giris kontrolu yapiniz

# email = "aligadashov"
# password = "aligadashovv"

# input_email= input("Email adresini giriniz:")
# input_passsword = input("Passwordu giriniz:")

# result = email == input_email and password == input_passsword

# print(f"Giris bilgileriniz dogrudur: {result}")

## 4- Girilen 3 sayiyi buyukluk olaraq karsilastiriniz

# num1 = int(input("Birinci rakami girini:"))
# num2 = int(input("Ikinci rakami girini:"))
# num3 = int(input("Ucuncu rakami girini:"))

# result1 = num1 > num2 and num1 > num3
# result2 = num2 > num1 and num2 > num3
# result3 = num3 > num1 and num3 > num2

# print(f"Girdiyiniz ilk rakam en buyuyu: {result1}")
# print(f"Girdiyiniz ikinci rakam en buyuyu: {result2}")
# print(f"Girdiyiniz ucuncu rakam en buyuyu: {result3}")


## 5- Kullanicidan 2 vizenin "%60" ini ve finalin "%40"ini alarak ortalama hesablayiniz
#   "Eger ortalama degeri 50 ve uzeri ise gecti altindaysa kaldi yazdirin"
#   a)Ortalama 50 olsa bile final notu en az 50 olmalidir 
#   b)Finaldan 70 aldiginda ortalamanin bir onemi olmasin

# vize1 = int(input("ilk nizenizi giriniz: "))
# vize2 = int(input("Ikinci vizenizi giriniz: "))
# final = int(input("Finalin puani giriniz: "))

# ortalama = (((vize1 + vize2) * 0.6) + (final * 0.4))/2

# result1 = ortalama >=50 and final >= 50
# result2 = final >= 70 or ortalama > 50   

# print(f"Imtahani notunuz: {ortalama} ve gecme durumunuz: {result1}")
# print(f"Imtahani notunuz: {ortalama} ve gecme durumunuz: {result2}")

## 6- Kullanicidan ad, kilo ve boy bilgilerini alib kilo indexlerini hesablayiniz 
#   indeks formulu: (kilo/boy uzunlugunun karesi)
#   indeks siralamasina gore kisinin hangi aralikda oldugunu yazdiriniz
#   0-18    => zayif
#   19-25    => normal
#   26-30    => fazla kilolu
#   31-35    => sisman

# name = input("Isminizi giriniz:")
# kilo = int(input("Kilonuzu giriniz: "))
# boy = float(input("Boyunuzu giriniz: "))

# formul = ((kilo) / (boy ** 2))

# zayif = formul > 0 and formul <=19
# normal = formul > 19 and formul <=26
# kilolu = formul > 26 and formul <=31
# obez = formul > 31 and formul <=35

# print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: {zayif}")
# print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: {normal}")
# print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: {kilolu}")
# print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: {obez}")