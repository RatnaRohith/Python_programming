with open("source.txt", "r") as file:
    text = file.read()

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of lines:", lines)
