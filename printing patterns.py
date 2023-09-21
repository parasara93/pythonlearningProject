
#printing desending sequence with numbers
st = ['A', 'B', 'C', 'D']

en = ['P', 'Q', 'R']
for i in range(4):
        for j in range(i+1):
            print st[j],
        for j in range(3 - i):


            print en[j + i],
        print

for i in range(4):
    for j in range(4-i):
            print j + i,

    print


for i in range(1, 4):
    print i,