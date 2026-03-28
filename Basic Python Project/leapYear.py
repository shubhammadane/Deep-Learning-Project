# Program to check if a year is a leap year
# A leap year is divisible by 4, but not by 100, unless also divisible by 400

# Input the year from user
num = int(input("Enter a year: "))

# Check leap year condition
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(num, "is a leap year.")
else:
    print(num, "is not a leap year.")