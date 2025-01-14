# Polymorphism

# Method Overloading


class Hotel:
    def hotel_name(self, *names):
        if len(names) == 0:
            print("Welcome")
        elif len(names) == 1:
            print(f"Welcome to Hotel {names[0]} ")
        else:
            print(f"Welcome to Hotel {names[0]}- {names[1]}")


newHotel = Hotel()

newHotel.hotel_name()
newHotel.hotel_name("Paradise")
newHotel.hotel_name("Bawarchi", "5-star")

# Method Overriding


class Restaurant:
    def get_menu(self):
        pass


class Paradise(Restaurant):
    def get_menu(self):
        print("Menu: Biryani, Chicken, Mutton")


class VegHotel(Restaurant):
    def get_menu(self):
        print("Menu: Idly, Dosa, Poori")


NonVeg = Paradise()
NonVeg.get_menu()

PureVeg = VegHotel()
PureVeg.get_menu()
