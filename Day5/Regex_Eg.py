import re

word = "Hello world 2022"
a = re.findall("[0-9]", word)
b = re.findall("\d", word) #number

print("".join(a))
print("".join(b))

a = re.findall("[A-z]", word)
b = re.findall("\D", word) #number
print("".join(a))
print("".join(b))


str = "     hi      world      "
a = re.sub("\s","", str)
print(a)

word = "Hello world 2022 its 03-09-2022"
w = re.sub('\D',"",word)
print(w)

regex = "[A-Z|a-z|0-9]+@[A-Za-z]+\.[A-Z|a-z]{3,}"
#print(re.fullmatch(regex,"email@gmail.com"))
if(re.fullmatch(regex,"emailgmail.com")):
    print("valid")
else:
    print("invalid")

print("\"Hello\"")