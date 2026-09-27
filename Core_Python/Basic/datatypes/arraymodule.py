# Program to demonstrate arrays in Python

from array import array

# Create an integer array
numbers = array('i', [10, 20, 30, 40, 50])

print("Array elements:")
print(numbers)

# Accessing array elements
print("\nFirst element:", numbers[0])
print("Third element:", numbers[2])

# Traversing the array
print("\nArray elements using loop:")
for element in numbers:
    print(element)

# Adding an element
numbers.append(60)
print("\nAfter adding 60:")
print(numbers)

# Inserting an element
numbers.insert(2, 25)
print("\nAfter inserting 25 at index 2:")
print(numbers)

# Updating an element
numbers[0] = 5
print("\nAfter updating first element:")
print(numbers)

# Removing an element
numbers.remove(40)
print("\nAfter removing 40:")
print(numbers)

# Finding the length
print("\nLength of array:", len(numbers))