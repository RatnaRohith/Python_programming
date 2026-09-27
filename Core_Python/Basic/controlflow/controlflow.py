# Demonstration of Control Flow in Python

# 1. Sequential statement
print("Program started")

number = 10
print("Number:", number)


# 2. if statement
if number > 0:
    print("The number is positive")


# 3. if-else statement
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# 4. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")


# 5. for loop
print("\nFor Loop:")
for i in range(1, 6):
    print(i)


# 6. while loop
print("\nWhile Loop:")
i = 1

while i <= 5:
    print(i)
    i += 1


# 7. break statement
print("\nBreak Statement:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 8. continue statement
print("\nContinue Statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 9. pass statement
print("\nPass Statement:")

for i in range(1, 4):
    if i == 2:
        pass
    print(i)

print("Program ended")