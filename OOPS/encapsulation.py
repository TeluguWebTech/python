
# # without Encapsulation
# class Bank:

#     account_balance = "15000"


# user = Bank()
# print(user.account_balance)

# Encapsulation

class Bank:
    __account_balance = "55000"  # private attribute

    def __user_account(self):
        print(f"user account balance is {self.__account_balance}")

    def show_balance(self):
        self.__user_account()


b1 = Bank()
# b1.__account_balance
# b1.__user_account()

b1.show_balance()
