# key _ value 

cities = ["istanbul", "ankara", "izmir"]
population = [15, 5, 4]

# print(population[cities.index("ankara")])

population = { "istanbul" : 15, "ankara" : 5, "izmir" : 4 }

population["ankara"] = 6
population["antalya"] = "3 milyon"

# print(population["ankara"])
# print(population["antalya"])

users = {
    "ali" : {
        "age" : 25,
        "city" : "istanbul"
    },
    "veli" : {
        "age" : 30,
        "city" : "ankara"
    }
}

# print(users)
# print(users["ali"])
# print(users["ali"]["city"])