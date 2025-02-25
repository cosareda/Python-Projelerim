yas = int(input("Yaşınızı giriniz: "))

if(0 <= yas <= 5):
    print("Ücretsiz")
elif (6 <= yas <= 18):
    print("10TL")
elif (19 <= yas <= 64):
    print("20TL")
else:
    print("15TL")