from sys import getsizeof

'''Tuple: Is a collection which is ordered and unchangeable. Allows duplicate members.'''

from ctypes import sizeof


thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
print(getsizeof(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print(getsizeof(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple1 = ("abc", 34, True, 40, 3.214)
tuple2 = (1, 5, 7, 9, 3.22)
tuple3 = (True, False, False)
print(tuple1)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)