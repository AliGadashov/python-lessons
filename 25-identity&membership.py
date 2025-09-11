#---------------------------- Identity Operator: "is" ----------------------------------------"

# x = y = [1, 2, 3]  # ayni adreste tutuluyolar

# z = [1, 2, 3] # adresi x ve y den farkli

# print(x == y)
# print(x == z)
# print("-------------")
# print(x is y)
# print(x is z) # is operatoru bilgilerin ayni yerde tutulub tutulmadiqini yokluyo

#---------------------------- Membership Operator: "in" ----------------------------------------"

# animal = ["dog", "cat"]

# print("dog" in animal)
# print("fish" in animal)

animal = "wolf"

print("w" in animal)
print("w" not in animal)
print("a" in animal)