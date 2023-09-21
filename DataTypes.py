# lists
# are similar to arrays
# we can have different types of data like a list with numbers and characters
# we have lists within lists
# lists are mutable - i.e we can change values
# diff b/w append and insert is append will add at the end and insert will add in b/wave
# .remove will remove a value specified, .pop wil delete based on index
# last in first out so pop deletes last indexed element
# del list_name[2: ] deletes all elements from 2nd index
nums = [11, 56, 85, 78, 14]
print("min number is", min(nums), max(nums))

# tuples
# similar to lists but immutable once created cannot be changed
# iteration in tuples is faster than lists
# below is an example of tuple
tup = (15, 45, 230)
print("this is an example of tuple", tup)
print(tup.index(45))

# set
# Collection of unique elements
# set does not maintain sequence, as it uses hash to retrieve elements as soon as possible
# so indexing is not supported

s = {45, 12, 23, 56, 79}
s.add(85)
print(s)


# Dictionary
# contains key value pair
# we need to specify the key to fetch a value
data = {1: 'Naveen', 2: 'kiran', 4: 'Harsh'}
# when you don't have a key or associated value you can go with the below code to print something
# with the non-existent value
# we can delete the data in a dictionary with del command and passing the key with dic_name
# we can hav dictionary as a value in the dictionary itself, similarly list as value in a dic itself

print(data.get(3, 'not found'))

# to take 2 lists as a dictionary one list as key and other as value
keys = ['naveen', 'harsh', 'kiran']
values = ['python', 'java', 'c']
data = dict(zip(keys, values))
print(data)

# passing new data into dictionary
data['monika'] = 'cs'

print(data)

del data['harsh']

prog = {
    'js': 'atom',
    'cs': 'VS',
    'python': ['pycharm', 'sublime'],
    'java': {'jse': 'netbeans', 'jee': 'eclipse'}
    }

print(prog['python'])
print(prog['python'][1])
print(prog['java']['jee'])

# Data Types
# None, numeric, list, tuple, set, string, range, dictionary
# None - a variable not assigned with any values is None NULL in other languages is none in python
# Numeric - int, float, complex and bool
num = 2.5
print(type(num)) # type function prints the class
num = 6+9j # complex
# to change from one numeric type to another we have in-built functions to do the same
a = 4.5
b = int(a)
c = complex(b, a) # o/p from if we print c will be a+bj
x = a > b # x is now a bollen numeric data type
print(int(x)) # it is 1 for true and 0 for false when converted to int

# Sequence data types are list,set,tuple,set,string and range
# we don't have char in python string and char are both same in python
# range is a unique data type in python not available in other languages
range(10)
list(range(10))
print(list(range(2,11,2))) # creates a list from 2 to 11 with a difference of 2 between each element

# Dictionary or Mapping
# All the keys in a dictionary should be unique. this is a reason for using curl braces for dictionaries

# To get list of keys and values of a specific dic
# We can also use get method to get a value of certain key instead of using sqare braces
data.keys()
data.values()
