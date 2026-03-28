# Program to find the maximum of two numbers
# Input two numbers from user
num1 = int(input("Enter a number A: "))
num2 = int(input("Enter a number B: "))

# Compare the two numbers to find the maximum
if num1 > num2:
    # num1 is greater than num2
    print("The maximum number is:", num1)
elif num2 > num1:
    # num2 is greater than num1
    print("The maximum number is:", num2)
else:
    # Both numbers are equal
    print("Both numbers are equal.")