from math import *
# x = int(input("enter the number"))
# for i in range(2,x):
#     if x % i == 0 :
#         print ("the number is not a prime number")
#         break
# else:
#     print ("the number is prime number")


for x in range(2, 11):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        print("prime", x)
print()

num = 7
print(sqrt(num))
print(num//2)
for x in range(2, int(sqrt(num))):
    if num % x == 0:
        print("not prime")
        break
else:
    print("prime", num)
print()
