# FUNCTIONS
# Defining a function
def greet():
    print("hello")
    print("darling")

# defining with arguments or parameters
def add_sub(x, y):
    c = x+y
    d = x-y
    return c, d

# calling a function
greet()
# we can call this multiple times
# function does two things  execute a task or return values
# example for returning values
result = add_sub(5, 4)
# when 2 values are returned we need to have two variables to print these 2 values
result1, result2 = add_sub(5, 4)
print(result)
print(result1, result2)

# Function Arguments
def update(x):
    x = 8
    print(x)
update(10) #o/p is 8
a = 10
update(a) # passing 10 not a
print("a ",  a)
# call by value and call by reference
# cav - when you are calling a function with value
# car - when you change the value of x then it will change the value of a
# In python everything is an object and neither cav nor car apply
# in the above function the id of a is passed to x, so both the ids will be same before passing a value to x
# After passing the value the id/address is changed
# since int is immutable after passing a new value id is changed
# same goes for str, but when mutable objects like list are used and values are updated the id doesn't change
def up(lst):
    print(id(lst))
    lst[1] = 25
    print((id(lst)))
    print(lst)

a = [1, 5, 6]
print(id(a))
up(a)
print("a", a)

# below is the o/p
# 2200931841792
# 2200931841792
# 2200931841792
# [1, 25, 6]
# a [1, 25, 6]

# types of arguments
# Formal Arguments - defined arguments and Actual Arguments - arguments that we pass to a function
# Actual Arguments - Position, keyword, default and variable length
# position
def person(name, age):
    print(name)
    print(age)
# position based arguments
person('vegeta', 8)
# if you dont know the sequence
# we use keyword arguments
person(age=8, name='goku')
# default
# imagine if the function is defined  like this
# def person(name, age=8) -- here age default is 8 and if you don't pass any value to the argument then it takes 8
# in the above case if you send an argument that is not default it will take the argument that has been sent

# Variable length argument
# Consider a scenario where you need to write a function to add all the given number
# in this case we cant just pass 2 arguments, we use variable length arguments
def sum(*b):
    # above while passing arguments we can give a, *b as at least one value will definitely be passed
    # by *b, we define b as tuple
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(5, 6, 8, 9, 2)

# keyworded variable length arguments
# sending multiple arguments with keywords
def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)
        # since data here is no more a tuple it is a key value pair we have 2 values
        # also we cannot just give data we need to use function called items

person('navin', age=28, city='mumbai', mob=9848456)

# Global and Local variables
# we can create variables inside and outside of functions
# Global - variable outside the function, Local - variable used inside the function
# preference will be given to the local variable inside the function
# cannot access local variable outside the function
# but, we can access the global variable inside any function
# Even though we can use the global variable inside a function we cannot change the value of it without explictly defining it
# we define global variable inside a function like global variable_name

a = 10
def som():
    # global a
    # after the above we cannot define a local variable called a inside the function
    # when you want to change the global variable inside a function and also define a local variable
    # x = globals() returns all the global variables
    x = globals()['a'] # global variable with name a
    # to verify check the id of x and outside variable a both will be same as it points to the global variable a
    a = 9
    print("initial value of gv: ", x)
    print("in fun local variable", a)
    # to change the global variable without affecting the local use below
    globals()['a'] = 15


som()
print("outside changed / actual global variable", a)

# passing list as an input for a function
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [14, 52, 36, 96, 85, 47, 89]

e, o = count(lst)

print(e)
print(o)
print("even : {} and odd: {}".format(e, o))
# in the above print as we are having string arguments to convert set braces into the values of o,e we use string function format

# take 10 names from user and then count and display users name with more than 5 characters
def count_name(lst):
    lnames = 0
    for x in lst:
        if len(x) > 5:
            print(x)
            lnames += 1
    return lnames

l = int(input("enter number of users: "))
lit = []
for i in range(l):
    lit.append(input("enter user names:"))
print(lit)

name = count_name(lit)
print(name)

