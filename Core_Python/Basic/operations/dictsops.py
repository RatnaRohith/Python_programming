# Program to demonstrate different dictionary operations

# 1. Create a dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "course": "AIML",
    "marks": 85
}

print("Original Dictionary:")
print(student)


# 2. Accessing dictionary elements
print("\nAccessing Elements:")
print("Name:", student["name"])
print("Marks:", student["marks"])


# 3. Adding a new key-value pair
student["city"] = "Hyderabad"

print("\nAfter Adding an Element:")
print(student)


# 4. Updating an existing value
student["marks"] = 90

print("\nAfter Updating Marks:")
print(student)


# 5. Using update() method
student.update({"age": 21})

print("\nAfter Using update():")
print(student)


# 6. Removing an element using pop()
student.pop("city")

print("\nAfter Removing City:")
print(student)


# 7. Removing the last inserted element using popitem()
student.popitem()

print("\nAfter popitem():")
print(student)


# 8. Checking whether a key exists
if "name" in student:
    print("\n'name' key exists in the dictionary")


# 9. Displaying all keys
print("\nKeys:")
print(student.keys())


# 10. Displaying all values
print("\nValues:")
print(student.values())


# 11. Displaying key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)


# 12. Finding the length of dictionary
print("\nNumber of Elements:", len(student))


# 13. Clearing the dictionary
student.clear()

print("\nAfter Clearing Dictionary:")
print(student)