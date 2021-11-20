def encrypt():
    message = input("Enter the message you want to encrypt:")
    ascii_message = [ord(char)+3 for char in message]
    encrypt_message = [ chr(char) for char in ascii_message]  
    print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt:")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag==True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!:")
    if choice == 'e':
        # plain_message = input("Enter message to encrypt??:")
        encrypt()
        play_again = input("Do you want to try agian (Y/N):")
        if play_again == 'Y':
            continue
        exist=input('Do you want to exist(Y/N):')
        if exist=='N':
            continue
        else:
            break
    elif choice == 'd':  
        # decrypt_message = input("Enter the message you want to decrypt")
        decrypt() 
        play_again = input("Do you want to try agian (Y/N):")
        if play_again == 'Y':
            continue
        exist=input('Do you want to exist(Y/N):')
        if exist=='N':
            continue
        else:
            break
    else:
        exist=input('Do you want to exist(Y/N):')
        if exist=='N':
            continue
        else:
            break