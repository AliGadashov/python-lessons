#********************************LISTE METHODLARI****************************************************************

# len() -> karakter sayini verir
# max() -> en buyuk elemani verir
# min() -> en kucuk elemani verir
# append() -> liste sonuna eleman ekler
# insert() -> listeye index belirterek eleman ekler
# pop() -> sondaki elemani siler
# remove() -> belirtilen elemani siler
# sort() -> listeyi alfabetik siraya gore dizer
# reverse() -> listeyi ters cevirir
# count() -> belirtilen elemanin listede kac kere gectigini verir
# clear() -> listeyi temizler

#****************************************************************************************************************

numbers = [1, 5, 3, 9, 2]
letters = ["a", "b", "c", "d", "e"]

result = len(numbers)

result = max(letters)
result = min(numbers)

numbers.append(10)
letters.append("abc")

print(numbers)
print(letters)

numbers.insert(4, 85)
letters.insert(2, "xyz")

print(numbers)
print(letters)

# numbers.pop() # index
# letters.pop(3)

# numbers.remove(3) # value
# letters.remove("b")

# numbers.sort()
# letters.sort()

# numbers.reverse()
# letters.reverse()

# result = numbers.count(5)
# result = letters.count("a")

# numbers.clear()
# letters.clear()

# print("Result:", letters)