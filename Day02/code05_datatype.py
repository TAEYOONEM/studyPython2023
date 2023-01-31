# 자료형
# None 값이 없는 값
None # 컴퓨터왈: 난몰라~~

print(None)
print(0==None)
print(''==None)

# 숫자형
val = 3
print(type(val))

val = 3.14
print(type(val))

val = 0b1010
print(type(val))

val = 12.123
print(type(val))

val = 4_520_000
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Life is short, You need Python'
print(val)
print(type(val))

val = 'Hello\nWorld!' # 탈출문자
print(val)
val = 'Hello\tWorld!'
print(val)
val = 'Hello\t\bWorld!'
print(val)

val = '''Life is short, 
You need Python'''
print(val)

val = 'Hello World!'
val = "Hello World!"

val = "Hi, I'm 'ty'"
print(val)
val = 'Hi, I\'m \'ty\''
print(val)

# 불린형 or 불
참 = True
거짓 = False
print(type(거짓))
print(1+1 == 2)
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(2)) # 1 이외 값은 True 라고 하지마세용