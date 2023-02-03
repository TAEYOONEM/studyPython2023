def calc(option, *args) :
    result = 0 
    if option == 'add' :
        for i in args :
            result += i
    
    elif option == 'mul' :
        result = args[0]
        for i in args[1:] : 
            result *= i
    
    elif option == 'sub' :
        result = args[0]
        for i in args[1:] :
            result -= i

    elif option == 'div' :
        try :
            result = args[0]
            for i in args[1:] :
                result /= i
        except : 
            return "error" 

    return result
  
# 여러값을 리턴할때는 튜플을 사용
def new_calc(x,y) :
    return (x*y, x/y, x+y, x-y)

# # 받을때는 튜플(소괄호) 생략가능
res1, res2,res3,res4 = new_calc(5,7)
# (res1, res2,res3,res4) = new_calc(5,7)
print(res1,res2,res3,res4)