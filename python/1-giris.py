# giriş

print("2" + "3")  # 23
print(2 + 3)  # 5

# print(type(2)) # integer -> int
# print(type(2.5)) # float -> float
# print(type("2")) # string -> str
# print(type("2.5")) # string -> str

print(round(3.14159, 2))  # 3.14

# ekrandan veri alma
# yaricap = int(input("dairenin yarıçapını giriniz: "))
# pi = 3.14
# alan = pi * yaricap * yaricap
# print(alan)

# değişkenler
yaricap = input("dairenin yarıçapını giriniz: ")
print(type(yaricap))  # <class 'str'>

yaricap = int(input("dairenin yarıçapını giriniz: "))
print(type(yaricap))  # <class 'int'>

yaricap = float(input("dairenin yarıçapını giriniz: "))
print(type(yaricap))  # <class 'float'>
