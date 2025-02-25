yil = int(input("Bir yıl giriniz: "))

if ((yil % 4 == 0) and (yil % 100 != 0)):
    print(yil, ' yılı artık bir yıldır')
elif yil % 400 == 0:
    print(yil, ' yılı artık bir yıldır')
else:
    print(yil, ' yılı artık bir yıl değildir.')