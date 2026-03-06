'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''
import  numpy as np
from numpy.ma.core import identity

a = np.zeros(5)
print(a)

a_2D = np.zeros((4,3))
print(a_2D)

a = np.ones(5)
print(a)

a_2D = np.ones((4,3))
print(a_2D)

a = np.arange( 1, 10, 2)
print(a)


a = np.linspace(0,10, num = 5, endpoint = True)
print(a)

a = np.linspace(0, 10, num = 5, endpoint = False)
print(a)

a = np.random.rand(5)
print(a)

a = np.random.rand(2,3)
print(a)

a = np.random.rand(2,3,4)
print(a)

a = np.empty((2,3))
print(a)

a = np.full((2,3), 5)
print(a)

#numpy.eye
identity_matrix =np.eye((4))
print(identity_matrix)
#numpy.identity
identity_matrix =np.identity((5))
print(identity_matrix)
#numpy.diagona
matrix =np.array([[10,20,30],[40,50,60],[70,80,90]])
print("original matrix",matrix)
diagonal_elements = np.diag(matrix)
print("diagonal element",diagonal_elements)

