# Count the number of vowels in a string

string = input("Enter a string: ")

vowel_count = (
    string.lower().count('a') +
    string.lower().count('e') +
    string.lower().count('i') +
    string.lower().count('o') +
    string.lower().count('u')
)

print("Number of vowels:", vowel_count)
