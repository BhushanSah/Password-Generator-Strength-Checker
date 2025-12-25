import random
import string 

def show_menu( ):
    print("        ---Welcome---")
    print("---Choose What You Want To Do---\n1- Password Generator\n2-Strength checker\n3-Exit")

def Password_Generator(password_type, password_length):
    if password_type=="1":
        character=string.ascii_letters
    elif password_type=="2":
        character=string.ascii_letters+string.digits
    elif password_type=="3":
        character=string.ascii_letters+string.digits+string.punctuation
    else:
        print("Default to Password_type 3")
        character=string.ascii_letters+string.digits+string.punctuation
        
    password="".join([random.choice(character) for i in range(password_length)])
    return password
def Strength_checker():
    pass 
def Generator():
    print("---What Do you want as your Password---")
    print("1-Only Alphabets\n2-Alphabets+numbers\n3-Alphabets+numbers+special Characters")
    while True:
        try:
            password_type = input("Enter 1/2/3: ")
            if password not in["1", "2", "3"]:
                print("Enter within Limit")
                continue
            break
        except ValueError:
            print("Please Enter a valid Number")
    while True:
        try:
            password_length = int(input("Enter the Length of the Password: "))
            if password_length <= 0:
                print("Length must be positive. Try again.")
                continue
            break  
        except ValueError:
            print("Please enter a valid number for length.")
    password = Password_Generator(password_type, password_length)
    print(f"\nYour Password is: {password}")
    
def main():
    while True:
        show_menu()
        choice=input("Enter Your Choice: ")
        if choice.isdigit():
            if choice=="1":
                Generator()
            elif choice=="2":
                Strength_checker()
                pass
            elif choice=="3":
                print("--Good Bye--")
                break
        else:
            print("Invalid Choice")
        
main()