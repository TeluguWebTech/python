
# callback functions

products = ("mobiles", "laptops", "computers")

print(products)


def mobile_price():
    print("Price of mobile is 15000")


def process_selection(selected_item,  product_price):
    if selected_item == "mobiles":
        product_price()


def select_product():
    selected_item = input("select your product:")
    process_selection(selected_item, mobile_price)


select_product()
