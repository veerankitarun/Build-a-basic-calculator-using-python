# you are going to a make the basic calculator using python code 
# just download the code and run you just need to change the file name extension as .py


def add(P, Q):
    # This function is used for adding two numbers
    return P + Q


def subtract(P, Q):
    # This function is used for subtracting two numbers
    return P - Q


def multiply(P, Q):
    # This function is used for multiplying two numbers
    return P * Q


def divide(P, Q):
    # This function is used for dividing two numbers
    return P / Q


# Now we will take inputs from the user
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':  # elif is like if-else statement 
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("enter a valid input")  # if any input don't match with the given values then the output will be invalid
