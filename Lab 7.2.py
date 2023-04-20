def max(list,n):

    max=list[0]
    for i in range(0,n):
        if(list[0]<list[i]):
            max=list[i]

    print("Maximum element in the list is ",max)        

def min(list,n):

    min=list[0]
    for i in range(0,n):
        if(list[0]>list[i]):
            min=list[i]

    print("Minimum element in the list is ",min) 
        

n=int(input("Enter the total number of element "))

list=[]

for i in range(0,n):
    x=int(input("Enter the element "))
    list.append(x)

max(list,n)
min(list,n)