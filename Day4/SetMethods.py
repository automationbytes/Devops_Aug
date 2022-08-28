vegetables = {"Carrot","Potato","Tomato","Onion","Cabbage","Carrot"}

#add (similar to append method in list, diff it will insert in random position)
vegetables.add("Beans")
print(vegetables)

#update - add a set/list/tuple with existing set (similar to extend)

fruits = ["Apple","Mango","Banana"]
vegetables.update(fruits)
print(vegetables)

#removing value from set

#pop
vegetables.pop()
print(vegetables)

#remove - remove specified value from set, remove will throws error when value is not thr
#vegetables.remove("Onion")
print(vegetables)

#Discard - remove specified value from set, discard will not get any error
vegetables.discard("vig")
print(vegetables)

#Clear -{} ->dict set()-empty set
vegetables.clear()
print(vegetables)

a = {}
print(type(a))
a = set()
print(type(a))

del a
#print(a)

#intersection
fruits = {"Apple","Mango","Orange"}
org = {"Apple","Microsoft","Google"}
print(fruits.intersection(org)) #existing set will not be impacted
print(fruits)

#intersection_update - values will be updated to existing set

fruits.intersection_update(org)
print(fruits)
print(org)

#Sym diff
fruits = {"Apple","Mango","Orange"}
org = {"Apple","Microsoft","Google"}
print(fruits.symmetric_difference(org))

#Sym diff update
fruits.symmetric_difference_update(org)
print(fruits)

#union - it will not update exisiting set (just combine)
fruits = {"Apple","Mango","Orange"}
org = {"Apple","Microsoft","Google"}
print(fruits.union(org))
print(fruits)

fruits.update(org)
print(fruits)


#diff
fruits = {"Apple","Mango","Orange"}
org = {"Apple","Microsoft","Google"}
print(fruits.difference(org))
print(fruits)

#diff update
fruits.difference_update(org)
print(fruits)

x = {1,5,7,8,9,4}
y = {4,5}
z = {100}

#x is super set of y
#y is subset of x
print(x.issubset(y))
print(x.issuperset(y))

#isdisjoint - return true if both doesnt hav any common value
print(x.isdisjoint(y))
print(x.isdisjoint(z))