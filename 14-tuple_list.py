list = [1,2,3,4,5]
# tuple = (23,45,67,89)
tuple = 23,45,67,89

# print(type(list))
# print(type(tuple))

# print(list[1])
# print(tuple[1])

list = ["ali",23,45.67,True]
tuple = ("ali",23,45.67,True)
names = ("ali","veli","ayse","fatma") + tuple

# list[0] = "veli"
# tuple[0] = "veli" # TypeError: 'tuple' object does not support item assignment

print(names)