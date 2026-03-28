# Program to swap two numbers USING a temporary variable

# Initialize two variables
a = 20
b = 30
print("Before swapping: a =", a, "b =", b)

# Swapping using a temporary variable
# Step 1: Store value of a in temp
temp = a
# Step 2: Copy b to a
a = b
# Step 3: Copy temp (original a value) to b
b = temp

print("After swapping: a =", a, "b =", b)   