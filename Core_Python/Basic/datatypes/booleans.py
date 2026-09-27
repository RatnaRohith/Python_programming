# Program to demonstrate Boolean data type

# Creating Boolean variables
a = True
b = False

print("Boolean values:")
print("a =", a)
print("b =", b)

# Checking the data type
print("\nData type of a:", type(a))
print("Data type of b:", type(b))

# Boolean using comparison operators
x = 10
y = 20

print("\nComparison operations:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

# Boolean using logical operators
print("\nLogical operations:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# Boolean in an if statement
print("\nBoolean in if statement:")
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")