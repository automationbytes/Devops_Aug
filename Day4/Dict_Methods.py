
mydic = {
    "fruit" : "Apple",
    "vegetable" : "Carrot",
    "cartoon" :"Tom Jerry",
    "number":19
}

#Adding
mydic["language"] = "Python"
print(mydic)

#Update
mydic.update({"number":10})
print(mydic)

#Update
mydic.update({"color":"Blue"})
print(mydic)


#setdefault - if yu hav a key- it wont update; else it will add

mydic.setdefault("color", "Red")
print(mydic)
#here red will nt be added, since we hav color key already
mydic.setdefault("car", "Tata")
print(mydic)
#car will be added since we dont hav car key


#remove

#pop
mydic.pop("number")
print(mydic)

#popitem
mydic.popitem() # it will remove the last value
print(mydic)

#clear - remove all values from dic
mydic.clear()
print(mydic)

#del
del mydic
#print(mydic)



mydic = {
    "fruit" : "Apple",
    "vegetable" : "Carrot",
    "cartoon" :"Tom Jerry",
    "number":19
}

newdic = mydic.copy()
print(newdic)

#Lab Exercises:
#1) check we hav specified key and update the value
#2) remove specified value
