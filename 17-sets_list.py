fruits = {"apple", "banana", "cherry" }
# print(fruits)
# print(type(fruits))

# print(fruits[0])  # This will raise an error because sets are unordered and do not support indexing

fruits.add("orange")
# print(fruits)

fruits.update(["kiwi", "mango"])
# print(fruits)

fruits.remove("banana")
# print(fruits)

fruits.discard("grape")  # This will not raise an error even if "grape" is not in the set

fruits.pop()  # Removes and returns an arbitrary element from the set
# print(fruits)

number = [1, 2, 3, 4,55 ,6,7,7, 8,9,0]
print(set(number))  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} (duplicates removed)
