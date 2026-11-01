# while

i = 0

while i <= 100:
    # print("i:", i, "asd")
    
    i = i + 1

# for
isim = "melih"

for i in isim:
    # print(i)
    pass

# liste oluşturma
alinacaklar_listesi = ["süt", "çikolata", "ekmek"]
print(type(alinacaklar_listesi)) # <class 'list'>
print(alinacaklar_listesi) # ['süt', 'çikolata', 'ekmek']
print(alinacaklar_listesi[0]) # süt
print(type(alinacaklar_listesi[0])) # <class 'str'>

karma_liste = ["süt", 2.4, 2]
print(karma_liste[1]) # 2.4
print(type(karma_liste[1])) # <class 'float'>

# for döngüsü liste döndürme
print("---------")
print("---------")

alinacaklar_listesi = ["süt", "çikolata", "ekmek"]
for alinacak in alinacaklar_listesi:
    print("alınacak öğe: ", alinacak)

range(0, 5) # [0, 1, 2, 3, 4]

for i in range(0, 11):
    print(i)

print("alinacaklar listesinin uzunlugu: ", len(alinacaklar_listesi))
print("istanbul kelimesinin uzunlugu: ", len("istanbul"))

print("ilk alınacak uzunlugu: ", len(alinacaklar_listesi[0]))

for i in range(0, 11, 2):
    print(i)

print("---------")
print("---------")


for i in range(0, 20):
    if i == 13:
        continue
        # break
    
    print("i: ", i)

# syntax

i = 13
print(i == 13) # True
print(i != 13) # False

# 0 ve 0 -> 0
# 0 ve 1 -> 0
# 1 ve 1 -> 1
# 0 veya 0 -> 0
# 0 veya 1 -> 1
# 1 veya 1 -> 1

x = True
y = False

print(x and y) # False
print(x or y) # True