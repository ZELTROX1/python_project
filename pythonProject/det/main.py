import numpy as np

# Define your matrix
matrix = np.array([[0,2,0,0],[1,1,0,0],[2,3,0,1],[5,3,23,10]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

print("Determinant:", determinant)
