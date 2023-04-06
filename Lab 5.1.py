fahrenheit=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    fahrenheit.append(e)

celcius = []
for f in fahrenheit:
    c = format((f - 32) * 5 / 9,'20.2f')
    celcius.append(c)
 
print(celcius)