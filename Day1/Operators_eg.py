'''
Operators - to do operations on variables/values

Arithmetic operators - add/sub/mul
Assignment operator -
Comparison operator
Logical operator
Bitwise operator

Identity operator (is)
Membership operator (in)
'''

#Arthimetic Operators - Add/sub/etc

a = 10
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(int(a/b))
print(type(a / b))#2.5
print(a // b) #quotient called as floor division

print(a % b) # remainder called as modulas
print(a**b) #exponential

#Assignment - assign values to back to variable
a = 7
# a = a + 10 #17
# print(a)
a += 10 # a = a+ 10
print(a)

#comparison operator - compare two variables and return true/false
'''
== - equal to
!= - not equal to
> - Greater than
< - Less than
>= - Greater than or equal to
<= - Lesser than or equal to
'''

a= 10
b = 5
print(a >= b)
print(a<b)

#Logical Operator - combine 2 statements

'''
and
---
true and true = true
true and false = false
false and true = false
false and false = false

or
--
true or true =  true
true or false =  true
false or true = true
false or false = false

not -> reversing my result
---
false -> true
true -> false


'''

a = 10
b = 8
c = 5
print(c<b and a>c)

print((a<b))
print(not(a<b))

#Bitwise - convert into binary and compare

'''
& - and
| - or
~ - not

&
--
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0 
0 & 0 = 0

|
-
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
'''

a = 10 # 1010
b = 3  # 0011
#        1011

print(a & b)
print(a | b)

#identity opertor - is/ is not -> checks both belongs to same memory or not
x = ["1","2"] #64654496
y = ["1","2"] #49874946
z = y #49874946

print(x is y) #False
print(y is z) # True
print(x == y) # True - it checks only value - True

print(x is not y)
#Membership - test whether the values present inside or not
fruit = 'apple'
print('p' in fruit) # true

y = ["1","2","3","5"]
print("4" in y) # false

#not in
print("4" not in y)
