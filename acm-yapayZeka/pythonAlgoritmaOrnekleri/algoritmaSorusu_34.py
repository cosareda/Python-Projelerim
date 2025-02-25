boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))

BMI = kilo / (boy*boy)

if(BMI < 18.5):
    print("Zayıf")
elif 18.5<= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Fazla Kilolu")
else:
    print("Obez")