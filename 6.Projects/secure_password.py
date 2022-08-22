# welcome to the secure password generator 
# SECURE=(('a','b'),('b','c'),('c','d'))
SECURE=[['a','@'],['b','^'],['c','('],['d','='],['e','*']]
def securepassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
        # print(password)cls
    return password
    


if __name__ == '__main__':
    password=input("Enter the password\n->")
    password=password.lower()
    print(password)
    new_password=securepassword(password)
    print(f'\n\n\nYour secure password is \n {new_password}')

    