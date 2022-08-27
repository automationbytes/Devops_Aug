#Adding
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage"]

#Append - end of the list
vegetables.append("Beans")
print(vegetables)

#Appending duplicate value
vegetables.append("Carrot")
print(vegetables)

#Insert - insert values in specified index
vegetables.insert(2,"Beetroot")
print(vegetables)
#vegetables.insert("ABC")
#Extend
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage"]
vegetables1 = vegetables.copy()

fruits = ["Apple", "Banana", "Mango", "Grapes", "Apple"]
vegetables.extend(fruits)
print(vegetables)

vegetables1.append(fruits)
print(vegetables1)
print(vegetables1[5][2])

a = [1,2,4,8]
b = a.copy()
print(b)

vegetables = ["Carrot","Cabbage","Potato","Tomato","Onion","Cabbage"]
vegetables[3] = "Beans"
print(vegetables)

#remove - remove the first value
vegetables.remove("Cabbage")
print(vegetables)

#Pop - removes the specified index
vegetables.pop(2)
print(vegetables)

#pop without index - removes the last value
print(len(vegetables))
vegetables.pop()
print(vegetables)
print(len(vegetables))

#delete the entire list

a = [1,2,4,8]
del a
#print(a)
#Clear - clear the values in list
a = [1,2,4,8]
a.clear()
print(a)

#count - used to return the number of occurences
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage","Onion"]
print(vegetables.count("carrot"))

#index - provides the index of particular value - remember it will provide first occurance

print(vegetables.index("Onion"))

#whenever we are trying to find values not there, it will throw an error
#print(vegetables.index("Apple"))

#sorting - both ascending,descending order
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage","Onion"]
vegetables.sort()#it will sort in ascending order
print(vegetables)

vegetables.sort(reverse=True)
print(vegetables)

#reverse
vegetables = ["Carrot","Potato","Tomato","Onion","Cabbage","Onion"]

vegetables.reverse()
print(vegetables)


a = [7,8,1,2,3]
a.sort(reverse=True)
print(a[0])
print(max(a))

#using loop finding max
num = [7,8,1,2,3]
max1 = num[0]
for i in num:
    if i > max1:
        max1 =i
print(max1)


#using loop finding min
num = [7,8,1,2,3]
min1 = num[0]
for i in num:
    if i < min1:
        min1 =i
print(min1)


str1 = ["apple","zebra","ball"]
print(min(str1))
