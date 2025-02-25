number = int(input("Bir sayı giriniz: "))

Kontrol = True
if(number < 0):
     Kontrol = False
for i in range(2,number):
    if(number % i==0):
            Kontrol = False
            print("Girilen sayı asal değildir.")
            break
    
if Kontrol:
    print("Girilen sayı asaldır")
else:
     print("Girilen sayı asal değildir ve negeatiftir.")