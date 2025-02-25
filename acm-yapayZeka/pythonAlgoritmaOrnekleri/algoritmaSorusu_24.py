en_kucukSayi = float('inf') #baaşlngıç değerini sonsuz değer vermek için
for i in range(1,5):
    sayi = int(input("Bir sayı giriniz: "))
    if(en_kucukSayi > sayi):
        en_kucukSayi = sayi
print("En küçük sayi: ",en_kucukSayi)