# arbitrary arguments

# # * unpacking opertor or splat opertor

# def see_args(*args):
#     print(args)
#     args[0] = 55
#     print(args[0])
#     print(type(args))


# see_args("red", 185, True, {"mango": "yellow"})

# **kwargs - keyword arguments


data = [{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
    {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
},]


def api_func(**kwargs):
    print(kwargs)


for record in data:
    # api_func(**record)
    print("this is message", record["title"])
    print("another key", record["userId"])
