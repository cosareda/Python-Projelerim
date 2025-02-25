number1 = int(input("Birinci sayi: "))
number2 = int(input("İkinci sayi: "))
number3 = int(input("Üçüncü sayi: "))

if((number1 >= number2) and (number1 >= number3)):
    print("En Büyük Sayı: ",number1)
elif((number2 >= number1) and (number2 >= number3)):
    print("En Büyük Sayı: ",number2)
else:
    print("En Büyük Sayı: ",number3)

