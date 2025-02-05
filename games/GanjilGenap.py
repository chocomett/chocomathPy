import libs

def user():
    user_input = int(input('tentukan bilangan '))
    return user_input

def start():
    while True:
        user_input = user()
        if user_input % 2 == 0:
            print(f"\n{user_input} adalah angka genap")
        else:
            print(f"\n{user_input} adalah angka ganjil")
           
        try_again = input("try again? [y / n]: ")
        if try_again == "n":
            libs.wellcome_message()   
            libs.menu()
            
            
    


if __name__ == "__main__":
    start()
            
        