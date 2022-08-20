#9941625522

a = 654698491798449846649849564984684984949
print(a)
b = 6546989497979797546.17984498466498498949849494949494949494994
print(b)

#none
x = None
print(x)# none
print(type(x))#None type

#byte
y = b'hello'
print(y)
print(type(y))

#bytearray
z = bytearray(3)
print(z)
print(type(z))

print(memoryview(bytes(3)))

'''
Declare multiple values
# '''
# a = 10
# b = 5
# c = 2

a,b,c = 10,5,2
print(a)
print(b)
print(c)

z = y = x = 5
print(x)
print(y)
print(z)

'''
isinstance -return true/false based on variable we provided
syntax - isinstance(var,datatype)
'''

r = 5.5
print(isinstance(r,float))#True
print(isinstance(r,int))#False

'''
Typecasting - converting from one datatype to another
'''
a = '5a'
print(type(a))
b = int(a)
print(type(b))





