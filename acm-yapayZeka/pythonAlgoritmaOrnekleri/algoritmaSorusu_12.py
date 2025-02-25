import random

number = random.randint(1, 100)
while(1):
    tahmin = int(input("Tahmininiz: "))
    if(tahmin > number):
        print("Daha küçük bir sayı giriniz: ")
    elif(number > tahmin):
        print("Daha büyük bir sayı giriniz: ")
    else:
        print("Tebrikler Doğru Tahmin")
        break
