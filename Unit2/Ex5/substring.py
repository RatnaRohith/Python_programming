# Program to perform addition, insertion and slicing operations on a list

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# i) Addition - adding an element using append()
numbers.append(60)
print("After Addition:", numbers)

# ii) Insertion - inserting an element at a specific position
numbers.insert(2, 25)
print("After Insertion:", numbers)

# iii) Slicing - extracting a portion of the list
sliced_list = numbers[1:5]
print("After Slicing:", sliced_list)