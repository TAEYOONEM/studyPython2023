# 콘솔출력 보충
# 이스케이프 캐릭터(탈출 문자)
print('1.Hello.\r\nWorld')
print('2.Hello.\nWorld') # 이걸 권장

print('3.Hello.\n\tWorld')
print('4.Hello.\n\t\bWorld')

print('5.Hello.\n\'World\'')
print('6.Hello. "World"')
print('7.Hello. \"World\"')

print('8.Hello. \ World') # 이렇게 역슬래쉬 프린트 파이썬만가능
print('9.Hello. \\ World')

print('10.Hello.\0')

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작
me = '저'
name = '태윤'
age = 20
print('%s는 %s입니다. %d대입니다.'%(me,name,age))

print(f'{254.112233:.2f}') # 최신식
print('%9.2f'%(254.112233)) # 전체 자리수. 소수점 자리수