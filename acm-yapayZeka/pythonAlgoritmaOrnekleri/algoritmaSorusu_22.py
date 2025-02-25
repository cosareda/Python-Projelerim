boy = float(input("Boyunuzu girin: "))
kilo = float(input("Kilonuzu girin: "))

vki = kilo / (boy ** 2)

if vki > 25:
    print("Fazla kilolu")
else:
    print("Fazla kilolu değil")
