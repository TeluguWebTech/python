
# Conditional Statements (True/False)
# if, if-else, if-elif-else

if 10 < 20:
    print("yes 10 is less than 20")

# if-else,

if 40 > 50:
    print("my name is Kalyan")
else:
    print("i live in Hyderabad")

# if-elif-else

if 50 < 40:
    print("my name is ashok")
elif 45 < 30:
    print('my name is gautham')
elif 30 > 15:
    print("my name is suri")
else:
    print("this is else block")

# "and", "or", "not"
age = 18
if (age <= 18) and (age != 19):
    print("you are not allowed")

if (age < 19) or (age == 18):
    print("yor are welcome")

if not (age != 19):
    print("you are not 19yrs old")
else:
    print("you are 19yrs old")
