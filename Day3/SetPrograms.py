#Remove duplicates from list
alist = [10,20,30,40,50,10,20,30]
print(alist)
remdup = set(alist)
print(remdup)
alist = list(remdup)
print(alist)

#to find duplicate
alist = [10,20,30,40,50,10,20,30]
newlist = []
for i in range(len(alist)):#10
    for j in range(i+1,len(alist)):#20
        if alist[i] != alist[j]:
            newlist.append(alist[i])
print(newlist)


#to remove duplicates
alist = [10,20,30,40,50,10,20,30,60]
newlist = []
for i in alist:
    if i not in newlist:
        newlist.append(i)
print(newlist)




