# 파일 만들기
file = open('sample.txt','w',encoding='utf-8') # 파일 쓰기로 만듦
file.write('안녕하세요')
file.close()

# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능