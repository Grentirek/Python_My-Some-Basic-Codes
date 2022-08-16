x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) #We can change the data type of a "variable" in python.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#GET THE 'TYPE' OF A VARIABLE:
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

print('''  A variable name cannot start with a number, 
           A variable name must start with a letter or the underscore character

Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

#Camel Case##
Each word, except the first, starts with a capital letter:

myVariableName = "John"

#Pascal Case#
Each word starts with a capital letter:

MyVariableName = "John"

#Snake Case#
Each word is separated by an underscore character:

my_variable_name = "John"''')

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

print('''''')

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print('''''')

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x+y+z)

'''x = 5
y = "John"
print(x + y) error'''

x = 5
y = "John"
print(x, y)

print('''
there is important
''')


x = "awesome" #this x is global

def myfunc():
  x = "fantastic"# but this, is local, then;
  print("Python is " + x)#this is will print "... fantastic"

myfunc()

print("Python is " + x)#and this print "... awesome"

print('''
But There is change things
''')
def myfunc():
  global x
  x = "fantastic"
  print("Python is", x)

myfunc()

print("Python is " + x)

print('''
Another example
''')

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
