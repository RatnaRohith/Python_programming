# Program to demonstrate arrays using a Python list

# Creating an array
numbers = [10, 20, 30, 40, 50]

print("Array elements:")
print(numbers)

# Accessing elements
print("\nFirst element:", numbers[0])
print("Third element:", numbers[2])

# Accessing the last element
print("Last element:", numbers[-1])

# Traversing the array
print("\nArray elements using loop:")
for number in numbers:
    print(number)

# Updating an element
numbers[1] = 25
print("\nAfter updating second element:")
print(numbers)

# Adding an element
numbers.append(60)
print("\nAfter adding 60:")
print(numbers)

# Inserting an element
numbers.insert(2, 35)
print("\nAfter inserting 35 at index 2:")
print(numbers)

# Removing an element
numbers.remove(40)
print("\nAfter removing 40:")
print(numbers)

# Finding length
print("\nLength of array:", len(numbers))

# Finding an element
print("\nPosition of 50:", numbers.index(50))