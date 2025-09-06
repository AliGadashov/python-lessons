# x = 5 
# y = 3
# z = 1

x,y,z = 5,3,1
# print(x,y,z)

# x, y = y, x
# print(x,y)

# x = x + 5
# x += 5
# print(x)

# numbers = [1,2,3]
# numbers = [1,2,3,4,5,6] # we can not unpack more values than variables
# numbers = [1,3] # we can not unpack less values than variables
numbers = [1,2,3,4,5,6,7,8,9]

# x, y, z = numbers

x, *y, z = numbers # y will be a list
print(x,y,z)