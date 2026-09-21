# Read words from source.txt
with open("source.txt", "r") as source_file:
    words = source_file.read().split()

# Convert all words to lowercase
words = [word.lower() for word in words]

# Sort the words
words.sort()

# Write sorted words to destination.txt
with open("destination.txt", "w") as destination_file:
    for word in words:
        destination_file.write(word + "\n")

print("Words sorted and written to destination.txt")
