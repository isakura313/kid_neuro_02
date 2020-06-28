import numpy as np


#создать простую матрицу

matrix = np.array([[1,2],
                   [2, 3]])
matrix2 = np.array([[2,3],
                    [3,4]])

print(matrix)
print(matrix2)
print(np.dot(matrix, matrix2))