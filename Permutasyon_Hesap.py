import math
n=int(input("p(n, r) için n'yi giriniz : "))
r=int(input("p(n, r) için r'yi giriniz : "))
x = math.factorial(n)
y = math.factorial(n-r)
print("Sonuç : ", x/y)
