class Google:
    def login(self):
        print("Google Login Method")

    def HomePage(self):
        print("Google Home Page")

class Youtube(Google):
    def HomePage(self):
        print("Youtube Home Page")

Y = Youtube()
Y.login()
Y.HomePage()

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def readMethod(self):
        print(self.name, '\'s read method of parent class')

class employe(student):
    def __init__(self,name,age,phone):
        super().__init__(name,age)
        self.phone = phone

    # def readMethod(self):
    #     super().readMethod()
emp = employe("Tom",20,"tom@gmail.com")
emp.readMethod()
