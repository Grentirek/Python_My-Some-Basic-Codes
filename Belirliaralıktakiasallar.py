altsayi = int(input("Alt sayiyi girin: "))
ustsayi = int(input("Ust sayiyi girin: "))

asal = []
diger = []

for sayilar in range(altsayi, ustsayi+1):
    ol = True
    
    if sayilar == 1:
        ol = False
    
    for i in range(2, sayilar):
        if sayilar % i == 0:
            ol = False
            break
    
    if ol:
        asal.append(sayilar)
    
    else:
        diger.append(sayilar)
        
print("Asal sayilar: ", asal)
print("Asal olmayan sayilar: ", diger)