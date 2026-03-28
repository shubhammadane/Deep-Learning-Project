# Program to find the maximum of three numbers
# Input three numbers from user
num1 = int(input("Enter a number A: "))
num2 = int(input("Enter a number B: "))             
num3 = int(input("Enter a number C: "))     

# Check if all three numbers are equal
if num1 == num2 and num1 == num3:
    print("All numbers are equal")
# Check if num1 and num2 are equal and greater than num3
elif num1 == num2 and num1 > num3:
    print("numbers A and B are equal and greater than C. The maximum number is:", num1)
# Check if num2 and num3 are equal and greater than num1
elif num2 == num3 and num2 > num1:
    print("numbers B and C are equal and greater than A. The maximum number is:", num2)
# Check if num1 and num3 are equal and greater than num2
elif num1 == num3 and num1 > num2:
    print("numbers A and C are equal and greater than B. The maximum number is:", num1)
# Check if num1 is the maximum
elif num1 >= num2 and num1 >= num3:
    print("The maximum number is:", num1)
# Check if num2 is the maximum
elif num2 >= num1 and num2 >= num3:
    print("The maximum number is:", num2)
# Otherwise num3 is the maximum
else:
    print("The maximum number is:", num3)
