#**********************************************************************************

countries = ['USA', 'Canada', 'Germany', 'India', 'Australia']
years = [1990, 1995, 2000, 2005, 1990, 2010]

## 1- "Japonya" ulkesini listeye ekleyin.
## 2- "Isvec" ulkesini listenin evveline ekleyin.
## 3- "Germany" ulkesini listeden silin.
## 4- "India" ulkesinin index bilgisini bulun.
## 5- "Turkiye" ulkesinin listede olup olmadigini kontrol edin.
## 6- countries listesini ters cevirin.
## 7- countries listesini alfabetik siraya gore siralayin.
## 8- years listesini kucukten buyuge siralayin.
## 9- str = "ankara, istanbul" karakter dizisini listeye cevirin.
## 10- years listesinin en buyuk ve en kucuk elemanlarini bulun.
## 11- years listesinde kac tane 1900  deyeri var.
## 12- years listesini temizleyin.
## 13- Kullanicidan alacaginiz 3 tane ulke ismini countries listesine ekleyin.

## 1

countries.append("Japonya")
# print(countries)

## 2

countries.insert(0, "Isvec")
# print(countries)

## 3

countries.remove("Germany")
# print(countries)

## 4

index_of_india = countries.index("India")
# print(index_of_india)

## 5

is_turkey_in_list = "Turkiye" in countries
# print(is_turkey_in_list)

## 6

countries.reverse()
# print(countries)

## 7

countries.sort()
# print(countries)

## 8    

years.sort()
# print(years)

## 9

str = "ankara, istanbul"
split_cities = str.split(", ")
# print(split_cities)

## 10

min_year = min(years)
max_year = max(years)
# print(min_year, max_year)

## 11

count_1990 = years.count(1990)
# print(count_1990)

## 12   

years.clear()
# print(years)

## 13

input_countries = input("ilk ulke ismini giriniz: ")
countries.append(input_countries)
input_countries = input("2ci ulke ismini giriniz: ")
countries.append(input_countries)
input_countries = input("3cu ulke ismini giriniz: ")
countries.append(input_countries)

# print(countries)