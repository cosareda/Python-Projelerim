number = int(input("Bir sayı giriniz: "))
ters_sayi=0
while number > 0:
    basamk = number % 10
    ters_sayi = ters_sayi * 10 + basamk
    number = number // 10

print("Sayı:", ters_sayi)