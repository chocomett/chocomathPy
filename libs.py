from games import GanjilGenap, jkw

def wellcome_message():
    title = "Wellcome to ChocomathPy"
    style = "*" * (len(title) + 6)
    print(style)
    print(f"** {title} **")
    print(style)

def menu():
    user_input = int(input("1. GanjilGenap\n2. JKW\n3. Exit Program\n\nChoose your option.. "))
    
    if user_input == 1:
        GanjilGenap.start()
    elif user_input == 2:
        jkw.start()
    elif user_input == 3:
        print("Program dihentikan... ")
        exit()
    else:
        print("pilihan tidak tersedia")
        

if __name__ == "__main__":    
    wellcome_message()    
    menu()