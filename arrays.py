from array import *
# Difference between lists and arrays is arrays hold only one data type with in them
vals = array('i', [24 , 42, 51, 39, 25, 19])

# copy values from one array to another, vlas.typecode gives the data type of vals array elements
arry = array(vals.typecode, (a for a in vals))

for i in arry:
    print(i)
# creating an array with user prompt
# create empy array for user to give values
arr = array('i', [])
n = int(input('specify the length: '))
for i in range(n):
    x = int(input('enter the values: '))
    arr.append(x)
print(arr)

# searching for the index of the values user has given
n = int(input("enter the value: "))
for i in range(len(arr)):
    if n == arr[i]:
        print("the index value is: ", i)
        break
else:
    print("the num is not present in the array")

# with using method or function
print(arr.index(n))

# using for loop to create an array
for i in range(6, 10):
    vals.append(i)
print(vals)
# sorting the array in ascending order
temp = 0
for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        if vals[i] > vals [j]:
            temp = vals[i]
            vals[i] = vals[j]
            vals[j] = temp
print(vals)

# sorting the array in descending order
for i in range(len(vals)):
    for j in range( len(vals)):
        if vals[i] > vals [j]:
            temp = vals[i]
            vals[i] = vals[j]
            vals[j] = temp
print(vals)

# deleting elements in array without functions
z = int(input("enter the index of the value to delete"))
a = array('i', [])
for i in range(len(arr)):
    if i < z:
        a.append(arr[i])
    elif i > z:
        a.append(arr[i])
# deleting elements in array with functions
arr.pop(z)
print(a)
print(arr)

# changing the sequence of array first element to last element and vice versa
e = array('i', [12, 23, 34, 44, 54])
print(e)
f = array(e.typecode, (a for a in e))
counter = len(e)-1
for i in e:
    f[counter] = i
    counter -= 1
print(f)

