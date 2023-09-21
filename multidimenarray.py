from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 9, 4, 3, 7])
arr = arr1 + arr2
# deep copy - two different arrays and one does not affect the other
arr3 = arr1.copy()
arr1[1] = 4
# shallow copy - once an array1 is copied into a different array2. when you change the values of array one array 2
# why does it affect array1 if any change done on array2 - since in shallow copy id will be same and two aliases to the same id will be created
# so change done on one array will affect the other as they both share the same id
arr4 = arr2.view()
arr2[1] = 4
print(arr)
print(arr3)
print(arr4)
print(id(arr))
print(id(arr3))

ar1= array([
    [1, 2, 3, 4]
])

#Matrices

