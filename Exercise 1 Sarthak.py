"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen."""
#git config--global user.name "C4P007"

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

"""Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

print("Hello," + first_name + " " + last_name + "! Welcome to the Python Program.")

