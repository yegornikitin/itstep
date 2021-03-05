try:
    a = int(input("Please, insert first integer: "))
    b = int(input("Please, insert first integer: "))

    # First function, that will only show  a + b
    def add(a, b):
        return a + b


    print("---------------")
    print("Result without decorator: ", add(a, b))

    # Second function with decorator, that will show  (a + b) * 3
    def triple_result(func):
        def wrapper(*args):
            print("Result with decorator: ", func(*args) * 3)
        return wrapper


    @triple_result
    def add_2(a, b):
        return a + b


    add_2(a, b)

except ValueError:
    print("---------------")
    print("Error. Please, try one more time and insert integers")
