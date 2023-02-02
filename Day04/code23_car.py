# 자동차 클래스 
class Car :
    number = '46저 2906'
    
    def get_number(self) :
        return self.number

    def __init__(self) -> None:
        print('__init__')

    def __new__(cls) :
        print("__new__")
        return super().__new__(cls)

    def __str__(self) -> str:
        return f'차번호는 {self.number} 입니다.'