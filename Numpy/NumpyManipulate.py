import numpy as np
from numpy.ma.core import reshape, transpose

a= np.arange(1,7)
print("original array",a)

reshaped = a.reshape(2,3)
print(reshaped)

arr = np.array([[1,2],[3,4]])
#flat
for x in arr.flat:
    print(x)


#flatten
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr =arr.flatten()
print(at_arr)

#ravel
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)


#pad
arr = np.array([1,2,3])
padded= np.pad(arr,2,mode='constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#transpose

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)


#rollaxis
arr =np.zeros((2,3,4))
print(arr)


new_arr = np.rollaxis(arr,2)
print(new_arr)

#swapaxis
arr =np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr,0,2)
print(new_arr)

#moveaxis
arr =np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr,0,-1)
print(new_arr)

#joining arrays
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(np.concatenate((a,b),axis = 0))
print(np.concatenate((a,b),axis = 1))

#stack
a = np.array([1,2,3])
b= np.array([4,5,6])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

#hstack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis = 1))

#vstack
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis = 0))


#column stack
a = np.array([1,2,3])
b= np.array([4,5,6])
print(np.column_stack((a,b)))

#row stack
print(np.vstack((a,b)))

#splitting
arr = np.array([1,2,3,4,5,6])
result = np.split(arr,3)
print(result)

#hsplit
arr2 = np.array([[1,2,3,4],
                [5,6,7,8]])
print(np.hsplit(arr2,2))

#vsplit
arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])
print(np.vsplit(arr2,2))

arr = np.array([1,2,3,4,5])
print(np.array_split(arr,3))

#adding /removing
#resize
arr = np.array([1,2,3,4])
new_arr = np.resize(arr,(2,3))
print(new_arr)
#append()
arr = np.array([1,2,3])
new_arr = np.append(arr,[4,5])
print(new_arr)

#2d array
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

print(np.append(a,b, axis=0))
#insert
arr = np.array([10,20,30])
new_arr = np.insert(arr,2,15)
print(new_arr)

#delete
arr = np.array([10,20,30])
new_arr = np.delete(arr,2)
print(new_arr)


arr = np.array([1,2,2,3,4,5,4,5])
print(np.unique(arr))
#reapting
arr = np.array([1,2,3])
print(np.repeat(arr,3))

#different repeats
arr = np.array([10,20,30])
print(np.repeat(arr,[1,2,3]))

#repeat in 2D array
arr2 = np.array([[1,2],[3,4]])
print(np.repeat(arr2,2,axis=0))

#tile
my_array = np.array([1,2,3])
tiled_array = np.tile(my_array,2)
print(my_array)
print(tiled_array)

#flip()
arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
aar2 = np.array([[1,2],[3,4]])

print(np.flip(arr2,axis=0))#flip rows
print(np.flip(arr2,axis=1))#flip columns

#fliplr
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.fliplr(arr2))

#flipud
print(np.flipud(arr2))

#roll
arr2 = np.array([[1,2,3],[4,5,6]])
np.roll(arr2,2,axis=None)


#Sorting n Searching
#sort() returns a sorted copy of an array(or sorts in-place if using ndarray method).
arr=np.array([5,2,9,1])
sorted_arr=np.sort(arr)
print(sorted_arr)

#argsort()- Returns the indices that would sort the array return the index positions
arr=np.array([5,2,9,1])
sorted_arr=np.sort(arr)
print(sorted_arr)
indices=np.argsort(arr)
print(indices)

#lexsort- used for sorting with mutiple columns (like sorting by last name, then first name)
#sort by first
#then by b(secordary key)
#sorting happens from right to left
a=np.array([1,1,0,0])
b=np.array([1,0,1,0])
result=np.lexsort((b,a))
print(result)




