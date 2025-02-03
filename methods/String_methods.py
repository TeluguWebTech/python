# Python String Methods with Real-Time Examples

# 1. capitalize()

# Description: Converts the first character to uppercase.
# Example:

name = "python programming"
print(name.capitalize())  # Output: "Python programming"

# 2. casefold()

# Description: Converts the string to lowercase, suitable for case-insensitive comparisons.
# Example:

text1 = "Strabe"
text2 = "strasse"
print(text1.casefold() == text2.casefold())  # Output: True

# 3. center(width[, fillchar])

# Description: Centers the string within a given width, padded with a specified character.
# Example:

title = "Python"
print(title.center(10, "-"))  # Output: "--Python--"

# 4. count(sub[, start[, end]])

# Description: Counts occurrences of a substring within the specified range.
# Example:

sentence = "banana banana banana"
print(sentence.count("banana"))  # Output: 3

# 5. encode([encoding[, errors]])

# Description: Encodes the string using the specified encoding.
# Example:

text = "Python © Programming"
print(text.encode("utf-8"))  # Output: b'Python \xc2\xa9 Programming'

# 6. endswith(suffix[, start[, end]])

# Description: Checks if the string ends with the specified suffix.
# Example:

filename = "report.pdf"
print(filename.endswith(".pdf"))  # Output: True

# 7. expandtabs(tabsize=8)

# Description: Replaces tabs with spaces.
# Example:

text = "Hello\tWorld"
print(text.expandtabs(4))  # Output: "Hello   World"

# 8. find(sub[, start[, end]])

# Description: Returns the lowest index of the substring.
# Example:

sentence = "Hello, welcome to Python."
print(sentence.find("welcome"))  # Output: 7

# 9. format(*args, **kwargs)

# Description: Formats the string with placeholders.
# Example:

text = "Hello, {}. Welcome to {}."
# Output: "Hello, Alice. Welcome to Python."
print(text.format("Alice", "Python"))

# 10. format_map(mapping)

# Description: Formats the string using a mapping dictionary.
# Example:

data = {"name": "Alice", "language": "Python"}
# Output: "Alice loves Python."
print("{name} loves {language}.".format_map(data))

# 11. index(sub[, start[, end]])

# Description: Returns the lowest index of the substring or raises ValueError.
# Example:

sentence = "Hello, Python!"
print(sentence.index("Python"))  # Output: 7

# 12. isalnum()

# Description: Checks if all characters are alphanumeric.
# Example:

text = "Python3"
print(text.isalnum())  # Output: True

# 13. isalpha()

# Description: Checks if all characters are alphabetic.
# Example:

text = "Python"
print(text.isalpha())  # Output: True

# 14. isascii()

# Description: Checks if all characters are ASCII.
# Example:

text = "Python123"
print(text.isascii())  # Output: True

# 15. isdecimal()

# Description: Checks if all characters are decimal.
# Example:

num = "12345"
print(num.isdecimal())  # Output: True

# 16. isdigit()

# Description: Checks if all characters are digits.
# Example:

num = "12345"
print(num.isdigit())  # Output: True

# 17. isidentifier()

# Description: Checks if the string is a valid Python identifier.
# Example:

identifier = "variable1"
print(identifier.isidentifier())  # Output: True

# 18. islower()

# Description: Checks if all characters are lowercase.
# Example:

text = "hello"
print(text.islower())  # Output: True

# 19. isnumeric()

# Description: Checks if all characters are numeric.
# Example:

num = "123"
print(num.isnumeric())  # Output: True

# 20. isprintable()

# Description: Checks if all characters are printable.
# Example:

text = "Hello, World!"
print(text.isprintable())  # Output: True

# 21. isspace()

# Description: Checks if all characters are whitespace.
# Example:

text = "   "
print(text.isspace())  # Output: True

# 22. istitle()

# Description: Checks if the string follows title case.
# Example:

title = "Python Programming"
print(title.istitle())  # Output: True

# 23. isupper()

# Description: Checks if all characters are uppercase.
# Example:

text = "HELLO"
print(text.isupper())  # Output: True

# 24. join(iterable)

# Description: Joins elements of an iterable with the string as a separator.
# Example:

words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: "Python is fun"

# 25. ljust(width[, fillchar])

# Description: Left-justifies the string in a field of given width.
# Example:

text = "Python"
print(text.ljust(10, "-"))  # Output: "Python----"

# 26. lower()

# Description: Converts all characters to lowercase.
# Example:

text = "HELLO"
print(text.lower())  # Output: "hello"

# 27. lstrip([chars])

# Description: Removes leading characters (default: whitespace).
# Example:

text = "   Hello"
print(text.lstrip())  # Output: "Hello"

# 28. maketrans(x[, y[, z]])

# Description: Returns a translation table for use with translate().
# Example:

trans = str.maketrans("abc", "123")
text = "abcde"
print(text.translate(trans))  # Output: "123de"

# 29. partition(sep)

# Description: Splits the string into a 3-tuple: (head, separator, tail).
# Example:

text = "Python is fun"
print(text.partition("is"))  # Output: ('Python ', 'is', ' fun')

# 30. replace(old, new[, count])

# Description: Replaces occurrences of a substring with another.
# Example:

text = "I like Python. Python is great."
# Output: "I like JavaScript. JavaScript is great."
print(text.replace("Python", "JavaScript"))

# 31. rfind(sub[, start[, end]])

# Description: Returns the highest index of the substring.
# Example:

text = "Python programming is fun"
print(text.rfind("is"))  # Output: 20
