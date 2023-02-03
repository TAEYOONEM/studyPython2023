# 글자 인코딩
# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능

# 파일 만들기
# file = open('C:\\DEV\\Temp\\Bank\\sample01.txt','w',encoding='utf-8') # 파일 쓰기로 만듦
# file = open('C:/DEV/Temp/Bank/sample02.txt','w',encoding='utf-8') # \\ / 둘다 됨
# file = open('./Day05/sample03.txt','w',encoding='utf-8') 
# file = open('./Day05/../Day04/sample04.txt','w',encoding='utf-8') 
file = open('../sample05.txt','w',encoding='utf-8') 
file.write('안녕하세요\n')
file.write('첫번째 파일이다.\n')
file.write('절대 경로에 파일이 생성될겁니다.\n')
file.close()

# 파일/폴더 경로