'''
Inheritance - derive the properties from one class to another class

class parentclass:
    #body
class childclass1(parentclass):
    #body
class childclass2(parentclass):
    #body


'''


class Vehicle:
    def todrive(self):
        print("This is method of Vehicle")

class AutoMobile:
    def todrive(self):
        print("This is method of AutoMobile")

class Car(AutoMobile,Vehicle):
    def brand(self):
        print("Brand name is Ford")

c = Car()
c.todrive()