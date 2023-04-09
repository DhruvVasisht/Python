def odd_numbers(li):
    return [x for x in li if x%2 != 0]
li=[21,24,26,29,31,45]
print(odd_numbers(li))

b=[3*i for i in range(10)]
print(b)

a=[1,2,8,8]
b=[1,2,8,9]
if a>b:
    print("True")
else:
    print("False")