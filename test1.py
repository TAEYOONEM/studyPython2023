class SizeRank() :
    w,h = 0  
    rank = 

sizerank = SizeRank()
n = int(input())
for i in range(n) :
    sizerank.w[i],sizerank.h[i] = int(input().split(' '))
print(sizerank.w)

arr = list(map(int,input().split('\n')))
print(arr)