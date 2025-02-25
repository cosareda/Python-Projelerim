
toplam = 0
for i in range(1,4):
    Not = int(input("not giriniz: "))
    toplam +=Not
    ortalama = toplam / i

if(ortalama >=50):
    print("Geçtiniz")
else:
    print("Kaldınız")