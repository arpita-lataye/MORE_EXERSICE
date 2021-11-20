# Cipher wheel with a function for finding an element in a list

# find_in_list function defined here but not called
def find_in_list(query, mainlist):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = 0
    for index in range_for_loop:
        element = mainlist[index]
        if element == query:
            index = index+1
    return index
# this should return the position of the "query" in the "mainlist"


chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']


def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_msg = plain_message
    for character in encrypted_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = new_char
            print(encrypt_message)
            
        else:
            encrypted_msg = character
            print(encrypted_msg) 


def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_msg = encrypt_message
    for character in decrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = new_char
            print(decrypted_msg)
        else:
            decrypted_msg = character
            print(decrypted_msg)  


# methods should return or print the new messages.
############################################### Code starts from here ##################################################
flag = True
while flag == True:
    choice = input("What do you want to do?\n 1. Encrypt a message 2. Decrypt a message \nEnter 'e' or 'd' respectively:")
    if choice=='e':
        plain_message = input("Enter message to encrypt??:")
        encrypt_message(plain_message)
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N):") 
        if play_again == 'Y':
            continue 
        elif play_again == 'N': 
            break

    elif choice=='d':
        encrypted_msg = input("Enter message to decrypt?:") 
        decrypt_message(encrypt_message)
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N):") 
        if play_again == 'Y':
            continue 
        elif play_again == 'N': 
            break

    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N):") 
        if play_again == 'Y':
            continue 
        elif play_again == 'N': 
            break


