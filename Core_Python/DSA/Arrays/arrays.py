# Program to demonstrate arrays

# Creating an array
numbers = [10, 20, 30, 40, 50]

# Displaying the array
print("Array elements:", numbers)

# Accessing array elements
print("First element:", numbers[0])
print("Third element:", numbers[2])

# Changing an element
numbers[1] = 25
print("After changing second element:", numbers)

# Adding an element
numbers.append(60)
print("After adding an element:", numbers)

# Removing an element
numbers.remove(30)
print("After removing an element:", numbers)

# Finding the length
print("Length of array:", len(numbers))