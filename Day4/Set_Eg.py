'''

Set is very similar to list
It is mutable (Yu can add/delete values)
Set will not maintain insertion order
Will not allow duplicates values
Will not allow indexing (unindexed)
{} - Used for storing values
Homo and Hetrogeneous data

'''

vegetables = {"Carrot","Potato","Tomato","Onion","Cabbage","Carrot"}
print(vegetables)
print(type(vegetables))

#len - after removing duplicates, we will get the output
print(len(vegetables))

#set constructor
newvegetables = set(("Carrot","Potato","Tomato","Onion","Cabbage","Carrot"))

#hetro
mixedset = {1,5.5,"abcd"}
print(mixedset)

#for loop
for n in newvegetables:
    print(n)

