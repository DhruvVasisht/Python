num=eval(input("Enter The Number"))
if(num%5==0 and num%10==0):
    print("It Is Divisble By Both")
elif(num%5==0):
    print("It Is Divisible By 5")
elif(num%10==0):
    print("It Is Divisible By 10")

else:
    print("It Is Not Divisible By 5 And 10")
