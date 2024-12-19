# reduce function

# import functools
from functools import reduce

collections = [11, 22, 33, 44, 55, 66]


def total_col(x, y):
    return x*y


grandTotal = reduce(total_col, collections)

print(grandTotal)
