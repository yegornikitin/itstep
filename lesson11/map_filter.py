data = ["Skakhtar", "46", "Dynamo", "45", "Desna", "43"]

filtered_data = filter(lambda x: x.isdigit(), data)
new_data = map(int, filtered_data)

print(list(new_data))
