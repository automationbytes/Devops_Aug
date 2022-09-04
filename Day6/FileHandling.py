'''

r - read
a - append
w - write
x - create

'''

f = open("myfile1.txt","a")
#f.write("\nTuesday")
li = ['Wednesday\n',"Thursday\n"]
f.writelines(li)

f.close()


f = open("myfile1.txt","r")
# for x in f:
#    print(x)
print(f.readline())

print(f.readline())
f.close()

import os
if os.path.exists("myfile1.txt"):
    os.remove("myfile1.txt")
else:
    print("File not found")
