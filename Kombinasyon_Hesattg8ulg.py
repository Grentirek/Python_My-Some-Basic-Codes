import math
n=int(input("C(n, r) için n'yi giriniz : "))
r=int(input("C(n, r) için r'yi giriniz : "))
x = math.factorial(n)
y = math.factorial(n-r)
z = x/y
k = math.factorial(r)

print("Sonuç : ", z/k)
