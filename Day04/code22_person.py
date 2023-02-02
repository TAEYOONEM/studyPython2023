# 클래스 생성
class Person:
    def __init__(self) :
        self.색상 : 빨간색
        
        self.name = '익명'
        self.height = ''
        self.gender = ''
        self.blood_type = 'a'
        self.state = '멈춤'
    
    def walk(self,option='걸어'):
        if option == '걸어' :
            self.state = '걷다'
        elif option == '뛰어' :
            self.state = '뛰다'
        elif option == '멈춰' :
            self.state = '멈춤'

taeyoon = Person() # 인스턴스
taeyoon.walk('뛰어')
print(f"{taeyoon.state}")
