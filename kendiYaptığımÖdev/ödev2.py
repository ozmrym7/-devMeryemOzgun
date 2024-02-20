"""  1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

sayia=1
sayib=1
print(sayia)
print(sayib)
for i in range(20):
     sayic=sayia+sayib
     print(sayic)
     sayia=sayib
     sayib=sayic

"""
"""
  2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
sayi=int(input("lütfen mükkemmel olup olmadiğini öğrenmek istedğiniz sayiyi giriniz = "))
toplam=0 pozitif bölenleri hesap ettikten sonra toplayıp bu variableye ekleyeceğiz
for i in range(1,sayi):   1den başlayıp sayiya kadar olan sayiları tek tek ele al
       if  sayi%i==0:
          toplam+=i
if toplam==sayi:
        print("sayi mükkemmel sayidir")
elif toplam!=sayi:
        print("sayi mükkemel sayi değildir")
else:
        print("geçersiz değer girisi yaptiniz")

 """  
"""

  3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
sayi1=int(input("lütfen EBOB ve EKOK'unu öğrenmek istdeğiniz BİRİNCİ sayiyi giriniz= "))
sayi2=int(input("lütfen EBOB ve EKOK'unu öğrenmek istdeğiniz İKİNCİ sayiyi giriniz= "))
 EBOB hesaplama fonksiyonu
def ebob_bul(sayi1, sayi2):
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

 EKOK hesaplama fonksiyonu
def ekok_bul(sayi1, sayi2):
    return sayi1 * sayi2 // ebob_bul(sayi1, sayi2)

 EBOB ve EKOK'u hesapla
ebob = ebob_bul(sayi1, sayi2)
ekok = ekok_bul(sayi1, sayi2)

 Sonuçları ekrana yazdır
print("Girilen sayilarin EBOB'u:", ebob)
print("Girilen sayilarin EKOK'u:", ekok)
""" 
"""
 #  4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
sayi=int(input("lütfen asal olup olmadigini öğrenmek istediğiniz sayiyi giriniz= "))
for i in range(2,sayi):
     if sayi%i==0 :
         print("Girmiş olduğunuz sayı asal değildir.")
         break
else:
  print("sayi asaldır")
"""

 # 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.
def asal_carpanlari_bul(sayi):
    carpanlar = []  # Asal çarpanları saklamak için bir liste oluştur

    # 2'nin tüm bölenlerini bul
    while sayi % 2 == 0:
        carpanlar.append(2)
        sayi //= 2

    # 3'ten başlayarak tüm tek sayıların bölenlerini bul
    for i in range(3, int(sayi**0.5) + 1, 2):
        while sayi % i == 0:
            carpanlar.append(i)
            sayi //= i

    # Eğer sayı kendinden küçük kalan bir değerse, bu değer de asal çarpan olur
    if sayi > 2:
        carpanlar.append(sayi)

    return carpanlar

# Kullanıcıdan bir sayı al
sayi = int(input("Lütfen bir sayı girin: "))

# Asal çarpanları bul ve ekrana yazdır
print("Girdiğiniz sayının asal çarpanları:", asal_carpanlari_bul(sayi))