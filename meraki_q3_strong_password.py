import re

def strong_password(password1):
    if len(password1)>6 and len(password1)<16:
        if re.findall("[^a-zA-Z0-9]", password1):
            print('password is created')
            return True
        else:
            print("password1 must contain at least one character,one digit or one special character")
            # password1=input('enter password:')
            # strong_password(password1)
    else:
        print("password1 length must be greater than 6")
        return False

password=input('enter password:')
a=strong_password(password)
print(a)

