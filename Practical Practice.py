'''def distance(x1,x2,y1,y2):
    return((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1=int(input("Enter x1 Coordinates"))
x2=int(input("Enter x2 Coordinates"))
y1=int(input("Enter y1 Coordinates"))
y2=int(input("Enter y2 Coordinates"))
z=distance(x1,x2,y1,y2)
print(z)'''


'''def hypotenuse(x,y):
    return((x**2+y**2)**0.5)

x1=int(input("Enter x1 Coordinates"))
y1=int(input("Enter y1 Coordinates"))
z=hypotenuse(x1,y1)
print(z)'''

'''def even_odd(num):
    if(num%5==0 and num%10==0):
        return("Divisible By Both")
    elif(num%5==0):
        return("Divisble By 5")
    elif(num%10==0):
        return("Divisble By 10")
    
    else:
        return("Not divisble")
    
num=int(input("Enter"))
print(even_odd(num))'''

'''def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def div(x,y):
    return(x/y)

def multiply(x,y):
    return(x*y)

print("Select An Operation")
print("1.Add")
print("2.Sub")
print("3.Div")
print("4.Multiply")

Operation=int(input("Enter The Choice"))
x=eval(input("Enter The Number 1 "))
y=eval(input("Enter The Number 2 "))

if Operation== 1:
    print(add(x,y))
    
elif Operation== d2:
    print(sub(x,y))

elif Operation== 3:
    print(div(x,y))

else:
    print(multiply(x,y))'''

'''def reverse(num):
    rev=0
    while(num>0):
      dig=num%10
      rev=rev*10+dig
      num=num//10
    return(rev)
num=int(input("Enter Number"))
print(reverse(num))'''


'''def even(n):
    a=0
    for i in range(0,n,2):
        a=a+i
        print(i)
     
    return(a)

n=int(input("Enter"))
print(even(n))'''

'''def table(n):
    for i in range(1,n):
        for j in range(1,11):
            print(j*i)
        print("\n")
          
n=int(input("Enter The Number Of tables"))
print(table(n))'''

'''def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

n = int(input("Enter A Number"))
print(factorial(n))'''

'''def traverse(c):
    length=len(c)
    for i in range(0,length,2):
        print(c[i])
    
c=(input("Enter The String"))
print(traverse(c))'''

