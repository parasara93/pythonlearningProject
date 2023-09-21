from array import *
lst1 = ['A', 'B', 'C', 'D']
lst2 = [1,2,3,4]
lst3 = ['P', 'Q', 'R']
print lst1,lst2
for j in range(len(lst1)):
    for i in range(len(lst1)-j):
        print lst1[i],
    print

for j in range(len(lst2)):
    for i in range(len(lst2)-j):
        print lst2[i+j],
    print
for j in range(len(lst1)):
    for i in range(j+1):
        print lst1[i],
    for i in range(len(lst3)-j):
        print lst3[i+j],
    print

AR = array('i', [24 , 42, 51, 39, 25, 19])
temp = 0
for i in range(len(AR)):
    for j in range(len(AR)):
        if AR[i] < AR[j]:
            temp = AR[i]
            AR[i] = AR[j]
            AR[j] = temp
print AR