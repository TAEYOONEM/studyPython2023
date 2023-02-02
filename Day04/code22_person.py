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

# 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력: 이름은 {self.name}, 성별은 {self.gender} 입니다.'

# taeyoon = Person() # 인스턴스
# taeyoon.walk()
# print(f"{taeyoon.state}")

# 1. 초기화 후 객체생성
hong = Person()
hong.walk()
print(hong)

# 2. 파라미터를 받는 생성자 실행
ashely = Person('ashely','160','Female')
print(ashely.height)
print(ashely)
