with open("source.txt", "r") as file:
    for line in file:
        print(line.rstrip()[::-1])
