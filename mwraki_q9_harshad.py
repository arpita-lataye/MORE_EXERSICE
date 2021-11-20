def harshad(num):
    a=num%10
    b=a//10
    c=a+b
    if num%c==0:
        print(True)
    else:
        print(False)
num=int(input('enter number:'))
harshad(num)


def harshad(num):
    i=a
    sum=0
    while i>0:
        sum=sum+(i%10)
        i=i//10
    if a%sum==0:
        print("it is a harshad number")
    else:
        print("it is not a harshad number")

a=int(input("enter the number:"))
harshad(a)