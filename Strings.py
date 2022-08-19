for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


print("""
KISIM2
""")

b = "Hello, World!"
ae = txt[0]
print(b[2:5])#5. index dahil değil.
print(b[:5])
print(ae)
print(b[5:])
print(b[-1])
print(b[-5:-2])#-2. index dahil değil(-1'den başlar)

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("l", "J"))

a = "Hello, World!"
print(a.split(", W")) # returns ['Hello', 'orld!']

'''age = 36
txt = "My name is John, I am " + age
print(txt)''' #Is this an error.

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
'\'+'ooo'	Octal value	
'\'+'xhh'	Hex value
"""

txt = "Saydi3nma"
print(txt.encode())
print(txt.endswith("a"))
print(txt.find("i"))
print(txt.index("i"))
print(txt.isalpha())
print(txt.isspace())
print(txt.join("AAA"))
print(txt.ljust(44))#?
print(txt.translate("3312"))#?
print(txt.zfill(14))
print(isinstance(txt, int))
