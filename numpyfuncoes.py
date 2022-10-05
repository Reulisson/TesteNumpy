import numpy as np

# Criando matriz 3x3
X = np.array([[3, 2, 5], [4, 1, 3], [2, 3, 4]])
Y = np.array([[1, 5, 3], [2, 4, 7], [4, 6, 2]])

# Criando matriz 2x2
Z = np.array([[4, -3], [6, -1]])

# Criando matriz 3x3
W = np.array([[1, 7, 3, 1], [6, 3, 9, 0], [2, 7, 4, 5], [1, 9, 9, 4]])

# Determinante
print('\nDeterminante')
det_X = np.linalg.det(X)
print(det_X)
det_Y = np.linalg.det(Y)
print(det_Y)
det_Z = np.linalg.det(Z)
print(det_Z)
det_W = np.linalg.det(W)
print(det_W)

# Matriz inversa
print('\nMatriz inversa')
inv_X = np.linalg.inv(X)
print(inv_X)
inv_Y = np.linalg.inv(Y)
print(inv_Y)
inv_Z = np.linalg.inv(Z)
print(inv_Z)
inv_W = np.linalg.inv(W)
print(inv_W)

# Matriz transposta
print('\nMatriz transposta')
transp_X = X.T
print(transp_X)
transp_Y = Y.T
print(transp_Y)
trasnp_Z = Z.T
print(trasnp_Z)
transp_W = W.T
print(transp_W)

# Traço da matriz
print('Traço da matriz')
traco_X = np.trace(X)
print(traco_X)
traco_Y = np.trace(Y)
print(traco_Y)
traco_Z = np.trace(Z)
print(traco_Z)
traco_W = np.trace(W)
print(traco_W)
