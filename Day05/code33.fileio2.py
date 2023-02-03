# 파일 읽어오기
file = open('./Day05/sample03.txt','r',encoding='utf-8')
# while True :
#     text = file.readline()
#     if not text : break
#     print(text)
lines = file.readlines()
for i in lines:
    print(i)
file.close()