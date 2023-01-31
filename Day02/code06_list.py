# 복합형 
 
# 리스트 안씀
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
print(a1 + a2 + a3 + a4 + a5)
print(a1,a2,a3,a4,a5)

# 리스트 , 리스트 == 배열 in py

a = [1,2,3,4,5]
sum = 0
for i in a :
    sum += i
print(sum)
print(a)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello',13,'World!',True]
print(arr3)
print(type(arr3))
print('arr1의 2번 인덱스 값'+str(arr1[2]))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

# 딕셔너리 
spiderman = {'name' : 'Peter Parker', 
            'age' : 18,
            'weapon' : 'web shooter'}
print(spiderman['name'])
print(spiderman['age'])
print(spiderman['weapon'])
print(type(spiderman))

# 집합
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")
print(set1)
