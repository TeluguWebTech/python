
# Scopes
# Global variable,
# Local variable,
# Global keyword
# nonlocal keyword
# locals() ->function
# global() ->function


apple = "red in color"


# def fruit():
#     return "this is fruit output", apple


# def mango():
#     return "this is mango function", apple


# print(fruit())
# print(mango())

# Local variable,
# def local_sample():
#     user_name = "madhu"
#     print(user_name)


# local_sample()


# print(apple)
# print(user_name)

x = 10

# # Global keyword
# def global_sample():
#     global x
#     x = x+125
#     print(x)


# global_sample()


def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 5
        print("Inner function, x:", x)

    inner_function()
    print("Outer function, x:", x)


outer_function()


def friend():
    name = "suresh"
    age = 30
    developer = True
    city = "hyd"

    print(locals())
    print(len(locals()))


friend()
