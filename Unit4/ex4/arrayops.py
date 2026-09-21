from array import array

# Create an array
numbers = array('i', [10, 20, 30, 40])

# Display the array
print("Original array:", numbers)

# Append an item
numbers.append(50)
print("After appending 50:", numbers)

# Insert an item at index 2
numbers.insert(2, 25)
print("After inserting 25:", numbers)

# Reverse the array
numbers.reverse()
print("After reversing:", numbers)
