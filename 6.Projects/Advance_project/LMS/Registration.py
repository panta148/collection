'''
this model is work for the registration of new student
'''


class Registration:
    def __init__(self):
        self.studentList = {}

    def getdata(self):
        name = input("Enter  name")
        password = input("Enter  password")
        cpassword = input("Confirm password")
        if password != cpassword:
            print("Enter same password yopu have enter two different password")
        else:
            self.studentList[name] = password
            print("Congratulation you have successfully register.....")
        print(self.studentList)
