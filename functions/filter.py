
# filter function

# filter(function, collection)

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_even(even):
    return even % 2 == 0


# print("checking for even number:", get_even(4))

even_result = filter(get_even, collection)

second_attempt = filter(get_even, collection)

print(set(even_result))
print(list(second_attempt))
