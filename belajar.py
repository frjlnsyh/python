angka = int(input("Masukan angka :"))

"""
Tugas dari youtube membuat

1. --0++++5----8++++++11
2. ++++0----5+++++8-----11++++++

Menyelesaikannya dengan menggunakan as 
"""


tgs1 = (angka >= 0) and (angka <= 5 ) or (angka >= 8) and (angka <= 11 )
print(tgs1)


tgs2 = (angka <= 0) or (angka >= 5 ) and (angka <= 8) or (angka >= 11 )
print(tgs2)

"""

Ini pembelajaran tentang modulus, division, pangkat

-Modulus itu SISA hasil dari pembagian itu
-Division adalah kebalikan dari modulus
-Pangkat itu pangkat dari angka tersebut
"""

moduls = angka % 3
print('inputan akan di moduluskan % dengan 3 = ',moduls)

division = angka // 3
print('inputan akan di division // kan dengan 3 = ',division)

pangkat = angka ** 3
print('inputan akan di pangkatkan dengan 3 = ',pangkat)
