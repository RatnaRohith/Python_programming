# Define two matrices
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Matrix Addition
addition = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]

# Transpose of Matrix A
transpose = [
    [A[j][i] for j in range(len(A))]
    for i in range(len(A[0]))
]

# Matrix Multiplication
multiplication = [
    [
        sum(A[i][k] * B[k][j] for k in range(len(B)))
        for j in range(len(B[0]))
    ]
    for i in range(len(A))
]

# Display results
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition of A and B:")
for row in addition:
    print(row)

print("\nTranspose of Matrix A:")
for row in transpose:
    print(row)

print("\nMultiplication of A and B:")
for row in multiplication:
    print(row)
