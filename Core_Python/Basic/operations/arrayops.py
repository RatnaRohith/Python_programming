# Program to demonstrate different operations on arrays

# Creating an array using a list
numbers = [50, 20, 40, 10, 30]

print("Original Array:")
print(numbers)

# 1. Accessing elements
print("\n1. Accessing Elements:")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# 2. Updating an element
numbers[1] = 25
print("\n2. After Updating Second Element:")
print(numbers)

# 3. Adding an element
numbers.append(60)
print("\n3. After Adding 60:")
print(numbers)

# 4. Inserting an element
numbers.insert(2, 35)
print("\n4. After Inserting 35 at Index 2:")
print(numbers)

# 5. Removing an element
numbers.remove(40)
print("\n5. After Removing 40:")
print(numbers)

# 6. Deleting an element using index
del numbers[0]
print("\n6. After Deleting First Element:")
print(numbers)

# 7. Searching for an element
search = 30

if search in numbers:
    print("\n7. Search:")
    print(search, "is present in the array")
else:
    print(search, "is not present in the array")

# 8. Finding length
print("\n8. Length of Array:")
print(len(numbers))

# 9. Sorting the array
numbers.sort()
print("\n9. Array in Ascending Order:")
print(numbers)

# 10. Reversing the array
numbers.reverse()
print("\n10. Array in Reverse Order:")
print(numbers)

# 11. Traversing the array
print("\n11. Traversing the Array:")
for element in numbers:
    print(element)