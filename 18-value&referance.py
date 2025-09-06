##*********************** VALUE TYPE => string, number, bool ***********************##

# a = 2 
# b = 3

# a = b
# b = 4
# print(a, b)  

## ----------

# x = "x"
# y = "y"
# x = y
# y = "z"
# print(x, y) 

##*********************** REFERENCE TYPE => list, dict ***********************##

a = [1, 2, 3]
b = [4, 5, 6]

a = b

b[0] = 7
print(a, b) 