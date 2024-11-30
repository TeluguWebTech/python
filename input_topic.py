

# # age = input("what is your age?")

# # print("user age is", age)

# # print(type(age))

# first_number = input("enter first number:")

# ufn = int(first_number)

# second_number = input("enter second number:")

# usn = int(second_number)

# result = print(ufn + usn)

# input while loop

correct_password = "secret123"

attempts = 0

max_attempts = 3

while attempts < max_attempts:
    user_password = input("Enter your password:")

    if user_password == correct_password:
        print("You are welcome")
    else:
        print("incorrect Password")
        attempts += 1

    if attempts == max_attempts:
        print("sorry you have reached maximum attempts")
