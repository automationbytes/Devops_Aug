#lambda arg... : expression

sum = lambda a,b : a+b
print(sum(10,5))

def powerof(num,exp):
    return num **exp

def powerof(exp):
    return lambda num : num ** exp

a = powerof(3)
print(a(2))

