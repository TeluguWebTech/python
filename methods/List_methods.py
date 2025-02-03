# Python List Methods with Examples

# Lists in Python are versatile and come with a variety of methods to manipulate and manage data. Here's a comprehensive guide to all list methods with real-time examples:

# 1. append()

# Adds a single element to the end of the list.

cart = ["apple", "banana"]
cart.append("orange")
print(cart)  # Output: ['apple', 'banana', 'orange']

# 2. extend()

# Adds all elements of an iterable (e.g., list, tuple) to the end of the list.

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert()

# Inserts an element at a specific position.

tasks = ["Task1", "Task3"]
tasks.insert(1, "Task2")
print(tasks)  # Output: ['Task1', 'Task2', 'Task3']

# 4. remove()

# Removes the first occurrence of the specified value.

guests = ["Alice", "Bob", "Charlie", "Bob"]
guests.remove("Bob")
print(guests)  # Output: ['Alice', 'Charlie', 'Bob']

# 5. pop()

# Removes and returns the element at the specified index (default is the last element).

stack = [10, 20, 30, 40]
last_item = stack.pop()
print(last_item)  # Output: 40
print(stack)      # Output: [10, 20, 30]

# 6. clear()

# Removes all elements from the list.

data = [1, 2, 3]
data.clear()
print(data)  # Output: []

# 7. index()

# Returns the index of the first occurrence of the specified value.

names = ["John", "Paul", "George", "Ringo"]
print(names.index("George"))  # Output: 2

# 8. count()

# Returns the number of times a specified value appears in the list.

votes = ["yes", "no", "yes", "yes"]
print(votes.count("yes"))  # Output: 3

# 9. sort()

# Sorts the list in ascending (default) or descending order.

scores = [50, 20, 80, 40]
scores.sort()
print(scores)  # Output: [20, 40, 50, 80]

scores.sort(reverse=True)
print(scores)  # Output: [80, 50, 40, 20]

# 10. reverse()

# Reverses the order of the list.

letters = ["a", "b", "c", "d"]
letters.reverse()
print(letters)  # Output: ['d', 'c', 'b', 'a']

# 11. copy()

# Returns a shallow copy of the list.

original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)  # Output: [1, 2, 3]

# 12. len() (Not a method, but useful with lists)

# Returns the number of elements in the list.

items = [100, 200, 300]
print(len(items))  # Output: 3

# 13. max() (Not a method, but useful with lists)

# Returns the largest item in the list.

numbers = [10, 20, 30, 40]
print(max(numbers))  # Output: 40

# 14. min() (Not a method, but useful with lists)

# Returns the smallest item in the list.

numbers = [10, 20, 30, 40]
print(min(numbers))  # Output: 10

# 15. sum() (Not a method, but useful with lists)

# Returns the sum of all items in the list.

prices = [100, 200, 300]
print(sum(prices))  # Output: 600

# 16. sorted() (Not a method, but useful with lists)

# Returns a new sorted list from the given list.

scores = [50, 20, 80, 40]
sorted_scores = sorted(scores)
print(sorted_scores)  # Output: [20, 40, 50, 80]
print(scores)         # Original list remains unchanged

# Real-Time Application Example

# Imagine managing an online store:

cart = []  # Initialize empty cart

# 17. Add items
cart.append("Laptop")
cart.append("Mouse")

# Adding multiple items
cart.extend(["Keyboard", "Monitor"])

# Check the cart
print("Cart:", cart)  # Cart: ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

# Remove an item
cart.remove("Mouse")

# Insert a priority item
cart.insert(0, "Tablet")

# Check cart size
print("Total items in cart:", len(cart))  # Total items in cart: 4

# Sort items alphabetically
cart.sort()
# Sorted Cart: ['Keyboard', 'Laptop', 'Monitor', 'Tablet']
print("Sorted Cart:", cart)
