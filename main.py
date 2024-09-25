import random
import string
from GUI import *
def generate_password(length:int,choice:str)->str:
    #print("MAIN MENU\n1.Only characters\n2.Only numbers\n3.Characters+Numbers\n4.Characters+Numbers+Special characters\n")
    character_list = ''
    if choice == '1.Only characters':
       character_list += string.ascii_letters
    elif choice == '2.Only numbers':
       character_list += string.digits
    elif choice == '3.Characters+Numbers':
        character_list += string.ascii_letters + string.digits
    elif choice == '4.Characters+Numbers+Special characters':
        character_list += string.ascii_letters + string.digits + string.punctuation
    else:
        print("Enter valid choice")

    password = ''.join(random.choice(character_list) for _ in range(length))
    return password


if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
