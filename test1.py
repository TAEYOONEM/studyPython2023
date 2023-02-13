class Point() :
    x = 0
    y = 0

n = int(input())    
arr = [_ for _ in range(n)]
 
for i in range(n) :
    arr[i] = Point()
    arr[i].x,arr[i].y = list(map(int,input().split()))

temp = Point()

for i in range(n-1) :
    for j in range(i+1,n) :
        if arr[i].x > arr[j].x :
            temp = arr[j]     
    arr[i] = temp

for i in range(n) :
    print(arr[i].x)


