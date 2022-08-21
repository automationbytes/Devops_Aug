a = 1
b = "ball"
print(type(a))
print(type(b))

#multiple line
multi = """A for Apple
B for Ball
C for Cat"""
print(multi)
print(type(multi))

a = "APPLE"

#length of the string
print(len(a))

#indexing
print(a[2])

#negative indexing
print(a[-2])

#Slicing
a = "APPLE FRUIT"
print(a[2:7]) #2 start value # 7 is my end value
print(a[2:])#it start from start and print til the end
print(a[:4])
print(a[:])

#negative slicing

print(a[-7:-1])
print(a[-9:])
print(a[:-6])
#print(a)
#print(a[-7:-2]) #2 start value # 7 is my end value

a = a[:-6]
print(a)

#Strip - trim the white spaces
a = "      APPLE    FRUIT    "
print(len(a))
print(a.strip()) #trim spaces on both sides
print(len(a.strip())) #trim spaces on both sides

print(a.lstrip()) #trim spaces on left side
print(a.rstrip())# trim spaces on right side

#lower case
a = "AppLe is lying in Graß.Banana is still on tree"
print(a.lower())
print(a.casefold())

#upper
print(a.upper())

#captialise
print(a.capitalize())

#title
print(a.title())

#swapcase
print(a.swapcase())

#isupper #islower
a = "appLe"
print(a.islower())

#replace
print(a.replace("p","o",1))

#replace
a = "Hello world"
print(a.replace("Hello","hi"))

#split
b= "Hello World Good Morning"
words = b.split(" ") #list
print(words)
print(words[0])
print(words[1])

#concat
a = "hello"
b = "world"
c= a+b
print(c)
d = 5
print(a+str(d))

#format
print(a+format(5))

#Startwith
a = "Apple is fruit"
print(a.startswith("Apple"))
print(a.endswith("fruit"))

#in - membership
print("is" in a)

#count
print(a.count("p"))
print(a.count("i",7)) #start value

print(a.count("i",2,7))
print(len(a))

print(a.index("f"))
print(a.index("p",2))
a = "Apple is fruit"

#print(a.index("x"))
#find
print(a.find("x"))
print(a.find("i"))#6
print(a.rfind("i"))#12

c = "abc"
print(c.isalpha()) # only alphabets

c = "456"
print(c.isdigit()) #only numbers

c = "abc123"
print(c.isalnum()) #alphabts n numbers

c = "Graß"
print(c.isascii()) #checks only ascii values
c = "45.87"

c = ["banana","mango","apple"]
print(type(c))
print(str(c))
x = " ".join(c)
print(x)

s = "Hello World.\tGood Night"
print(s)
print(s.expandtabs(9))

a = "Hello 2022 World"
print(a.removeprefix('2022'))

print(a.removesuffix("World"))
a = "Hello"
print(len(a.center(30)))

acctnum = "5678"
print(acctnum.zfill(16))


#replace special char with #
#hello%^&546$^&"
hello = "hello$%45"
for i in range(len(hello)):
    print(hello[i])
    if not hello[i].isalnum():

        print(hello.replace(hello[i],"#"))
