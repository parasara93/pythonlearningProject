x = 8
r = x % 2

if r == 0:
    print("even")
else:
    print("odd")
# elif is else if in python

# loops
# while
# we can use nested while like nested if
n = 1
while n <= 5:
    print("while check", n, end=" ") # end = " " is used to tell the print statement to print next print values in the same line
    n = n+1
    m = 1
    while m <= 4:
        print("this is another loop", m, end=" ")
        m = m+1
    print() # this prints each iteration in each line

# Write a code to print all the values from 1 to 100 skip the numbers which are divisible by 3 or 5
n = 1
while n <= 100:
    if n % 3 != 0 and n % 5 != 0:
        print(n)
    n = n+1

# Write a code to print a pattern, 4 rows with 5 hashes
j = 1
while j <= 4:
    print('#', end=" ") # end = " " is used to tell the print statement to print next print values in the same line
    j = j+1
    i = 1
    while i <= 4:
        print('#', end=" ")
        i = i+1
    print()
    # this prints each iteration in each line

# For loop
# works with sequence while works on conditions
x = 'Hemanth'
for i in x:
    print(i)
# here for i in x means for each value in x. if x is a list also same applies
# you can use the sequence directly instead of using it through a variable like x
# to print rang of values and also print values that are not divisible by 5
for i in range(1, 21):
    if i%5 != 0:
        print(i, end=" ")
print()
# break and continue
# av = 5
# x = int((input("how many candies:")))
# y = range(1, x+1)
# for i in y:
#     if i>av:
#         print("out of stock, more the available qauntity ", av)
#         break
#     print("candy", i)

# practicig printing patterns
for i in range(4, 0, -1):
    for j in range(i):
        print("#", end=" ")
    print()
for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()

for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()

x = ['a', 'b', 'c', 'd']
y = ['p', 'q', 'r']
for i in range(len(x)) :
    for j in range(i+1):
        print(x[j], end=" ")
    for n in range(i, len(y)):
        print(y[n], end=" ")
    print()

for m in range(len(y)):
        for n in range(m, len(y)):
            print(y[n], end=" ")
        print()
