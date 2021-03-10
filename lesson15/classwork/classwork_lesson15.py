def same_cities(first_traveler_cities:set, second_traveler_cities:set):
    new_set = first_traveler_cities.intersection(second_traveler_cities)
    return new_set

mark_cities = {"“Boston”", "“Lisbon”", "“Paris”", "“London”"}
peter_cities = {"“New York”", "“Lisbon”", "“Michigan”", "“London”"}

print("First task: ", same_cities(mark_cities, peter_cities))
print("----------------------------------------")

def unique_ids(ids: list):
    set_new = set(ids)
    new_list_2 = list(set_new)
    return new_list_2


print("Second task: ", unique_ids([1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9, 8, 12, 13, 14, 14, 19]))
print("----------------------------------------")



def same_cities_2(first_traveler_cities:set, second_traveler_cities:set):
    try:
        user_input = input("If you want to intersept two sets => please, insert 'intersept' \n"
                           "If you want to unique from first set => please, insert 'first' \n"
                           "If you want to unique from second set => please, insert 'second' \n"
                           "If you want to exit => please, insert 'exit' :  \n")
        if user_input == "intersept":
            new_set = first_traveler_cities.intersection(second_traveler_cities)
            return new_set
        if user_input == "first":
            mark = first_traveler_cities.difference(second_traveler_cities)
            return mark
        if user_input == "second":
            peter = second_traveler_cities.difference(first_traveler_cities)
            return peter
        if user_input == "exit":
            exit
        else:
            print("Error. Not correct input")
    except ValueError:
        print("Error. Not correct input")


mark_cities = {"“Boston”", "“Lisbon”", "“Paris”", "“London”"}
peter_cities = {"“New York”", "“Lisbon”", "“Michigan”", "“London”"}

print("Third task: ", same_cities_2(mark_cities, peter_cities))
print("----------------------------------------")

