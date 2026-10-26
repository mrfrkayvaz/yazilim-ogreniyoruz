# koşullar - conditions
age = int(input("yaşınız: "))
print(age)

if age >= 18:
    if age < 50:
        print("ehliyet alabilirsiniz")
    else:
        print("yasınız cok fazla")
else:
    print("ehliyet alamazsın")

# elif
# yas -> 120
if age > 100 or age < 0:
    print("gecersiz")
elif age > 50:
    print("yasiniz cok fazla")
elif age >= 18:
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alamazsın")

# str
# int
# float

print(type(age > 100))  # boolean -> 0,1 -> bool

# age -> 120
yas_100den_buyuk_mu = age > 100  # True

# age -> 60
yas_100den_buyuk_mu = age > 100  # False

# if
if True:
    print("burası her zaman calisir")
else:
    print("burası hicbir zaman calismaz")

if False:
    print("burası hicbir zaman calismaz")
else:
    print("burası her zaman calisir")
