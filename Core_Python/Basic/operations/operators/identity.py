# Program to demonstrate identity operators

# Creating two lists
list1 = [10, 20, 30]
list2 = [10, 20, 30]

# Assigning list1 to list3
list3 = list1

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

# Using 'is'
print("\nIdentity Operator 'is':")
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

# Using 'is not'
print("\nIdentity Operator 'is not':")
print("list1 is not list2:", list1 is not list2)
print("list1 is not list3:", list1 is not list3)

# Comparing values using ==
print("\nComparison using ==:")
print("list1 == list2:", list1 == list2)
print("list1 == list3:", list1 == list3)