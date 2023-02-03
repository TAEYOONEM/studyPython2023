# 예외처리

def add(a,b) :
    return a+b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

try :    
    x, y = input().split()
    x =int(x)
    y = int(y)
except Exception as e :
    print(e)
    exit()
finally :
    print('Continue?') # 실행 뒤 종료됨 finally
 
# 원시적인 예외처리
# if y == 0 :
#     print('y에 0을 넣지 마시오.')
#     exit()

try:
    print(div(x,y))
# except ZeroDivisionError as e :
#     print('0으로 나누면 안되요!')
except Exception as e:
    print(e)
finally :
    print('Calculate Continue')

print(add(x,y))
print(mul(x,y))


