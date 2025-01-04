
class Maruti:

    def __init__(self):
        self.model = "Sedan Automatic"
        self.tyres = "4 back-wheel moving"
        self.seats = "4"
        self.price = "5.5lacs"

    def car_model(self):
        print(f"The model of the car is {self.model}, with {self.tyres} tyres, "
              f"{self.seats} seats, and the price of the car is {self.price}.")


# car1 = Maruti()
# car1.car_model()

# inheritance


class WagonR(Maruti):

    def __init__(self, color):
        super().__init__()
        self.color = color

    def car_color(self):
        print(f"Model of the car is {self.model},"
              f"price is {self.price} and color is {self.color}")


# new_car = WagonR()
# new_car.car_model()

new_wagonR = WagonR("green")
new_wagonR.car_color()
