while True:
    username = input("Enter your desired username: ")
    if len(username) >= 21:
        print(f"{username} is too long, please reduce it to less than 20 characters.")
        continue
    elif not username.find(" ") == -1:
        print("Your username can not contain spaces.")
    elif not username.isalpha():
        print("Your username can not contain numbers.")
    else:
        print(f"Welcome {username}!")
        break