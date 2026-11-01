def kdv_hesapla(fiyat):
    kdv_orani = 0.2

    return fiyat * kdv_orani

urun_fiyat = 160
kdv_tutari = kdv_hesapla(urun_fiyat)

yeni_vergi = kdv_tutari * 0.3

print("kdv: ", kdv_tutari)
print("yeni vergi: ", yeni_vergi)

def bizim_range(baslangic, bitis):
    geri_donecek_liste = []
    i = baslangic
    while i < bitis:
        geri_donecek_liste.append(i)
        i = i + 1
    
    return geri_donecek_liste

print(bizim_range(0, 5))