from functools import reduce
# to use reduce the above import is mandatory

# fibonacci sequence
# add 2nd last number with next number
# 0 1 1 2 3 5 8 13 21
import sys
# to use system level functions like getrecursionlimit etc

def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("invalid")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            if c < n:
                print(c)
# 1 2 3 4 5
# 0 1 2 3 4
# 0+1 1, 1+1 2, 2+1 3, 3+2 5
# 1st iteration - a+b c, a=b and b=c, then a=1 and b=1 c=2 in next iteration,
# 2nd iteration - a=b a is 1, b=c b is 2 and c= 3 in next iteration
fib(10)

#factorial
# 5! = 5*4*3*2*1 / 1*2*3*4*5
def fact(n):
    a=1
    for i in range(1, n+1):
        a = a * i
    print(a)
# 1*2 2, 2*3 6, 6*4 24, 24*5 120
fact(5)

# Recursion - a function calling itself
def greet():
    print("hello")
    greet()
# if I call the function greet it will execute infinite times as it is calling itself without any limit

# to know how many times it can call itself / To know what is recursion limit
print(sys.getrecursionlimit())

# To set max recursion
sys.setrecursionlimit(1000)

def fact2(n):
    if n == 0:
        return 1
    return n * fact2(n-1)

reslut = fact2(5)
print(reslut)

# Anonymous functions / Lambdas
# functions without def, used in the cases where we use funtion only once and it has only just few lines to execute
f = lambda a: a*a
result = f(5)
print(result)
# you can call any number of args but should have only one expression like a+b+c or a*b*c

# Filter, Map, Reduce - similar to the  terms defined in Big
# Filter - Filters data on certain condition
# Map - take the data and apply some operation on it
# Reduce - Find one value out of chunk

# Filter
# with function
def is_even(n):
     return n % 2 == 0

nums = [1,2, 3, 4, 5, 6]
evens = list(filter(is_even, nums))
print(evens)

# without defining a function or using Lambda
nums = [1,2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
# lambda n: n % 2 == 0 - this in itself is a function instead of using def and defining a function for such small functionality
# filter function needs two arguments - funtion and the input argument
# Filter function filter values based on true or false

# Map - take the data and apply some operation on it
# Reduce - Find one value out of check
# reduce - one time we add only two values or perform operations on any two values in a given list
# in reduce we will pass two parameters in the function other than the input parameters
nums = [1,2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n*2, evens))
sumi = reduce(lambda a, b: a+b, double)
print(evens)
print(double)
print(sumi)



# ___________________________________________________________________________
# Tech-M written test questions
# 1. Write a python function to count the occurrences of each character in a given string
# Example: "hello"
# Then
# Output: {'h':1, 'e':1, 'l':2, 'o':1}
def count_characters(ip_string):
    count_char = {}
    for i in ip_string:
        if i in count_char:
            count_char[i] += 1
        else:
            count_char[i] = 1
    return count_char

input_str = "hello"
r = count_characters(input_str)
print(r)

# 2. find missing element in the given range of numbers which have one missing value
# missing element = expected sum - actual sum
# The formula for expected sum of consecutive numbers from 1 to n is derived from arithmatic progression
# An arithmatic progression is a sequence of numbers, where difference between each consecutive number is constant
# Given the input is a range the difference is 1 between two consecutive numbers
# the formula for sum of an arithmatic progression is: Sum = (n/2) * [2a + (n-1)d]
# Where:
#
# Sum is the sum of the sequence.
# n is the number of terms in the sequence.
# a is the first term in the sequence.
# d is the common difference between terms.
def find_missing_element(arr):
    n = len(arr) + 1
    expected_sum = (n * (n+1)) // 2
    actual_sum = sum(arr)
    missing_element = expected_sum - actual_sum
    return missing_element

input_list = [1, 2, 3, 5]
m_e = find_missing_element(input_list)
print("missing element is :", m_e)

# DECORATORS - change the behaviour of an existing function at the
# if the function code is not available - either we are importing the function or we don't have the access
# or we don't want to change the existing function code

def div(a, b):
    print(a/b)
div(4,2)
div(2,4)
# When we want to have a condition where in any given 2 numbers the numerator should be less than the denominator
# and we don't want to change the existing function code then we use decorators
# decorators are functions that take function as an argument and apply another function's defined int hem to the called function

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner
# A decorator returns a function that function has the code or feature which is an extension we needed to the existing function

div = smart_div(div)
# like above we can declare a variable with the existing functions name and assign decorator to it to call it with the extended features

div(2,4)


