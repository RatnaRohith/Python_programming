# Program to demonstrate sets

# Creating a set
numbers = {10, 20, 30, 40, 50}

print("Original Set:")
print(numbers)


# Adding an element
numbers.add(60)

print("\nAfter adding an element:")
print(numbers)


# Adding multiple elements
numbers.update([70, 80])

print("\nAfter adding multiple elements:")
print(numbers)


# Removing an element
numbers.remove(30)

print("\nAfter removing 30:")
print(numbers)


# Discarding an element
numbers.discard(100)

print("\nAfter discard():")
print(numbers)


# Checking whether an element exists
if 40 in numbers:
    print("\n40 is present in the set")


# Finding the length
print("\nNumber of elements:", len(numbers))


# Traversing the set
print("\nElements in the set:")
for number in numbers:
    print(number)


# Creating another set
numbers2 = {40, 50, 60, 90}

print("\nSecond Set:")
print(numbers2)


# Union
print("\nUnion:")
print(numbers.union(numbers2))


# Intersection
print("\nIntersection:")
print(numbers.intersection(numbers2))


# Difference
print("\nDifference:")
print(numbers.difference(numbers2))


# Symmetric Difference
print("\nSymmetric Difference:")
print(numbers.symmetric_difference(numbers2))


# Clear the set
numbers.clear()

print("\nAfter clearing the set:")
print(numbers)