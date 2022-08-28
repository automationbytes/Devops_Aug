'''
Dict - use key and value pair
will not duplicates for key
3.7 - dict ordered = 3.6 unordered
{}
mutable
'''

mydic = {
    "fruit" : "Apple",
    "vegetable" : "Carrot",
    "cartoon" :"Tom Jerry",
    "fruit": ["Mango","PineApple"],
    "number":19
}
print(mydic)

#len
print(len(mydic))

#type
print(type(mydic))

#Access the value
#get
print(mydic.get("number"))

print(mydic["number"])

#All keys
print(mydic.keys())

#All values
print(mydic.values())

#items - both keys and value
print(mydic.items())

#loops

#iterating only keys
for k in mydic.keys():
    print(k)

#from keys how to get values
for v in mydic.keys():
    print(mydic[v])

#iterating value
for v in mydic.values():
    print(v)

for k,v in mydic.items():
    print(k,"--",v)