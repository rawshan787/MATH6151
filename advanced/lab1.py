import numpy as np
import matplotlib

# slide 9
'''
print((1.2 + 3.4 - (5.6 * 7.8)**(9/11)) / 12)



x = np.array([1, 2, 5])

print(x)
print(len(x))
print(np.sum(x))
print(np.sin(np.pi * x)**2)
'''

'''
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A.size)
print(A.shape)
print(A)
print(np.transpose(A))
print(np.dot(A, x))
print(A @ x)
print(A * A) # Element-wise multiplication!
'''

### Questions for Lab 1 (easy version) 
## Question 5 
# define the vector v as v = (1,2) as a numpy array and check its shape and length.
v = np.array([1, 2])
print(v)
print(v.shape)
print(len(v))

# using numpy, compute the sum of all its entries.
print(np.sum(v))

## Question 6
# define the matrix A as A = [[2,6],[3,5]] as a numpy array and check its shape and size.
A = np.array([[2, 3], [6, 5]])
print(A)
print(A.shape)
print(A.size)

# using numpy, compute matrix A multiplited by vector v
print(A @ v)

## Question 7
# using linalg package with numpy, compute the eigenvalues and eigenvectors of A.
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

