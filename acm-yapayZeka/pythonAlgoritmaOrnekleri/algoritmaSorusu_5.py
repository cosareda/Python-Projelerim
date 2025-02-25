number = int(input("Bir sayı giriniz: "))

while(1):
    if not(7 >= number >= 1):
        number = int(input("Lütfen 1 ya da 7 arasında bir sayı giriniz: "))
    else:
        break
    
match number:
    case 1:
        print("1: Pazartesi")
    case 2:
        print("2: Salı")
    case 3:
        print("3: Çarşamba")
    case 4:
        print("4: Perşembe")
    case 5:
        print("5: Cuma")
    case 6:
        print("6: Cumartesi")
    case 7:
        print("7: Pazar")
