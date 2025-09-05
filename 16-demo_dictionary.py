urunler = {
    "k500" : {
        "marka" : "iphone",
        "fiyat" : 4500,
        "model" : "12 pro max"
    },
    "k280" : {
        "marka" : "samsung",
        "fiyat" : 3000,
        "model" : "galaxy s20"
    },
    "k700" : {
        "marka" : "xiaomi",
        "fiyat" : 2000,
        "model" : "redmi note 10"
    }
}

## 1- bilgileri verilen urunleri kullanicidan aldiginiz bilgilerle dictionary icerisinde saklayiniz

urun_kodu = input("urun kodu : ")
urun_marka = input("marka : ")   
urun_fiyat = input("fiyat : ")
urun_model =input("model : ")

# urunler[urun_kodu] = {
#     "marka" : urun_marka,
#     "fiyat" : urun_fiyat,
#     "model" : urun_model
# }

urunler.update({
    urun_kodu : {
        "marka" : urun_marka,
        "fiyat" : urun_fiyat,
        "model" : urun_model
    }
})

# print(urunler)

## 2- kullanicidan urun kodu alarak urun bilgilerini gosteriniz

urun_kodu = input("urun kodu : ")

print(f"urun kodu : {urunler[urun_kodu]}")
