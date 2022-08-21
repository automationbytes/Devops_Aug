i = 0
while i <= 10:
    print(i)
    i = i+1

##############################

#reverse a number
num = 1234 #4321
reversednumber = 0

while num > 0:
    remainder = num % 10 #4 = 4*10 = 40 #3 =43\
    reversednumber = reversednumber*10 + remainder
    num = num // 10

print(reversednumber)
print(type(reversednumber))

num = 1234
numstr = str(num) #typecasting
print(numstr)
print(type(numstr))
print(numstr[::-1])

a = "APPLE"
print(a[-1:-3:-1])

num = '1234'
print(num[::2]) #13
