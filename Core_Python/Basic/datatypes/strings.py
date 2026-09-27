# Program to demonstrate strings in Python

# 1. Creating a string
text = "Python Programming"

print("String:", text)
print("Type:", type(text))

# 2. Accessing characters
print("\nAccessing characters:")
print("First character:", text[0])
print("Last character:", text[-1])

# 3. String slicing
print("\nString slicing:")
print("First 6 characters:", text[0:6])
print("From index 7:", text[7:])
print("Every second character:", text[::2])

# 4. String concatenation
first = "Hello"
second = "Python"

print("\nString concatenation:")
print(first + " " + second)

# 5. String repetition
print("\nString repetition:")
print("Hi " * 3)

# 6. Finding length
print("Length of string:", len(text))

# 7. Changing case
print("\nChanging case:")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# 8. Removing spaces
message = "  Hello Python  "

print("\nRemoving spaces:")
print("Original:", message)
print("After strip():", message.strip())

# 9. Replacing characters
print("\nReplacing text:")
print(text.replace("Python", "Java"))

# 10. Checking a substring
print("\nChecking substring:")
print("Python" in text)
print("Java" in text)

# 11. Splitting a string
print("\nSplitting string:")
words = text.split()
print(words)

# 12. Joining strings
print("\nJoining strings:")
print("-".join(words))