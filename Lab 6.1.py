'''Sort the List According to the length of element and then sort in acending order Assume Data type integer'''


list=[]
n=int(input("enter the total number of element"))

for i in range(0,n):
    l=input("enter element in list")
    list.append(l)


list.sort(key=len)

for i in range(0,n):
     list[i] = int(list[i])

print("List after Sorting According to len:",list)

list.sort(reverse=False)
print("List after Sorting According ascending:",list)