'''
Tuple - ordered
and Unchangable
Duplicates are allowed
()- without brackets also possible
multiple datatypes are possible

'''
#with brackets
words = ("Apple","Ball","Cat","Dog")
print(type(words))
print(words)


#without brackets
words = "Apple","Ball","Cat","Dog"
print(type(words))
print(words)

#constructor
words = tuple(("Apple","Ball","Cat","Dog"))
print(type(words))
print(words)

#indexing
print(words[0])
#negative indexing
print(words[-2])

#slicing
print(words[1:3])

#add/update/remove - convert to list and do action and convert back to tuple

#add a values to tuple
words = ("Apple","Ball","Cat","Dog")
#elephant
newlist = list(words)
newlist.append("Elephant")
words = tuple(newlist)
print(words)
print(type(words))

#Remove items
remlist = list(words)
remlist.remove("Dog")
words =tuple(remlist)
print(words)

#looping
for w in words:
    print(w)

for w in range(len(words)):
    print(words[w])

[print(i) for i in words] #again convered to list

#count - how many times values are repeated

words = ("Apple","Ball","Cat","Dog","Apple")
print(words.count("Apple"))

#index - returns the position the value
print(words.index("Apple"))

newords = list(words)
newords.sort()
print(newords)
words = tuple(newords)
print(words)


'''

List - Mutable                  Tuple  - immutable
More memory                     Less memory
slower                          Faster
insert,delete, update(write)    read only memory access it
[]                              {}

'''
