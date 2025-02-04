def wellcome_message(message):
    style = "*" * (len(message) + 6)
    print(style)
    print(f"** {message} **")
    print(style)

def menu():
    user_input = int(input("1. GanjilGenap\n2. Rumus blabla\n\Choose your option.."))
    
    if user_input == 1:
        GanjilGenap.start()
    elif user_input == 2:
        print("program belum ada")
    else:
        print("pilihan tidak tersedia")
        

if __name__ == "__main__":    
    wellcome_message("Wellcome to ChocomathPy")    
    menu()