toplam = 0
N = int(input("Bir sayı giriniz: "))
for i in range(1,(N+1)):
    toplam += (i ** 3)
print( "Küplerin Toplamı: ",toplam)