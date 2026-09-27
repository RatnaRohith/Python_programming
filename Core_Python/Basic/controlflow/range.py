# Program to demonstrate range() in different ways

# 1. range(stop)
print("1. range(stop):")
for i in range(5):
    print(i)

# 2. range(start, stop)
print("\n2. range(start, stop):")
for i in range(2, 8):
    print(i)

# 3. range(start, stop, step)
print("\n3. range(start, stop, step):")
for i in range(2, 10, 2):
    print(i)

# 4. range with negative step
print("\n4. range with negative step:")
for i in range(10, 0, -2):
    print(i)

# 5. Reverse range
print("\n5. Reverse range:")
for i in range(5, 0, -1):
    print(i)

# 6. Range with step 3
print("\n6. Range with step 3:")
for i in range(1, 15, 3):
    print(i)

# 7. Convert range into a list
print("\n7. Convert range into list:")
numbers = list(range(1, 6))
print(numbers)