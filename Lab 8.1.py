# a=45
# try:
#      b=a/0
#  except ZeroDivisionError:                          / zerodivision error
#      print("Error found")


# l = [1, 2, 3]
# try:
#     print("the index of 1 is", l[1])
#     print("the index of 1 is",l[2])
#     print("the index of 1 is",l[4])
# except IndexError:
#     print("index not found")


# try:
#     f=open("text.txt",'w')
#     f.write("This is a Text File")
#     f.close()
#     f=open("text.txt",'r')
#     print(f.read)
#     f.close()
# except EOFError:
#     print("error")


# a="hallo"
# b=45
# try:
#     c=a+b
#     print(c)
# except TypeError as e:
#     print(e)


def overflow(n):
    try:
        for i in range(1, 1000):
            n = n**i

    except OverflowError as e:
        print(e)


def zerodivision(a, b):
    try:
        c = a/b
        print(c)
    except ZeroDivisionError as e:
        print(e)    


def main():
    overflow(5.0)
    zerodivision(4, 0)

main()