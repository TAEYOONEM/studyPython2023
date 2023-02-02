# 클래스 생성
class Person:
    # 1. 초기화 추가
    # def __init__(self) :    
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'RH+ A'
    #     self.state = '멈춤'
   
    def __init__(self,name,height,gender) : 
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self,option='걸어'):
        print(f'{self.name}')
        if option == '걸어' :
            self.state = '걷다'
        elif option == '뛰어' :
            self.state = '뛰다'
        elif option == '멈춰' :
            self.state = '멈춤'
        print(f'{self.state}')

# taeyoon = Person() # 인스턴스
# taeyoon.walk()
# print(f"{taeyoon.state}")

# 1. 초기화 후 객체생성
# hong = Person()
# hong.walk()

# 2. 파라미터를 받는 생성자 실행
ashely = Person('ashely','160','Female')
print(ashely.height)