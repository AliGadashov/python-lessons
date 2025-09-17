## ---------- range(): belirli bir aralikda sayilari uretiyor ---------------------------------------

# for item in range(5):
    # print(item)

# print(list(range(10))) ## baslangic deyeri
# print(list(range(10, 100))) ## baslangic deyeri / son alacaqi deyer (her ne qeyd olunursan ondan 1 az)
# print(list(range(10, 100, 5))) ## baslangic deyeri / stop deyeri / hansi araliqlarla artmasi 

## ---------- enumerate(): Bir dizi ve ya lisyedeki ogelerin indekslerini ulasir ---------------------------------------

# metn = "Merhaba"
# # indeks = 0

# # for letter in metn:
# #     print(f"index: {indeks}, harf: {letter}")
# #     indeks+=1

# for index,harf in enumerate(metn):
#     print(f"index: {index}, harf: {harf}")

## ---------- zip(): iki ve ya daha fazla liste veya diziyi birlesdirir ---------------------------------------

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e ",]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2)))
print(list(zip(list1,list2,list3)))

for item in zip(list1,list2):
    print(item)

for x,y,z in zip(list1,list2,list3):
    print(f"{x} {y} {z}")