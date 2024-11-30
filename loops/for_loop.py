
# for var in sequence

city = "Hyderabad"

for i in city:
    print(i)

fruits = ["apple", "mango", 55]

for fruit in fruits:
    print(fruit)

# tuple

colors = ("red", "green", "yellow")

for color in colors:
    print(color)


# range

for item in range(121):
    print(item)

# nested

rows = 10

# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
