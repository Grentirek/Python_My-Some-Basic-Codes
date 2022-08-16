s = int(input("Sayı_"))
while True:
    if s%2 == 0:
        s /= 2
        print(s)
    elif s == 1:
         print(s)
         break
    else:
        s = (3*s)+1
        print(s)

    
