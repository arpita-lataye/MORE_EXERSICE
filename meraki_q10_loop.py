marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i=0
while i<len(marks):
    j=0
    max=0
    while j<len(marks[i]):
        if marks[i][j]>max:
            max=marks[i][j]
        j=j+1
    print(max)
    i=i+1

# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter])
#     counter=counter+1