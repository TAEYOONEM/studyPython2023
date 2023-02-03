# 다중입력
# x,y= input("두 영단어를 입력하시오:").split(',')
# print(x)
# print(y)

# 완전 다중입력(개수가 몇개든지 상관없음)
inputs = list(map(str,input('단어를 입력하세요(개수상관X) > ').split()))
print(inputs) 
inputs = list(map(int,input('정수를 입력하세요(개수상관X) > ').split()))
print(inputs) 