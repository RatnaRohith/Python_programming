import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary
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

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Select two columns
x = df["Age"]
y = df["Marks"]

# Display selected columns
print("Selected columns:")
print(df[["Age", "Marks"]])

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")

# Display the plot
plt.show()