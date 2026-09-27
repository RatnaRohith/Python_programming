# Program to demonstrate different operations on lists

# 1. Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:")
print(numbers)


# 2. Accessing elements
print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])


# 3. List slicing
print("\nSlicing:")
print(numbers[1:4])


# 4. Adding an element using append()
numbers.append(60)

print("\nAfter append():")
print(numbers)


# 5. Inserting an element
numbers.insert(2, 25)

print("\nAfter insert():")
print(numbers)


# 6. Adding multiple elements using extend()
numbers.extend([70, 80])

print("\nAfter extend():")
print(numbers)


# 7. Updating an element
numbers[0] = 5

print("\nAfter updating first element:")
print(numbers)


# 8. Removing an element using remove()
numbers.remove(25)

print("\nAfter remove():")
print(numbers)


# 9. Removing an element using pop()
numbers.pop()

print("\nAfter pop():")
print(numbers)


# 10. Finding the length
print("\nLength of list:", len(numbers))


# 11. Searching for an element
if 40 in numbers:
    print("40 is present in the list")


# 12. Finding the index
print("Index of 40:", numbers.index(40))


# 13. Counting elements
numbers.append(40)
print("Count of 40:", numbers.count(40))


# 14. Sorting the list
numbers.sort()

print("\nAfter sorting:")
print(numbers)


# 15. Reversing the list
numbers.reverse()

print("\nAfter reversing:")
print(numbers)


# 16. Copying the list
new_list = numbers.copy()

print("\nCopied List:")
print(new_list)


# 17. Clearing the list
numbers.clear()

print("\nAfter clear():")
print(numbers)