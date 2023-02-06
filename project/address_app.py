# 주소록 프로그램
# 2023-02-06
# TaeYoon

# 2. 클래스 생성
class Contact:
    # 생성자 - 이름, 전번, 이멜, 주소
    def __init__(self,name,phone_num,email,addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr
    
    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이 름 : {self.__name}\n'
                   f'핸드폰: {self.__phone_num}\n'
                   f'이메일: {self.__email}\n' 
                   f'주 소 : {self.__addr}\n') 
        return str_res

# 3. 전체 실행
def run() :
    temp = Contact('엄준식','010-0000-0000','aaa@aaa.com',
                    '동탄시...')
    print(temp)

# 1. 메인 실행영역 
if __name__ == '__main__' :
    print('주소록 앱 시작합니다.')
    run()