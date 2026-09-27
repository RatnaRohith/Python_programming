# Program to demonstrate different operations on strings

text = "Python Programming"

print("Original String:", text)

# 1. Length of string
print("\n1. Length:", len(text))

# 2. Indexing
print("2. First character:", text[0])
print("   Last character:", text[-1])

# 3. Slicing
print("3. First 6 characters:", text[:6])
print("   Characters from index 7:", text[7:])
print("   Reverse string:", text[::-1])

# 4. Concatenation
text1 = "Python"
text2 = "Programming"
print("4. Concatenation:", text1 + " " + text2)

# 5. Repetition
print("5. Repetition:", "Python " * 3)

# 6. Membership operation
print("6. Is 'Python' present?", "Python" in text)
print("   Is 'Java' present?", "Java" in text)

# 7. Comparison
str1 = "apple"
str2 = "banana"
print("7. Are strings equal?", str1 == str2)
print("   Is str1 smaller than str2?", str1 < str2)

# 8. Convert to uppercase
print("8. Uppercase:", text.upper())

# 9. Convert to lowercase
print("9. Lowercase:", text.lower())

# 10. Capitalize
print("10. Capitalize:", text.capitalize())

# 11. Replace
print("11. Replace:", text.replace("Python", "Java"))

# 12. Find
print("12. Position of 'Programming':", text.find("Programming"))

# 13. Count
print("13. Count of 'm':", text.count("m"))

# 14. Split
print("14. Split:", text.split())

# 15. Join
words = ["Python", "is", "easy"]
print("15. Join:", " ".join(words))

# 16. Remove spaces
text_with_spaces = "   Python   "
print("16. Strip spaces:", text_with_spaces.strip())

# 17. Check starting and ending characters
print("17. Starts with 'Python':", text.startswith("Python"))
print("   Ends with 'ing':", text.endswith("ing"))

# 18. Check string properties
print("18. Is alphabetic?", "Python".isalpha())
print("   Is numeric?", "12345".isnumeric())
print("   Is alphanumeric?", "Python123".isalnum())