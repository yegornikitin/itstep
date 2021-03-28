class Car:
    model = None
    producer = None

    def __init__(self, model, producer):
        self.model = model
        self.producer = producer
    def year_of_production(self, production_year):
        self.production_year = production_year
    def engine_volume(self, engine_volume):
        self.engine_volume = engine_volume
    def colour(self, colour):
        self.colour = colour
    def price(self, price):
        self.price = price


bmw = Car("523i", "BMW")
bmw.year_of_production = "2007"
bmw.engine_volume = "2.5"
bmw.colour = "black"
bmw.price = "USD 15,000"

print("Producer of the car: ", bmw.producer, "\nModel: ", bmw.model)
print("Production year: ", bmw.year_of_production)
print("Engine volume: ", bmw.engine_volume)
print("Colour of the car: ", bmw.colour)
print("Price of the car: ", bmw.price)




