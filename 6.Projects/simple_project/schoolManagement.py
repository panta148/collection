# this is the school management system  which is base upon the object oriented
class Schools:
    def __init__(self,t_name,name):
        self.t_name = t_name
        self.name=name


    def show_teacher_detail(self,list_of_teacher):
        for name in self.t_name:
            if name==list_of_teacher:
                print(f"NAME: {h.t_name} ")
            else:
                print("no such teacher is found in the list")



if __name__ == '__main__':
        h=Schools(['toyo','ram','shyam'],"Bal_niketan_school")
        h.show_teacher_detail("ram")