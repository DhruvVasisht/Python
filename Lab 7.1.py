def even_odd( a , b):
    list1=[]
    list2=[]

    for i in range(a,b):
        if(i%2==0):
            list1.append(i)
        else:
            list2.append(i)

    print("Even list is",list1) 
    print("Odd list is",list2)          
        

a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
even_odd(a,b)