# numbers = [1,2,3,4,5,6,7,8,9]

## 1. Numbers listesini while ile ekrana yazdirin

# x = 0 

# while x < len(numbers): 
#   print(numbers[x])
#   x+=1
  
## 2. Baslangic ve bitis degerlerini kullanicidan alib aradaki tum tek sayilari ekrana yazdiriniz

# start = int(input("Baslangic degerini giriniz: "))
# end = int(input("Bitis degerini giriniz: "))

# x = start
# while x < len(numbers):
#     if numbers[x] % 2 == 1:
#         print(numbers[x])
#     if x < end:
#        x+=1

## 3. 1-100 arasindaki sayilari azalan bir sekilde yazdirin

# x = 100
# while x >= 1:
#     print(x)
#     x-=1

## 4. Kullanicidan alagaciniz 5 sayiyi bir listenin icine atin ve ekranda listeyi sirali bir sekilde yazin

# x=0
# numbers = []

# while x < 5:
#     number = int(input(f"{x} indeksine gore bir rakam giriniz: "))
#     numbers.append(number)
#     x+=1

# x=0
# while x < len(numbers):
#     print(numbers[x])
#     x+=1

## 5. kullanicidan alacaginiz sinirsiz ulke ve ulke kodu bilgisini, bir ulkeler listesi icerisinde saklayiniz 
# *** Kac ulke girmek istediyini kullaniciya sorunuz 
# *** Liste Dict turunde bir liste olsun yani yapisi {"ulke" : "ulke_kodu", "turkiye": "tr "} biciminde olsun 
# *** Ulkeleri ekleme islemi bittiginde, for dongusu ile ulkeleri ekranda listeleyin 

# ulkeler = []

# ulke_sayi = int(input("Kac ulke kayd etmek istediyinizi giriniz: "))

# while ulke_sayi > 0: 
#     ulke_ismi = input("Ulke ismi: ")
#     ulke_kodu = input("Ulke kodu: ")
#     ulkeler.append({
#         "ulkenin ismi" : ulke_ismi,
#         "Ulkenin kodu" : ulke_kodu
#     })
#     ulke_sayi-=1

# for ulke in ulkeler:
#     print(ulke)
