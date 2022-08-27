'''
#List

Insertion Ordered
Mutable
Does allow duplicates
Homo and hetro data types (Same and diff data)
[] - for storing list
Elements will be accessed based on index

'''

fruits = ["Apple", "Banana", "Mango", "Grapes", "Apple"]
print(fruits)

#Length of list
print(len(fruits))

#indexing (Starts from 0)
print(fruits[2])

#Updating
fruits[4] = "PineApple"
print(fruits)

#Negative Indexing (from the last value)
print(fruits[-4])

#Slicing - Cutting down the list into small list
#['Apple', 'Banana', 'Mango', 'Grapes', 'PineApple']

print(fruits[1:4]) #upper bound value will nt be printed

#starts from the mentioned index and print till the end
print(fruits[2:])

#start from begining and stop at mentioned index
print(fruits[:3])
fruits = ["Apple", "Banana", "Mango", "Grapes", "Apple","Banana", "Mango", "Grapes"]

print(fruits[slice(1,6,2)]) #start, stop, step

print(fruits[1:6:2])

#Negative Slicing
print(fruits[-5:-2],"Negative Slicing")

print(fruits[:-1])#starts from the first value and print till -1
print(fruits[-5:])

#Loops
#length of string is 5
            #   0         1       2        3        4
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage"]
for i in range(0,len(vegetables),1):
    print(vegetables[i])
print('-------------------------------------')

for j in range(len(vegetables)): #start 0 and step 1
    print(vegetables[j])
print('-------------------------------------')

#for each
for v in vegetables:
  #  print(v)
    if v == 'Onion':
        print("Available")
        break

mixedlist = [1,"Hi",3.14,"World"]
print(mixedlist)

for m in mixedlist:
    print(m)

print(type(mixedlist))

a = [1,2,4,8]
b = list((1,4,7,9)) # constructor - remember to use double round brackets
print(a)
print(type(a))
print(b)
print(type(b))

#While loop

mixedlist = [1,"Hi",3.14,"World"]
i = 0
while i < len(mixedlist):
    print(mixedlist[i])
    i = i+1 #i++

#Shortend for - List comprehension
mixedlist = [3,"Hello",3.14,"World"]
[print(i) for i in mixedlist]

fruits = ["Apple", "Banana", "Mango", "Grapes", "Apple"]
newfruits = [i for i in fruits if i!= 'Apple']
print(newfruits)


forwitelse = [x if x!="Apple" else "PineApple" for x in fruits]
print(forwitelse)
