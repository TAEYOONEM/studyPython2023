# 자동차 클래스 
import os

class Car :
    number = '46저 2906'
    
    def get__number(self) :
        return self.__number

    def __init__(self,num='54fk 9538') -> None:
        print('__init__')
        self.__number = num

    # 클래스 외부에선 변경x, 멤버함수로는 내부를 조작o
    def set_number(self,number) :
        self.__number = number

    # 만들때 init 보다 먼저나옴
    # def __new__(cls) :
    #     print("__new__")
    #     return super().__new__(cls)

    # class 출력시 호출
    def __str__(self) -> str:
        return f'차번호는 {self.__number} 입니다.'

mycar = Car()
print(mycar)
print(f'제 차는 요, 테슬라이고, 번호가 {mycar.get__number()} 예요.')

mycar.__number = '18거 1517'
print(mycar)


yourcar = Car("a15")
print(yourcar)
yourcar.__number = '54라9999'
print(yourcar)
yourcar.set_number('1111')
print(yourcar)

