# Demonstrate dictionary in Python

# Creating a dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "course": "AIML",
    "marks": 85
}

# Display the dictionary
print("Student Dictionary:")
print(student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

# Adding a new key-value pair
student["city"] = "Hyderabad"
print("\nAfter adding city:")
print(student)

# Updating a value
student["marks"] = 90
print("\nAfter updating marks:")
print(student)

# Removing a key-value pair
student.pop("age")
print("\nAfter removing age:")
print(student)

# Displaying keys
print("\nKeys:")
print(student.keys())

# Displaying values
print("\nValues:")
print(student.values())

# Displaying key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)