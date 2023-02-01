arr = [1, 2, 3, 4, 5]
sum = 0 

for i in arr :
    # print(f'{i:.2f}')
    sum += i

# print('sum ='+str(sum))
print(f'sum ={sum}')


# 리스트를 편하게 만드는 방법
vals = [i for i in range(1,11)]
print(vals)

# continue / break
num = 0
for i in vals : 
    num += 1 
    if num % 2 == 0 :
        continue
        # break
    else : 
        print(num,'번 수는',i)



