sayac = 0
for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0):
        sayac +=1
        print(i)

print("Toplam Sayı: ", sayac)
