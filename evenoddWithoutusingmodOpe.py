# Program to check if a number is even or odd witghout using modulus operator
# Input the number from user
num= int(input("Enter a number: "))

# Check if the number is divisible by 2
if num // 2 * 2 == num:    
    # Print if the number is even
    print(num, "is an even number.")        
else:    
    # Print if the number is odd
    print(num, "is an odd number.")