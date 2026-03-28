# Program to swap two numbers WITHOUT using a temporary variable
# Method: Using multiplication and integer division

# Initialize two variables
a = 20
b = 30
print("Before swapping: a =", a, "b =", b)

# Swapping using multiplication/division without temporary variable
# Step 1: Store product of both numbers in a
a = a * b
# Step 2: Store quotient in b (original a value)
b = a // b
# Step 3: Store quotient in a (original b value)
a = a // b

print("After swapping: a =", a, "b =", b)   