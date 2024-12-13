#fmt: off

def user_details():
    user_name = "suresh"
    phone_num = "123456"

    print(user_name)
    print(phone_num)
    return user_name + " " + phone_num


print(user_details())

# lambda functions

greeting = lambda: "welcome"
print(greeting())

result = lambda x,y: x+y, print("add")

print(result(225,350))