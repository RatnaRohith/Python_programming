# Program to demonstrate strings

# Creating strings
name = "Python"
message = 'Welcome to Python Programming'

print("String 1:", name)
print("String 2:", message)

# String indexing
print("\nFirst character:", name[0])
print("Last character:", name[-1])

# String slicing
print("\nFirst three characters:", name[0:3])
print("Characters from index 2:", name[2:])

# String concatenation
first_name = "Hello"
last_name = "World"
full_name = first_name + " " + last_name
print("\nConcatenation:", full_name)

# String repetition
print("Repetition:", "Python " * 3)

# String length
print("Length of name:", len(name))

# Changing case
print("\nUppercase:", name.upper())
print("Lowercase:", name.lower())

# Removing spaces
text = "   Python Programming   "
print("Stripped string:", text.strip())

# Finding a substring
print("\nPosition of 'thon':", name.find("thon"))

# Replacing text
print("Replace:", message.replace("Python", "AI"))

# Checking substring
print("\nIs 'Python' present?", "Python" in message)

# Splitting a string
words = message.split()
print("Split string:", words)