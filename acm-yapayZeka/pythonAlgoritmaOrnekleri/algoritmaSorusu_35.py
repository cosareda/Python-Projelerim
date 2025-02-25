kenar1 = float(input("Bir kenar uzunluğu giriniz: "))
kenar2 = float(input("Bir kenar uzunluğu giriniz: "))
kenar3 = float(input("Bir kenar uzunluğu giriniz: "))

if(kenar1==kenar2==kenar3):
    print("Üçgen eşkenar üçgendir.")
elif(kenar1 == kenar2 or kenar1==kenar3 or kenar2==kenar3):
    print("Üçgen ikizkenar üçgendir.")
elif not(kenar1 + kenar2 >kenar3 and kenar1 + kenar3> kenar2 and kenar2 + kenar3>kenar1):
    print("Üçgen oluşturmaz")
else:
    print("Üçken çeşitkenar üçgendir.")