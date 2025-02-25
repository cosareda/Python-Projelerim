number1 = int(input("Birinci sayı giriniz: "))
number2 = int(input("İkinci sayı giriniz: "))
islem = input("Bir islem giriniz: ")
match islem:
    case '+':
        print("Toplam: ",number1 + number2)
    case '-':
        print("Çıkarma: ", number1 - number2)
    case '*':
        print("Çarpma: ",number1 * number2)
    case '/':
        print("Bölüm: ",number1 / number2)



