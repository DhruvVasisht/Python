lst=[]
for i in range(1,21):
    lst.append(i)
print("Orignal List",lst)

slc1=lst[5:15:2]
slc2=lst[::4] 
sum=avg=0
for a in slc1:
    sum=sum+a
print("Slice 1",slc1)
print("Sum Of Slice 1: ",sum)
print("Slice 2",slc2)
sum=avg=0
for a in slc2:
    sum=sum+a
print("Sum:",sum)
avg=sum/len(slc2)
print("Average Of Elements In Slice 2: ",avg)