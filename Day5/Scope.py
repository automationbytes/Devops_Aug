def myfn():
    a = 10
    print(a)
myfn()

def myfn():
    global a
    a = 10
    return a

myfn()


def innerfun():
    print(a)


innerfun()


x = 10
def myfn():
    global x
    x = 20
myfn()
print(x)
