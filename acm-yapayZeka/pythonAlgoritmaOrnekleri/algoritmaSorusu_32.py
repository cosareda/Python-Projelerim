sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))

if sayi1 == sayi2 == sayi3:
    print("Tüm sayılar eşit")
elif sayi1 == sayi2 or sayi1 == sayi3 or sayi2 == sayi3:
    print("İki sayı eşit")
else:
    print("Hiçbiri eşit değil")
