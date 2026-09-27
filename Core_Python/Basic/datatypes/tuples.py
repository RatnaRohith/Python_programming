# Program to demonstrate tuples

# 1. Creating a tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple:")
print(numbers)


# 2. Accessing elements
print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])


# 3. Tuple slicing
print("\nTuple slicing:")
print(numbers[1:4])


# 4. Finding the length
print("\nLength of tuple:", len(numbers))


# 5. Counting an element
print("\nCount of 20:", numbers.count(20))


# 6. Finding the index of an element
print("Index of 30:", numbers.index(30))


# 7. Checking whether an element exists
if 40 in numbers:
    print("\n40 is present in the tuple")


# 8. Traversing the tuple
print("\nElements of tuple:")
for number in numbers:
    print(number)


# 9. Tuple with different data types
student = ("Ravi", 20, "AIML", 85.5)

print("\nTuple with different data types:")
print(student)


# 10. Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))

print("\nNested tuple:")
print(nested_tuple)