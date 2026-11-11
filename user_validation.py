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
user_password = input("Enter your password : ")
while True:
    if len(user_password) < 8:
        print("Password must be at least 8 characters long.")
        user_password = input("Enter your password : ")
    elif not any(char.isdigit() for char in user_password):
        print("Password must contain at least one number.")
        user_password = input("Enter your password : ")
    elif not any(char.isupper() for char in user_password):
        print("Password must contain at least one uppercase letter.")
        user_password = input("Enter your password : ")
    elif not any(char.islower() for char in user_password):
        print("Password must contain at least one lowercase letter.")
        user_password = input("Enter your password : ")
    else:
        print("Password is valid.")
        break
