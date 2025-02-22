# --> comment line
# --> explain your source code, what ever we write in the
# comment line it will not exeecute


#this below code says welcome message

# welcome1="***************"
# welcome2="***************"
# welcome3="   Welcome     "
# welcome4="      To       "
# welcome5="Python Tutorial"
# welcome6="***************"
# welcome7="***************"


# print(welcome1)
# print(welcome2)
# print(welcome3)
# print(welcome4)
# print(welcome5)
# print(welcome6)
# print(welcome7)

# indentation -- spaces, which is used to read the code

my_num=[1,22,3]

def square(x):
    return x**2

square=list(map(square,my_num))
print(square)

# ways of writing variable

'''
1. snake case
eg: my_variable_datatype

2. myVariable === camle case

3. MyVariableDatatype ---> Pascal case

4. MYVARDATA --> upper case

5. myvardata --> lower case
'''

"""
data type:

2 types of data type:

1.primitive data type
integer --> int --> whole number
float --> float --> decimal number
string --> str --> character
(collection of characters are called as string)
boolean --> bool --> true or false

2.non primitive data type
list --> [list data type stored in square braces]
tuple--> (tuple data types are sored in round braces)
set --> {set data types are stored in flower braces}
dictionary --> {"key":"values"}
frozenset --> ({})
"""

name="pooja"

print(name)
print(type(name))

a=10
b=10.5
c="string"
d=True
e=["apple","mango"]
f=(12,34,65)
g={23,45,64,2,2,2,6,6,7,7,8,8}
dic={"name":"eshwari","name2":"shilpa","name3":"pooja","name4":"santhosh"}
Frozen=({1,2,3,4,5,6,6,6,6,5})
complex=3+1j

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (dic)
print (Frozen)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(dic))
print(type(Frozen))