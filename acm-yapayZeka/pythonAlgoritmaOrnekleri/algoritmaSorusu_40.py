alisverisTutar = float(input("Alışveriş tutarı giriniz: "))
uyelikDurum = input("Üyelik durumunuzu giriniz(üye/non-üye): ")
if uyelikDurum == "üye":
    indirim = 10  
else:
    indirim = 5

indirimliTutar = (alisverisTutar - (alisverisTutar*indirim / 100))

print(f"İndirim oranı:",indirim)
print(f"İndirimli tutar: ",indirimliTutar)
