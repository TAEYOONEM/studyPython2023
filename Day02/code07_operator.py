# 연산자
# 할당 연산 assignment
# 2 = 1(X)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2) # 소수 나누기
print(1024 // 2) # 정수 나누기
print(1024 % 2)
print(1 // 3)
print(1 % 3) # 나머지

# print(6/0) -> Zero Division

print(2 ** 10) # 승 제곱

# 문자열 연산
first = 'Hello'
second = 'World'
print(first + second)
print(first,second)
print(first +' '+second)

print(first * 4)

# 문자열 길이
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])

print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 스플릿 슬라이싱
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7
print(que)

que.append(5) 
print(que)
que.insert(3,99)
print(que)
que.remove(5)
print(que)

tup = (1, 2, 3, 4, 5)
# tup[1] = 9

# 문자열 == 문자 리스트
title = 'python'
print(title[0])
# title[0] = 'P' # 문자열에서는 값변경 X
print('P'+title[1:])

text = ['p','y','t','h','o','n']
text[0] = 'P'
print(text)




