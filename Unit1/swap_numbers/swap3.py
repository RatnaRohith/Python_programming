# Program to swap two numbers using multiple assignment

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping using multiple assignment
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
