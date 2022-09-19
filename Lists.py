thislist = list(("apple", True, 2.342, 60)) # note the double round-brackets
print(thislist)

'''
There are four collection data types in the Python programming language:

List        is a collection which is ordered and changeable. Allows duplicate members.
Tuple       is a collection which is ordered and unchangeable. Allows duplicate members.
Set         is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary  is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #refers to last item.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#This example returns the items from the beginning to, but NOT including, "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)

"""CHANGING ITEMS"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)#Change the second value by replacing it with two new values

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)#will remove last item

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist#will delete the entire list
#print(thislist) will make an error, because there is no such thing as 'thislist'

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#'thislist' still alive but is empty.


'''-------------------LOOPS IN LIST------------------'''

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])#Will print all items by referring to their index number.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

'''Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:'''

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]#A short hand for loop that will print all items in a list. Prints to down.

##Without listcomprehension:##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

##With listcomprehension:##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]#The new list is "x", which is contains words with the letter 'a' in "fruits".

print(newlist)#Prints side by side.



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]#If x is not "apple", appending to newlist.

print(newlist)

#ITERABLE: The "iterable" can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)]

print(newlist)#Side by side, in a list.
[print(x) for x in range(10)]#To down

newlist = [x for x in range(10) if x < 5+1]
print(newlist)

#Expression:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]#<-- the expression is 'x.upper()'.
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x == "banana" else "orange" for x in fruits]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]#If x not equal to "banana", for x in fruits, else(x is equal to banana) change it with "orange". It mean: "Return the item if it is not banana, if it is banana return orange".
print(newlist)


#SORTING##
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Custom
def myfunc(n):
  return abs(n - 50)#Sort the list based on how close the number is to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()#Case sensitive sorting
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#Solution
print(thislist)

##Reversing##
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

##COPYING##

print("""
Wrong way
""")
#THIS IS A MISTAKE#
thislist = ["apple", "banana", "cherry"]
mylist = thislist
mylist.append("a")#Because;
print(mylist, thislist)#This. 'thislist' have argument "a", too.

print("""
True way
""")
#THIS IS TRUE#
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist.append("a")
print(mylist, thislist)#Only mylist have "a" letter.

#Whith list() function:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist.append("a")
print(mylist, thislist)

##Join Lısts##
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)#X = indexes

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print('''
append()	  Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	  Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	  Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()	   Removes the item with the specified value
reverse()	  Reverses the order of the list
sort()	    Sorts the list
''')