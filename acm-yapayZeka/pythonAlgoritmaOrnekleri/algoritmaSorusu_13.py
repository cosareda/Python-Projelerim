n = int(input("Kaç Fibonacci terimi yazdırmak istersiniz? "))

a = 0
b = 1

for i in range(n):
    print(a)
    temp = a
    a = b
    b = temp + b
