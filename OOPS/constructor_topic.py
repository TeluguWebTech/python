

class Employee:
    department = "Accounts"
# constructor
# non-parameterized constructor

    def __init__(self):
        self.emp_name = "Kalyan"
        self.phone = "12345"

    def emp_detail(self):
        return f"Employee name is {self.emp_name}, phone number is {self.phone}"


new_emp = Employee()  # object
print(new_emp.emp_detail())


class Student:
    department = "Accounts"

    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_detail(self):
        return (f"Student name is {self.name} and age is {self.age}")
# instantiation


student_one = Student("Rajesh", 28)  # Student name is Rajesh and age is 28
print(student_one.student_detail())

student_two = Student("Suresh", 26)  # Student name is Suresh and age is 26
print(student_two.student_detail())

student_three = Student("Hari", 27)
print(student_three.student_detail())

student_four = Student("Nani", 26)
print(student_four.student_detail())
