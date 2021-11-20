# i=int(input("enter the number: "))
# fac=1
# while i>0:
#     # if num%num:

#     fac=fac*i
#     i=i-1
# print(fac)




# here we have get output like Aa_Bb_Cc

n=input('enter string:')
i=0
while i<len(n):
    j=n.upper()
    print(j[i]+n[i],'_',end='')
    i=i+1