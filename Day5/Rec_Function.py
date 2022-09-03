'''
Reccursive func - func to be called by itself

'''

num = 5 #5*4*3*2*1
fact = 1
for i in range(1, num+1):
    fact = fact * i #1*1 = 1 1*2 = 2 2*3 = 6 6*4=24 24*5 = 120
print(fact)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(num))