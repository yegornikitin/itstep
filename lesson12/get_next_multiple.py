def get_next_multiple(number):
    for multiple in range(1, 100000):
        yield number * multiple


gen_multiple_of_two = get_next_multiple(2)
print("First multiple of '2'= ", next(gen_multiple_of_two))
print("Next multiple of '2'= ", next(gen_multiple_of_two))
print("Next multiple of '2'= ", next(gen_multiple_of_two))
print("Next multiple of '2'= ", next(gen_multiple_of_two))
print("------------")

gen_multiple_of_thirteen = get_next_multiple(13)
print("First multiple of '13'= ", next(gen_multiple_of_thirteen))
print("Next multiple of '13'= ", next(gen_multiple_of_thirteen))
print("Next multiple of '13'= ", next(gen_multiple_of_thirteen))
print("Next multiple of '13'= ", next(gen_multiple_of_thirteen))
print("------------")
print("------------")

# Generator of multiples from user_input
print("Dear user, the program will show multiples from your input integer.")
try:
    user_input = int(input("Please, insert your integer: "))


    def uer_input_next_multiple(user_input):
        for multiple in range(1, 100000):
            yield user_input * multiple


    gen_multiple_of_two = get_next_multiple(user_input)
    print("First multiple of your input = ", next(gen_multiple_of_two))
    while True:
        question = input("Want to see next multiple? Please insert 'yes' or 'no': ")
        if question == "yes":
            print("Next multiple of your input = ", next(gen_multiple_of_two))
        elif question == "no":
            break
        else:
            print("Error. Not correct insert")
except ValueError:
    print("Error. Not correct insert")
