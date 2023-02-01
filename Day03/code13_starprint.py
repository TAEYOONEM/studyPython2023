for i in range(1,6) :
    print('*'*i)

for i in range(1,6) :
    print(' '*(6-i) + '*'*i)

for i in range(1,6) :
    for j in range(5,i-1,-1) :
        print(" ",end='')
    for k in range(1,i+1) :
        print("*",end="")
    print()