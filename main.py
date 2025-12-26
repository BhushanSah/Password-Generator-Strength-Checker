import random
import string
from pyfiglet import Figlet 
from colorama import init, Fore
init(autoreset=True)  

def show_menu( ):
    print(Fore.CYAN + "Choose your option")
    print(Fore.YELLOW + "1- Password Generator \n2- Strength Checker \n3- Exit")

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
        
    password = "".join(random.choices(character, k=password_length))
    return password
def Strength_checker(password):
    has_digit = has_alpha = has_special = False

    for c in password:
        if c.isdigit():
            has_digit = True
        elif c.isalpha():
            has_alpha = True
        elif c in string.punctuation:
            has_special = True

    length = len(password)

    if length >= 12 and has_digit and has_alpha and has_special:
        return "Very Strong"
    elif length >= 12 and has_digit and has_alpha:
        return "Strong"
    elif 8 < length < 12 and has_digit and has_alpha and has_special:
        return "Medium"
    elif 8 < length < 12 and has_digit and has_alpha:
        return "Weak"
    else:
        return "Too Weak"
def Generator():
    print("---What Do you want as your Password---")
    print("1-Only Alphabets\n2-Alphabets+numbers\n3-Alphabets+numbers+special Characters")
    while True:
        password_type = input("Enter 1/2/3: ")
        if password_type not in["1", "2", "3"]:
            print("Enter within Limit")
            continue
        break
    while True:
        try:
            password_length = input("Enter the Length of the Password (default 12): ")
            if not password_length:
                password_length = 12
            else:
                password_length = int(password_length)
            if password_length <= 0:
                print("Length must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for length.")
    password = Password_Generator(password_type, password_length)
    print(f"\nYour Password is: {Fore.CYAN}{password}{Fore.RESET}")
    strength = Strength_checker(password)
    if strength == "Very Strong":
        color = Fore.GREEN
    elif strength in ["Strong", "Medium"]:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print(f"Password Strength: {color}{strength}{Fore.RESET}")
    
def Manual_Strength_Check():
    password = input("Enter Your Password to Check Strength: ")
    strength = Strength_checker(password)
    if strength == "Very Strong":
        color = Fore.GREEN
    elif strength in ["Strong", "Medium"]:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print(f"Password Strength: {color}{strength}{Fore.RESET}")
    
def main():
    f = Figlet(font='slant')  
    print(Fore.MAGENTA + f.renderText('Welcome'))
    while True:
        show_menu()
        choice=input("Enter Your Choice: ")
        if choice.isdigit():
            if choice=="1":
                Generator()
            elif choice=="2":
                Manual_Strength_Check()
            elif choice=="3":
                print("--Good Bye--")
                break
        else:
            print("Invalid Choice")
        
if __name__ == "__main__":
    main()