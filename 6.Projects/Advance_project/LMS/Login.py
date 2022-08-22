'''
this is the login module of this software

'''

from Registration import Registration


class Login():
    def userLogin(self, username, password):
        print(username, password)
        self.username = username
        self.password = password
        r = Registration()
        datapassword = r.studentList
        print(datapassword)
        if self.username == 'admin' and self.password == 'admin':
            return True
        else:
            return False
