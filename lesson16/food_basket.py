# Первое задание
def calculate_food_basket(food_basket: dict, exchange_rate: float) -> float:
    return sum(food_basket.values()) * exchange_rate


basket_example = {
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "sunflower oil": 2,
    "meat": 2.4
}
print("1. Total sum of food basket in UAH is: ",
      calculate_food_basket(basket_example, 27.5))
print("---------------------------------------")


# Второе задание
def find_most_in_food_basket(food_basket: dict, max_cost=True) -> set:
    new_list = []
    if max_cost:
        for product in food_basket:
            if food_basket[product] > 2:
                new_list.append(product)
                new_set = set(new_list)
        return new_set
    elif not max_cost:
        for product in food_basket:
            if food_basket[product] < 1:
                new_list.append(product)
                new_set = set(new_list)
        return new_set


big_basket = {
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "sunflower oil": 2,
    "meat": 2.4,
    "eggs": 0.4,
    "fish": 2.4
}
print("2.1. The most expensive products in the basket: ",
      find_most_in_food_basket(big_basket))
print("2.2. The cheapest products in the basket: ",
      find_most_in_food_basket(big_basket, False))
print("---------------------------------------")
