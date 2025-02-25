notu = int(input("Sınav notunuzu giriniz (0-100): "))

if 90 <= notu <= 100:
    print("Harf notunuz: A")
elif 80 <= notu <= 89:
    print("Harf notunuz: B")
elif 70 <= notu <= 79:
    print("Harf notunuz: C")
elif 60 <= notu <= 69:
    print("Harf notunuz: D")
elif 0 <= notu <= 59:
    print("Harf notunuz: F")
else:
    print("Geçersiz not! Lütfen 0-100 arasında bir değer giriniz.")
