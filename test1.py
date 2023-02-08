m,n = map(int,input().split())
arr = list()

for i in range(0,n+1) :
    arr.append(0)

for i in range(2,n+1) :
    if arr[i] != 0 :
        continue
    for j in range(2*i,n+1,i) :
        arr[j] = 1

for i in range(m,n+1) :
    if(arr[i] == 0) :
        print(i)

