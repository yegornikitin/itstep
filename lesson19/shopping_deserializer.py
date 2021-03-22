import pickle
import json


# pickle

with open("shopping_list.pkl", "rb") as file:
    file_load = pickle.load(file)

print(file_load)

# json

with open("shopping_list.json", "r") as file:
    file_load = json.load(file)

print(file_load)
