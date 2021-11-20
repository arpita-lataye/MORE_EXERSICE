student_num=int(input('enter number of students:'))
student_expenses=int(input('per students expenses:'))
total_expenses=student_num*student_expenses
if total_expenses<50000:
    print('under badget')
else:
    print('out of budget')