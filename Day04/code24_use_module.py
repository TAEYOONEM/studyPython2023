# 모듈 사용
import math as m # 클래스로 안된 모듈
import code22_person as p # 우리가 만든 클래스
from code23_car import Car as c

print(m.pi)
print(m.sin(m.pi/2))
print(m.pow(2,10))
print(2**10)

# 우리가 만든 모듈 사용
me = p.Person('홍길순',155,'female')
print(me)

avante = c()
print(avante)