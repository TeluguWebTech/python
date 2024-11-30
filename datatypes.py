
# # string

# username = 'kalyan'

# phone_number = "5689"

# print(type(username))

# print(type(phone_number))

# cities = '''hyderabad,
#     secunderabad,
#     warangal'''

# states = """delhi,
#     gujarat,
#     telangana"""

# print(cities)
# print(states)

# # numeric types

x = 8956235419
y = 2.3

print(type(x))
print(type(y))

complex_example = 3+4j

print(type(complex_example))

# list datatype

my_list = [11, "username", 55.23, True, {"city": "hyderabad"}]

print(my_list[0])
print(my_list[2])
print(my_list[1])
print(my_list[3])
print(my_list[4])

my_list[0] = "secunderabad"
print(my_list[0])
my_list[4] = 22
print(my_list[4])

print(type(my_list))

# Tuple
example_tuple = (11, "username", 55.23, True, {"city": "hyderabad"})

print("this is output from tuple", example_tuple[0])

# example_tuple[0] = "myName"

# range

numberofseq = list(range(0, 99, 2))
print(numberofseq)

print(range(0, 20))


my_list = [11, "username", 55.23, True, {"city": "hyderabad"}]
print(my_list[-1])
print(my_list[-2])

example_tuple = (11, "username", 55.23, True, {"city": "hyderabad"})

print(example_tuple[-1])
print(example_tuple[-3])


print(list(range(-20, 0)))

# Dictionary

user_details = {
    "username": "Kalyan",
    "phone": 1245689,
    "developer": True
}

print(user_details["username"])
print(user_details["phone"])

# set
fruits = {"apple", "mango", 55, True, 55, 55, 55}

sample_list = [1, 1, 2, 2, 3, 3, 4, 4, 55, 669, 66]
print(set(sample_list))
# print(fruits)

fruits.add("grapes")
print(fruits)

fruits.remove("apple")
print(fruits)


# frozenset

new_fruits = frozenset({"apple", "mango", "banana", 112, 112, 44, 44, 98})

print(new_fruits)

# new_fruits.add("cherry")
# new_fruits.remove("apple")


# boolean
True, False

print(bool(1))
print(bool(0))

x = 10
y = 20

print("x is less than y", x < y)
print("x is greater than y", x > y)

# the bytes datatype in Python represents a sequence of integers, where each integer is in the range 0–255. It cannot directly store strings as its elements, but it can store the byte-encoded representation of a string.

# sample_bytes = bytes([254, 23, 24, 25])+b"anil"

sample_bytes = bytearray([254, 23, 24, 25])+b"anil"

sample_bytes[0] = 200

print(sample_bytes[0])

# none type

abc = None

print(type(abc))
print(type(abc))
