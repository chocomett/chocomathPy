from games import GanjilGenap

def wellcome_message():
    title = "Wellcome to ChocomathPy"
    style = "*" * (len(title) + 6)
    print(style)
    print(f"** {title} **")
    print(style)

def menu():
    user_input = int(input("1. GanjilGenap\n2. Rumus blabla\n3. Exit Program\n\nChoose your option.. "))
    
    if user_input == 1:
        GanjilGenap.start()
    elif user_input == 2:
        print("program belum ada")
    elif user_input == 3:
        print("Program dihentikan... ")
        exit()
    else:
        print("pilihan tidak tersedia")
        

if __name__ == "__main__":    
    wellcome_message()    
    menu()