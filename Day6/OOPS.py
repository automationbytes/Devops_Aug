'''

Student
    #attributes
        name
        age
        rollnum

    #methds (behavior)
    learning
    writing

'''

class Student:
    name = "Jack"
    age = 9

    def readMethod(self):
        print(self.name, '\'s read method')

s = Student()
s.readMethod()
print(s.name)

class Student_WithConst:
    name = "Jack"
 #   age = 9
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def readMethod(self):
        print(self.name, '\'s read method')


    def __del__(self):
        print("Destructor")
s = Student_WithConst("Tom",5)
s.readMethod()

s1 = Student_WithConst("Jack",6)
s1.readMethod()
del s1
s1.name