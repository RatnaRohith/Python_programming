import pandas as pd

# Create a dictionary with 5 keys
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma",
             "Frank", "Grace", "Henry", "Ivy", "Jack"],

    "Age": [20, 21, 19, 22, 20, 23, 21, 19, 22, 20],

    "Department": ["CSE", "ECE", "CSE", "EEE", "IT",
                   "CSE", "ECE", "IT", "EEE", "CSE"],

    "Marks": [85, 78, 92, 70, 88, 95, 76, 89, 81, 90],

    "City": ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune",
             "Bangalore", "Hyderabad", "Delhi", "Pune", "Mumbai"]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

# 1. Apply head() function
print("\nFirst 5 rows using head():")
print(df.head())

# Display first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# 2. Data Selection Operations

# Select a single column
print("\nName column:")
print(df["Name"])

# Select multiple columns
print("\nName and Marks columns:")
print(df[["Name", "Marks"]])

# Select rows using loc
print("\nRows 0 to 2 using loc:")
print(df.loc[0:2])

# Select specific rows and columns using loc
print("\nName and Marks for rows 0 to 2:")
print(df.loc[0:2, ["Name", "Marks"]])

# Select rows using iloc
print("\nFirst 3 rows using iloc:")
print(df.iloc[0:3])

# Select specific rows and columns using iloc
print("\nFirst 3 rows and first 2 columns:")
print(df.iloc[0:3, 0:2])

# Select rows based on a condition
print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])

# Select students from CSE department
print("\nStudents from CSE department:")
print(df[df["Department"] == "CSE"])