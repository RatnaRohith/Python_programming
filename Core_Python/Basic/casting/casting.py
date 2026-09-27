# Program to demonstrate various types of casting in Python

# 1. Integer to Float
a = 10
b = float(a)

print("Integer to Float:")
print("Original value:", a)
print("Converted value:", b)
print("Type:", type(b))

# 2. Float to Integer
x = 15.75
y = int(x)

print("\nFloat to Integer:")
print("Original value:", x)
print("Converted value:", y)
print("Type:", type(y))

# 3. Integer to String
num = 100
text = str(num)

print("\nInteger to String:")
print("Original value:", num)
print("Converted value:", text)
print("Type:", type(text))

# 4. String to Integer
value = "250"
number = int(value)

print("\nString to Integer:")
print("Original value:", value)
print("Converted value:", number)
print("Type:", type(number))

# 5. String to Float
value = "25.50"
number = float(value)

print("\nString to Float:")
print("Original value:", value)
print("Converted value:", number)
print("Type:", type(number))

# 6. List to Tuple
my_list = [10, 20, 30]
my_tuple = tuple(my_list)

print("\nList to Tuple:")
print("Original value:", my_list)
print("Converted value:", my_tuple)
print("Type:", type(my_tuple))

# 7. Tuple to List
my_tuple = (10, 20, 30)
my_list = list(my_tuple)

print("\nTuple to List:")
print("Original value:", my_tuple)
print("Converted value:", my_list)
print("Type:", type(my_list))

# 8. List to Set
my_list = [10, 20, 20, 30]
my_set = set(my_list)

print("\nList to Set:")
print("Original value:", my_list)
print("Converted value:", my_set)
print("Type:", type(my_set))