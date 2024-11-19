# Miring
def triangle_miring(n):
    for i in range (1, n + 1):
        print('*' * i)
triangle_miring(5)

print("\n")

#miring terbalik
def triangle_miring_tebalik(n):
    for i in range (n, 0, -1):
        print('*' * i)
triangle_miring_tebalik(5)

print("\n")

#Setengah diamond
def setengah_diamond(n):
    for i in range (1,n + 1):
        print('*' * i)
    for j in range (n,0,-1):
        print('*' * j)
setengah_diamond(5)

print("\n")

#Setengah Diamon atas
def setengah_atas_diamon(n):
    for i in range (1,n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
setengah_atas_diamon(10)

print("\n")

#Setengah Diamon bawah
def setengah_atas_diamon(n):
    for i in range (n,0,-1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
setengah_atas_diamon(10)

print("\n")

# Full Diamon
def full_diamon(n):
    for i in range (1, n + 1):
        print(' ' * (n - i) + '*' * (2*i-1))
    for j in range (n, 0, -1):
        print(' ' * (n - j) + '*' * (2*j-1))
full_diamon(5)

print("\n")