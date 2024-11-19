print(10*"=")
print("Kalkulator")
print(10*"=")

valid_operators = {"","+", "-", "*", "/", "%", "//", "**"}

print("\n")

angka1 = input("Masukan Angka pertama : ")
operator = input("Masukkan operator aritmatika (+, -, *, /, %, //, **): ")
angka2 = input("Masukan Angka kedua : ")

if angka1 == "" or angka2 =="":
    print("\n")
    print("angka ada yang kosong")
elif operator not in valid_operators:
    print("\n")
    print("Aritmatika tidak ada operator dengan angka")
elif operator == "":
    print("\n")
    print("Operator Kosong")
else :
    try:
        angka1 = int(angka1)
        angka1 = int(angka2)
    except ValueError:
        print("\n")
        print("Bukan angka")
    else:
        if operator == '+':
            hasil = angka1 + angka2
            info = "Pertambahan"
        elif operator == '-':
            hasil = angka1 - angka2
            info = "Pengurangan"
        elif operator == '/':
            if angka2 == 0 :
                print("Angka 0 tidak bisa dibagi")
            else :
                angka1 = float(angka1)
                angka1 = float(angka2)

                hasil = angka1 / angka2
                info = "Pembagian"
        elif operator == '*':
            hasil = angka1 * angka2
            info = "Perkalian"
        elif operator == '**':
            hasil = angka1 ** angka2
            info = "Pangkat"
        elif operator == '//':
            hasil = angka1 // angka2
            info = "Division"
        elif operator == '%':
            hasil = angka1 % angka2
            info = "Modulus"

        print("\n")
        print(10*"=")
        print("Hasil dari ","\n",angka1,operator,angka2,"= ",hasil)
        print(10*"=")


print("\n")
