import numpy as np

matrix_2x2_1 = np.array([[2, 1],
                         [3, 2]])
matrix_2x2_1_inv = np.array([[2, -1],
                             [-3, 2]])
x_vector_column_2x2_1 = np.array([3, -3])

matrix_2x2_2 = np.array([[4, 3],
                         [5, 4]])
matrix_2x2_2_inv = np.array([[4, -3],
                             [-5, 4]])
x_vector_column_2x2_2 = np.array([1, 1])

matrix_3x3_1 = np.array([[1, 2, 3],
                         [0, 1, 4],
                         [5, 6, 0]])
matrix_3x3_1_inv = np.array([[-24, 18, 5],
                             [20, -15, -4],
                             [-5, 4, 1]])
x_vector_column_3x3_1 = np.array([1, 0, 1])

matrix_3x3_2 = np.array([[3, 1, 0],
                         [2, 4, 1],
                         [5, 6, 2]])
matrix_3x3_2_inv = np.array([[8, -6, -1],
                             [-5, 4, 1],
                             [-9, 7, 1]])
x_vector_column_3x3_2 = np.array([0, 1, 1])

matrix_4x4_1 = np.array([[1, 2, 3, 4],
                         [0, 1, 4, 5],
                         [6, 7, 0, 8],
                         [9, 10, 11, 0]])
matrix_4x4_1_inv = np.array([[24, -23, 14, -5],
                             [-20, 19, -12, 4],
                             [-5, 5, -3, 1],
                             [15, -14, 9, -3]])
x_vector_column_4x4_1 = np.array([1, 1, 0, 1])

matrix_4x4_2 = np.array([[4, 3, 2, 1],
                         [1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]])
matrix_4x4_2_inv = np.array([[-6, 5, -4, 1],
                             [5, -4, 3, -1],
                             [1, 0, -1, 0],
                             [-1, 1, 1, -1]])
x_vector_column_4x4_2 = np.array([0, 1, 1, 0])
