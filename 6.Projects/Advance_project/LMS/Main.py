''''
this is the main class of this software 
'''
from Login import Login
from Registration import Registration


class SMS:
    def register(self):
        r = Registration()
        r.getdata()

    def login(self):
        l = Login()
        print(l.userLogin("admin", "admin"))


m = SMS()
m.register()
m.login()
