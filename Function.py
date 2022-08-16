import time

#----Örnek 1----
x = int(input("Toplama yapılacak ilk sayıyı giriniz: "))
y = int(input("Toplama yapılacak ikinci sayıyı giriniz: "))
def toplama(a,b):
    return a+b

print(toplama(x, y))




time.sleep(1)
print("\n---- 2. Kısım ----\n")
time.sleep(2)

#----Örnek 2----
ad = input("Adınız neydi? ")
Omerdog = int(input(ad + " efendi, doğum yılınızı girermisiniz? "))
def yashesap(dogumyili):
    return 2022 - dogumyili

ageÖmer = yashesap(Omerdog)
print("Yaşınız", ageÖmer)




time.sleep(1)
print("\n---- 3. Kısım ----\n")
time.sleep(2)

#----Örnek 3----
def ekv(dogumyili2, isim):
    yas = yashesap(dogumyili2)
    emeklilik = 65 - yas
    if emeklilik > 0:
        return "Sayın " + ad2 + ", emekliliğe " + str(emeklilik) + " yılınız kaldı."
    else:
        return "Sayın " + ad2 + ", zaten emekli oldunuz."

ad2 = input("Adınızı giriniz: ")
dogyili3 = int(input("Doğum yılınızı giriniz: "))
kalanyil = ekv(dogyili3, ad2)
print(kalanyil)





time.sleep(1)
print("\n---- 4. Kısım ----\n")
time.sleep(2)

#----Örnek 4----
girilenkelime = input("Hangi kelimeyi yazalım? ")
girilenadet = int(input("Kaç adet yazalım? "))
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir(girilenkelime  + "\n", girilenadet)