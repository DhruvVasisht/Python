def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def div(x,y):
    return(x/y)

def multiply(x,y):
    return(x*y)

def modulo(x,y):
    return(x%y)

print("Select An Operation")
print("1.Add")
print("2.Sub")
print("3.Div")
print("4.Multiply")
print("5.Modulo")

Operation=int(input("Enter The Choice"))
x=eval(input("Enter The Number 1 "))
y=eval(input("Enter The Number 2 "))

if Operation== 1:
    print(add(x,y))
    
elif Operation== 2:
    print(sub(x,y))

elif Operation== 3:
    print(div(x,y))

elif Operation==4:
    print(multiply(x,y))

else:
    print(modulo(x,y))
