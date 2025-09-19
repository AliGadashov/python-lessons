# numbers= []
# for i in range(10):
#     numbers.append(i)
# print(numbers)

# print("------------------------------------------")

# numbers = [i for i in range(10)]
# print(numbers)

#-------------------------------------------------------

# numbers = []
# for i in range(10):
#     if (i%3 ==0):
#         print(i**2)

# numbers = [(i**2) for i in range(10) if i % 3 == 0]

# print(numbers)

#-------------------------------------------------------

myString = "Gadashov Ali"

myList = []

for letter in myString:
    print(letter)

myList = [letter for letter in myString]
print(myString)