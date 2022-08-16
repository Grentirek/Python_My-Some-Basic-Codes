# import time

# #----Örnek 1----
# sayilar = [1,2,3,4,5]
# for sayi in sayilar:
#    print("Yazı", sayi)




# time.sleep(1)
# print("\n---- 2. Kısım ----\n")
# time.sleep(2)

# #----Örnek 2----
# result = list(range(5))
# print(result)




# time.sleep(1)
# print("\n---- 2. Kısım ----\n")
# time.sleep(2)

#----Örnek 2----
# for i in range(5, 11, 2):
#    print("Yazı ", i)






############# ÖRNEK UYGULAMA #############

# sayilar = [1,3,5,7,9,12,19,21]
# #1- Sayilar listesindeki hangi sayılar 3' ün katıdır ?
# for i in sayilar:
#     if i % 3 == 0:
#         print(i, " sayısı üçün katıdır.")
#     else:
#         print(i, " sayısı üçün katı değildir.")

# print("\n---------------------------\n")

# # Sayilar listesinde sayıların toplamı kaçtır ?
# total = 0
# for i in sayilar:
#     total += i
#     print (total)


# print("\n---------------------------\n")

# #3- Sayilar listesindeki tek sayıların karesini alınız.
# for i in sayilar:
#     if i % 2 == 1:
#         print(i**2)
#     else:
#         print('"', i, '" sayısı tek sayı değildir.')


# print("\n###########################\n")

# sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
# #1- Şehirlerden hangileri en fazla 5 karakterlidir ?
# for sehir in sehirler:
#    if (len(sehir) <= 5):
#       print(sehir)


# print("\n###########################\n")

# urunler = [
#   {'name':'samsung S6', 'price': '3000' },
#   {'name':'samsung S7', 'price': '4000' },
#   {'name':'samsung S8', 'price': '5000' },
#   {'name':'samsung S9', 'price': '6000' },
#   {'name':'samsung S10', 'price': '7000' }
# ]
# #5- Ürünlerin fiyatları toplamı nedir ?
# toplam = 0
# for urun in urunler:
#    fiyat = int(urun['price'])
#    toplam += fiyat
# print('toplma ürün fiyatı: ', toplam)



# print("\n###########################\n")

# liste = [
#    {'uz': '33'},
#    {'uz': '7'}
# ]
# toplam = 0
# for topla in liste:
#    esit = int(topla['uz'])
#    toplam += esit
# print(toplam) #Liste içine "uz"un 33'e ve diğer "uz"un 7 ye eşit olduğunu giriyoruz. Toplamımız 0. 'topla'ya 'liste'deki her elemanı atıyoruz (ya da kopyalıyoruz).
              #"esit"imiz "topla"nın 'uz'una atanmış değeri integer (sayısal) olmasına eşitliyoruz (bütün "uz"ları hepsini tek tek). Sıfır olan 'toplam'ımıza esitin aldığı tüm farklı değerleri sıra sıra ekliyoruz.,
              #toplamı yazdırıyoruz.

liste = [
   {'uz' : '20'},
   {'uz' : '30'},
   {'su' : '30'}
]
toplam = 0
for sonuc in liste:
   esit = int(sonuc['uz'])
   toplam += esit
print(toplam) #Peki iki farklı "tanınmışı" yani 'uz' ve 'su'yu nasıl toplayabiliriz?