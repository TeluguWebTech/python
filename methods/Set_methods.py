# Python Set Methods with Real-Time Examples

# Python sets are collections of unique and unordered elements. They come with a variety of built-in methods to perform operations such as adding, removing, or comparing elements. Here’s a comprehensive list of Python set methods with practical examples:

# 1. add()

# Adds an element to the set.

fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)  # Output: {"apple", "banana", "orange"}

# 2. clear()

# Removes all elements from the set.

fruits = {"apple", "banana", "orange"}
fruits.clear()
print(fruits)  # Output: set()

# 3. copy()

# Returns a shallow copy of the set.

fruits = {"apple", "banana"}
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: {"apple", "banana"}

# 4. difference()

# Returns a set containing elements in the first set but not in the second.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # Output: {1}

# 5. difference_update()

# Removes elements found in another set from the original set.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}

# 6. discard()

# Removes the specified element from the set, if present.

fruits = {"apple", "banana"}
fruits.discard("banana")
print(fruits)  # Output: {"apple"}

# 7. intersection()

# Returns a set containing elements common to both sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # Output: {2, 3}

# 8. intersection_update()

# Updates the set to keep only elements found in it and another set.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}

# 9. isdisjoint()

# Returns True if two sets have no elements in common.

set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True

# 10. issubset()

# Returns True if the set is a subset of another set.

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

# 11. issuperset()

# Returns True if the set is a superset of another set.

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True

# 12. pop()

# Removes and returns an arbitrary element from the set.

fruits = {"apple", "banana"}
removed_element = fruits.pop()
print(removed_element)  # Output: "apple" (or "banana")
print(fruits)

# 13. remove()

# Removes a specified element from the set. Raises a KeyError if the element is not found.

fruits = {"apple", "banana"}
fruits.remove("apple")
print(fruits)  # Output: {"banana"}

# 14. symmetric_difference()

# Returns a set with elements in either of the sets but not in both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# 15. symmetric_difference_update()

# Updates the set with elements found in either set but not in both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}

# 16. union()

# Returns a set containing all elements from both sets.

set1 = {1, 2}
set2 = {3, 4}
print(set1.union(set2))  # Output: {1, 2, 3, 4}

# 17. update()

# Updates the set with elements from another set or iterable.

set1 = {1, 2}
set2 = {3, 4}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4}
