import random

sayi = random.randint(0, 100) # 45

while True:
    kullanici_sayi = int(input("bir sayi tahmin et: "))

    if kullanici_sayi == sayi:
        print("evet bildiniz !")
        break
    elif kullanici_sayi < sayi:
        print("yukarı çık")
    else:
        print("aşağı in")