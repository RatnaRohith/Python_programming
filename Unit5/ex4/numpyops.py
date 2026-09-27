import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

# 1. Basic Slicing
print("\nBasic Slicing:")

print("Elements from index 1 to 4:", arr[1:5])
print("First three elements:", arr[:3])
print("Elements from index 2:", arr[2:])
print("Every second element:", arr[::2])

# 2. Integer Indexing
print("\nInteger Indexing:")

print("Element at index 0:", arr[0])
print("Element at index 3:", arr[3])

# Selecting multiple elements using integer indices
indices = [0, 2, 5]
print("Elements at indices 0, 2 and 5:", arr[indices])

# 3. Boolean Indexing
print("\nBoolean Indexing:")

condition = arr > 30

print("Boolean condition:", condition)
print("Elements greater than 30:", arr[condition])

# Another Boolean condition
print("Even elements:", arr[arr % 2 == 0])