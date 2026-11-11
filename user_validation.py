user_name = input("Enter your username : ")
while True:
    if len(user_name) < 12:
        print("Username must be at least 12 characters long.")
        user_name = input("Enter your username : ")
    elif not user_name.isalnum():
        print("Username can only contain letters and numbers.")
        user_name = input("Enter your username : ")
    else:
        print("Username is valid.")
        break
print(f"Your username is: {user_name}")
