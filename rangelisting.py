a = int(input("Alt sayıyı giriniz: "))
b = int(input("Üst sayıyı giriniz: "))
x = range(a, b)
def listing():
    a = min(x)-1
    for i in x:#x'teki sayılar kadar (11 tane) bunu yap
        a += 1
        print(a)
    print(a+1)

listing()

print('''
----2. Kısım----
''')


a = int(input("Alt sayıyı giriniz: "))
b = int(input("Üst sayıyı giriniz: "))
def listing(z, y):
    for i in range(z, y+1):#x'teki sayılar kadar (11 tane) bunu yap
        print(z) 
        z += 1

listing(a ,b)

#İkisi aaynı şey