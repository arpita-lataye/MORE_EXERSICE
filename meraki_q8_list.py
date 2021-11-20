list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16,5]
a=[]
i=0
while i<len(list2):
    if list1[i] not in a:
        a.append(list1[i])
    if list2[i] not in a:
        a.append(list2[i])
    i=i+1
print(a)

# a={}
# n=int(input('enter range:'))
# for i in range(n):
#     x=input('enter key:')
#     y=int(input('enter value:'))
#     # a[x]=y
#     a.update({x:y})
# print(a)

# a='w3school'
# b={}
# count=0
# for i in a:
#     if i not in b:
#         b[i]=1
#     else:
#         b[i]=b[i]+1
# print(b)