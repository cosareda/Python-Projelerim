print("Dört İşlem Menüsü:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
islem = int(input("Bir islem giriniz: "))
number1 = int(input("Birinci sayı giriniz: "))
number2 = int(input("İkinci sayı giriniz: "))
match islem:
    case 1:
        print("Toplam: ",number1 + number2)
    case 2:
        print("Çıkarma: ", number1 - number2)
    case 3:
        print("Çarpma: ",number1 * number2)
    case 4:
        print("Bölüm: ",number1 / number2)



