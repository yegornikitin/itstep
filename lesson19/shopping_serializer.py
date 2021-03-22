import pickle
import json

shopping_list_example = [
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower oil": 2,
        "meat": 2.4
    },
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower oil": 2,
        "meat": 2.4,
        "eggs": 0.4,
        "fish": 2.4
    }
]

# pickle
with open("shopping_list.pkl", "wb") as file:
    pickle.dump(shopping_list_example, file)

with open("shopping_list.pkl", "rb") as file:
    file_load = pickle.load(file)

print(file_load)

# json
with open("shopping_list.json", "wb") as file:
    json.dump(shopping_list_example, file)

with open("shopping_list.json", "rb") as file:
    file_load = json.load(file)

print(file_load)
