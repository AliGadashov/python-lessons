#-------------------------------- "AND"----------------------------------------
# "Her iki taraf True olduqda true geri dondurur bir taraf False ve ya her iki taraf False olarsa geriye False dondurur "
x = 4

result = True

# result = x > 7 and x < 10 # False
# result = x > 7 and x < 2 # False
# result = x > 3 and x < 10 #True

#-------------------------------- "OR"----------------------------------------
# "Iki terefden biri veya ikiside true olduqu halda geriye true dondurur yalniz her taraf False olduqunda false dondurur"

# result = x > 7 or x < 10 # True
# result = x > 7 or x < 2 # False
# result = x > 3 or x < 10 # True

#-------------------------------- "NOT"----------------------------------------
# "Onune not elave olunmazdan evvel False idise True olur veya tam tersi "

# result = not(x > 7 or x < 10) # False
# result = not(x > 7 and x < 2) # True
# result = not(x > 3 or x < 10) # False

print(result)