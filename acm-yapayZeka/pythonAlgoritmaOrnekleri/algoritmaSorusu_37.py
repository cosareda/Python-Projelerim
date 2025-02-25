havaDurumu = input("Hava Durumunu Giriniz: ")
sicaklik = float(input("Sıcaklığı giriniz: "))

if(havaDurumu == "Güneşli" and sicaklik >=25):
    print("Piknik Yapabilirsiniz.")
elif(havaDurumu == "Yağmurlu"):
    print("Şemsiye Almayı Unutmayın.")
elif(havaDurumu == "Karlı" and sicaklik < 0):
    print("Kayak Yapmaya Gidebilirsiniz.")
else:
    print("Evde Kalabilirsiniz.")