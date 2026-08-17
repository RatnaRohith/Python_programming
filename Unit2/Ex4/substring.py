# Program to check whether a substring is present in a string

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in string:
    print("Substring is present in the given string")
else:
    print("Substring is not present in the given string")