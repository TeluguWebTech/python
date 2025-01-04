# Parent Class 1: Restaurant
class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Location: {self.location}")

# Parent Class 2: IndianCuisine


class IndianCuisine:
    def __init__(self, cuisine_type):
        self.cuisine_type = cuisine_type

    def display_speciality(self):
        print(f"Cuisine Type: {self.cuisine_type}")
        print("Specialties: Noodles, Fried-Rice, Snacks")

# Child Class 1: SouthIndianRestaurant


class SouthIndianRestaurant(Restaurant, IndianCuisine):
    def __init__(self, name, location, cuisine_type, rating):
        super().__init__(name, location)  # Calls Restaurant.__init__
        IndianCuisine.__init__(self, cuisine_type)
        self.rating = rating

    def display_rating(self):
        print(f"Rating: {self.rating} stars")

# Child Class 2: VegetarianRestaurant


class VegetarianRestaurant(Restaurant, IndianCuisine):
    def __init__(self, name, location, cuisine_type, vegetarian_options):
        super().__init__(name, location)  # Calls Restaurant.__init__
        IndianCuisine.__init__(self, cuisine_type)
        self.vegetarian_options = vegetarian_options

    def display_vegetarian_menu(self):
        print(f"Vegetarian Options: {', '.join(self.vegetarian_options)}")

# Child Class 3: NorthIndianRestaurant


class NorthIndianRestaurant(Restaurant):
    def __init__(self, name, location, fine_dining_menu):
        super().__init__(name, location)
        self.fine_dining_menu = fine_dining_menu

    def display_fine_dining_menu(self):
        print("Fine Dining Menu: ", ", ".join(self.fine_dining_menu))

# Child Class 4: ChineseRestaurant


class ChineseRestaurant(Restaurant, IndianCuisine):
    def __init__(self, name, location, cuisine_type, ambiance_type):
        super().__init__(name, location)  # Calls Restaurant.__init__
        IndianCuisine.__init__(self, cuisine_type)
        self.ambiance_type = ambiance_type

    def display_ambiance(self):
        print(f"Ambiance: {self.ambiance_type} Dining")

# Create objects for each child class


# SouthIndianRestaurant
restaurant1 = SouthIndianRestaurant(
    "Dosa Paradise", "Ameerpet", "South Indian", 4.8)
restaurant1.display_info()
restaurant1.display_speciality()
restaurant1.display_rating()

print("\n")

# VegetarianRestaurant
restaurant2 = VegetarianRestaurant("Annapurna Veg", "Secunderabad", "Vegetarian", [
    "Masala Dosa", "Vada Sambar", "Rava Kesari"])
restaurant2.display_speciality()
restaurant2.display_vegetarian_menu()

print("\n")

# NorthIndianRestaurant
restaurant3 = NorthIndianRestaurant("The Royal Thali", "Banjara Hills", [
    "Paneer Butter Masala", "Aloo Gobi", "Lassi", "Tandoori Roti"])
restaurant3.display_info()
restaurant3.display_fine_dining_menu()

print("\n")

# ChineseRestaurant
restaurant4 = ChineseRestaurant(
    "Golden Dragon", "Hitech City", "Chinese", "Elegant")
restaurant4.display_info()
restaurant4.display_speciality()
restaurant4.display_ambiance()
