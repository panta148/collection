def get_data():
    username=input("Enter UserName ->")
    password=input("Enter passwoord to login ->")
    if username=="1" and password=="1":
        print("\n\nCongratulation, Login Successfully..")
        return True
    else:
        print("\n\nEnter the correect username and the password")
        return False    

        



