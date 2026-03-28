# Program to swap two numbers WITHOUT using a temporary variable
# Method: Using addition and subtraction

# Initialize two variables
a = 20
b = 30
print("Before swapping: a =", a, "b =", b)

# Swapping using addition/subtraction without temporary variable
# Step 1: Store sum of both numbers in a
a = a + b
# Step 2: Store difference in b (original a value)
b = a - b
# Step 3: Store difference in a (original b value)
a = a - b

print("After swapping: a =", a, "b =", b)   