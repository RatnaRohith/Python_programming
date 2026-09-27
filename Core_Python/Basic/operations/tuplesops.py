# Program to demonstrate different operations on tuples

# 1. Creating tuples
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)


# 2. Accessing elements
print("\nFirst element:", tuple1[0])
print("Last element:", tuple1[-1])


# 3. Slicing
print("\nSlicing tuple1:")
print(tuple1[1:4])


# 4. Concatenation
tuple3 = tuple1 + tuple2

print("\nAfter concatenation:")
print(tuple3)


# 5. Repetition
tuple4 = (1, 2, 3) * 2

print("\nAfter repetition:")
print(tuple4)


# 6. Finding length
print("\nLength of tuple1:", len(tuple1))


# 7. Counting an element
tuple5 = (10, 20, 20, 30, 20)

print("\nCount of 20:", tuple5.count(20))


# 8. Finding index
print("Index of 30:", tuple5.index(30))


# 9. Membership operation
print("\nMembership operation:")

if 40 in tuple1:
    print("40 is present in tuple1")

if 100 not in tuple1:
    print("100 is not present in tuple1")


# 10. Comparing tuples
print("\nTuple comparison:")

if tuple1 == tuple2:
    print("Both tuples are equal")
else:
    print("Both tuples are not equal")


# 11. Traversing a tuple
print("\nElements of tuple1:")

for value in tuple1:
    print(value)


# 12. Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))

print("\nNested tuple:")
print(nested_tuple)

print("First nested tuple:", nested_tuple[0])
print("First element of first nested tuple:", nested_tuple[0][0])


# 13. Tuple unpacking
student = ("Ravi", 20, "AIML")

name, age, course = student

print("\nTuple Unpacking:")
print("Name:", name)
print("Age:", age)
print("Course:", course)