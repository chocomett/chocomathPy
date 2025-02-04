def user():
    user_input = int(input('tentukan bilangan '))
    return user_input

def start():
    while True:
       user_input = user()
       if user_input % 2 == 0:
           print(f"{user_input} adalah angka genap")
       else:
           print(f"{user_input} adalah angka ganjil")
    


if __name__ == "__main__":
    start()
            
        