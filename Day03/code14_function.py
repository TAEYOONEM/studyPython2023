# # 함수

# global cnt
# cnt = 0

# 백준 25501
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for i in range(1,n+1) :
    val = input()
    cnt = 0
    print(isPalindrome(val),cnt)


# def add(x,y) :
#     return x + y

# def sub(x,y) :
#     return x - y

# def mul(x,y) :
#     return x * y

# def div(x,y) :
#     return x/y
