'''
Functions (Methods) - Block of code which only runs when they are called

Pass data - parameters

return - used to return some value from function

Adv
Reusability
Modularity

'''

def functionname(parameters):
    print("Sample function")

functionname("abc")
#fucntion witj return statement

def myname(name):
    return "Hello "+name

x = myname("Tom")
print(x)


studentname = myname("Tom")
marks = [10,5,80]

def sum (a,b):
    print(a, "A")
    print(b, "B")
    return a+b

print (sum (50,60) // 2)

def my_country(country = "India"):
    print("Country selected is ", country)

my_country("US")


def studentlist (*students):
    print("Student name",students[1])

studentlist("Tom","Jerry","Bheam","Scooby")


def stdlist(**students):
    print("Student name",students["std1"])

stdlist(std1 = "Tom", std2 = "Jack")


def stdname(sname):
    print(sname)
    for x in sname:
        if x == "Jerry":
            print("Hi Jerry")

names = ["Tom","Jack","Jerry"]
stdname(names)