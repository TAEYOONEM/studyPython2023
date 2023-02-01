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
        result = args[0]
        for i in args[1:] :
            result /= i
    
    return result

print(calc('sub',3,5))   