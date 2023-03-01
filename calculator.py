"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
response=''
while True:
    response=input(">>")
    if response=="q":
        print('thanks we are done')
        break
    
    try:
        operator,n1,n2=response.split(" ")
        n1,n2=int(n1),int(n2)
        
        if operator=="+":
            print(add(n1,n2))
        if operator=="-":
            print(subtract(n1,n2))
        if operator=="*":
            print(multiply(n1,n2))
        if operator=="/":
            print(f'{divide(n1,n2):1f}')
        if operator=="square":
            print(square(n1,n2))
        if operator=="cube":
            print(cube(n1,n2))
        if operator=="pow":
            print(power(n1,n2))
        if operator=="mod":
            print(mod(n1,n2))
    
    except:
        print('please try that again')


