## 1- Girilen bir sayinin 0-100 arasinda olup olmadiqini kontrol ediniz

# num1 = int(input("Bir rakam giriniz: "))

# result = num1 > 0 and num1 < 100

# if num1 > 0 and num1 < 100:
#     print("Girilen rakam 0 ile 100 arasinda")
# else:
#     print("Girilen rakam 0 ile 100 arasinda deyil")

## 2- Girilen sayinin pozitiv cift sayi olub olmadiqini kontrol ediniz

# num1 = int(input("Bir rakam giriniz: "))

# if  num1 > 0:
#     if num1 % 2 == 0:
#         print("Girilen rakam pozitiv cift rakam.")
#     else:
#         print("Girilen rakam cift rakam deyil.")
# else:
#     print("Girilen rakam pozitiv rakam deyil.")

## 3- Email ve parola bilgileri ile giris kontrolu yapiniz

# email = "aligadashov"
# password = "aligadashovv"

# input_email= input("Email adresini giriniz:")
# input_passsword = input("Passwordu giriniz:")

# if email == input_email:
#     if password == input_passsword:
#         print("Giris bilgileriniz dogrudur.")
#     else:
#         print("Parolaniz yalnis.")
# else:
#     print("Mail adresiniz yalnis.")

## 4- Girilen 3 sayiyi buyukluk olaraq karsilastiriniz

# num1 = int(input("Birinci rakami girini:"))
# num2 = int(input("Ikinci rakami girini:"))
# num3 = int(input("Ucuncu rakami girini:"))

# if num1 > num2 and num1 > num3:
#     print("Girdiyiniz ilk rakam en buyuyu.")
# if num2 > num1 and num2 > num3:
#     print("Girdiyiniz ikinci rakam en buyuyu.")
# if num3 > num1 and num3 > num2:
#     print("Girdiyiniz ucuncu rakam en buyuyu.")

## ----------------------------------------------------
# if num1 > num2 : 
#     if num1 > num3 :
#         print("Girdiyiniz ilk rakam en buyuyu.")
#     else:
#         print("Girdiyiniz ucuncu rakam en buyuyu.")
# if num2 > num1 :
#     if num2 > num3 :
#         print("Girdiyiniz ikinci rakam en buyuyu.")
#     else:
#         print("Girdiyiniz ucuncu rakam en buyuyu.")
# if num3 > num1 :
#     if num3 > num2:
#         print("Girdiyiniz ucuncu rakam en buyuyu.")
#     else: 
#         print("Girdiyiniz ikinci rakam en buyuyu.")

## Bu kisim fazla karmasik ve kodlar gereksiz uzanmis 
## ----------------------------------------------------



## 5- Kullanicidan 2 vizenin "%60" ini ve finalin "%40"ini alarak ortalama hesablayiniz
#   "Eger ortalama degeri 50 ve uzeri ise gecti altindaysa kaldi yazdirin"
#   a)Ortalama 50 olsa bile final notu en az 50 olmalidir 
#   b)Finaldan 70 aldiginda ortalamanin bir onemi olmasin

# vize1 = int(input("ilk vizenizi giriniz: "))
# vize2 = int(input("Ikinci vizenizi giriniz: "))
# final = int(input("Finalin puani giriniz: "))

# ortalama = (((vize1 + vize2) * 0.6) + (final * 0.4))/2

# if final >= 70: 
#     print(f"Imtahani notunuz: {ortalama} \nFinal notunuz: {final} \nGecme durumunuz: Gecti")
# if ortalama >=50 and final >= 50 :
#     print(f"Imtahani notunuz: {ortalama} \nGecme durumunuz: Gecti")
# else:
#     print(f"Imtahani notunuz: {ortalama} \nGecme durumunuz: Kaldi")

## 6- Kullanicidan ad, kilo ve boy bilgilerini alib kilo indexlerini hesablayiniz 
#   indeks formulu: (kilo/boy uzunlugunun karesi)
#   indeks siralamasina gore kisinin hangi aralikda oldugunu yazdiriniz
#   0-18    => zayif
#   19-25   => normal
#   26-30   => fazla kilolu
#   31-35   => sisman

# name = input("Isminizi giriniz:")
# kilo = int(input("Kilonuzu giriniz: "))
# boy = float(input("Boyunuzu giriniz: "))

# formul = ((kilo) / (boy ** 2))

# if (formul > 0 and formul <= 19):
#     print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: zayif")
# elif (formul > 19 and formul <=26):
#     print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: normal")
# elif (formul > 26 and formul <=31):
#     print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: kilolu")
# elif (formul > 31 and formul <=35):
#     print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: obez")
# elif (formul > 35):
#     print(f"{name} sizin kilo indeksiniz: {formul} ve bu indekse gore: obezden daha yukari")