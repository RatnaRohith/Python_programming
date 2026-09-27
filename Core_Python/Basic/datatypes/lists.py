# Program to demonstrate lists

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("List of fruits:")
print(fruits)

# Accessing elements
print("\nFirst fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding an element
fruits.append("Grapes")
print("\nAfter adding an element:")
print(fruits)

# Inserting an element
fruits.insert(1, "Pineapple")
print("\nAfter inserting an element:")
print(fruits)

# Updating an element
fruits[2] = "Papaya"
print("\nAfter updating an element:")
print(fruits)

# Removing an element
fruits.remove("Orange")
print("\nAfter removing an element:")
print(fruits)

# Finding length
print("\nNumber of elements:", len(fruits))

# Slicing
print("\nFirst three elements:")
print(fruits[:3])

# Traversing the list
print("\nElements in the list:")
for fruit in fruits:
    print(fruit)