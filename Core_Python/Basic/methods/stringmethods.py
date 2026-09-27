# Program to demonstrate string methods

text = "Python Programming"

# 1. upper() - converts string to uppercase
print("Uppercase:", text.upper())

# 2. lower() - converts string to lowercase
print("Lowercase:", text.lower())

# 3. capitalize() - capitalizes the first character
print("Capitalize:", text.capitalize())

# 4. title() - converts first letter of each word to uppercase
print("Title:", text.title())

# 5. swapcase() - changes uppercase to lowercase and vice versa
print("Swapcase:", text.swapcase())

# 6. replace() - replaces a substring
print("Replace:", text.replace("Python", "Java"))

# 7. find() - finds the position of a substring
print("Find:", text.find("Programming"))

# 8. count() - counts occurrences of a substring
print("Count:", text.count("m"))

# 9. startswith() - checks starting characters
print("Starts with Python:", text.startswith("Python"))

# 10. endswith() - checks ending characters
print("Ends with ing:", text.endswith("ing"))

# 11. split() - splits the string into a list
print("Split:", text.split())

# 12. strip() - removes spaces from beginning and end
new_text = "   Hello Python   "
print("Strip:", new_text.strip())

# 13. isalpha() - checks whether all characters are alphabets
print("Is alphabet:", "Python".isalpha())

# 14. isdigit() - checks whether all characters are digits
print("Is digit:", "12345".isdigit())

# 15. isalnum() - checks whether all characters are alphabets or digits
print("Is alphanumeric:", "Python123".isalnum())