class Metaclass(type):
    def __new__(self, class_name, bases, attrs):
        attr = {}
        for key, value in attrs.items():
            if not key.startswith('__'):
                attr['method_' + key] = value
                new_class_name = class_name.lower()
            else:
                attr[key] = value
        return type(new_class_name, bases, attr)

class Car(metaclass=Metaclass):
    year = 1972
    car = "BMW"

    def print_car(self):
        print(self.year)

if __name__ == '__main__':
    bmw = Car()
    print(bmw.method_car)

