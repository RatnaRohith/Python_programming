# Create a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "college": "ABC Engineering College"
}

# Get the key from the user
key = input("Enter the key to search: ")

# Check whether the key exists
if key in student:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
