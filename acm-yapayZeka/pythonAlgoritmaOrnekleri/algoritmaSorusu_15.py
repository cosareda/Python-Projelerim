number = int(input("Bir sayı girin: "))
temp_number = number
basamak_sayisi = 0

while temp_number > 0:
    temp_number //= 10
    basamak_sayisi += 1

temp_number = number
armstrong_toplam = 0
while temp_number > 0:
    basamk = temp_number % 10
    armstrong_toplam += basamk ** basamak_sayisi
    temp_number //= 10

if armstrong_toplam == number:
    print(number, "bir armstrong sayısıdır.")
else:
    print(number ,"bir armstrong sayısı değildir.")
