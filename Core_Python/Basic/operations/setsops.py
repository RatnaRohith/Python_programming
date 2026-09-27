# Program to demonstrate different operations on sets

# 1. Creating sets
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("Set 1:", set1)
print("Set 2:", set2)


# 2. Adding an element
set1.add(60)

print("\nAfter adding 60 to Set 1:")
print(set1)


# 3. Adding multiple elements
set1.update([70, 80])

print("\nAfter adding multiple elements:")
print(set1)


# 4. Removing an element
set1.remove(30)

print("\nAfter removing 30:")
print(set1)


# 5. Discarding an element
set1.discard(100)

print("\nAfter discard(100):")
print(set1)


# 6. Checking membership
print("\nMembership Operation:")
if 40 in set1:
    print("40 is present in Set 1")


# 7. Union
union_set = set1.union(set2)

print("\nUnion of Set 1 and Set 2:")
print(union_set)


# 8. Intersection
intersection_set = set1.intersection(set2)

print("\nIntersection of Set 1 and Set 2:")
print(intersection_set)


# 9. Difference
difference_set = set1.difference(set2)

print("\nDifference of Set 1 and Set 2:")
print(difference_set)


# 10. Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)

print("\nSymmetric Difference:")
print(symmetric_difference_set)


# 11. Subset
set3 = {40, 50}

print("\nIs Set 3 a subset of Set 1?")
print(set3.issubset(set1))


# 12. Superset
print("\nIs Set 1 a superset of Set 3?")
print(set1.issuperset(set3))


# 13. Length of a set
print("\nNumber of elements in Set 1:")
print(len(set1))


# 14. Traversing a set
print("\nElements of Set 1:")
for value in set1:
    print(value)


# 15. Clearing a set
set1.clear()

print("\nSet 1 after clear():")
print(set1)