# 1. Hitung luas segitiga
# 2. Hitung luas persegi panjang
# 3. Menentukan angka ganjil dan genap
# 4. Quit
# Masukan Pilihan :
print("============= Restu Ramdani ============")
print("============= Latihan Sesi6 ============")
print("===== Program Kalkulator Sederhana =====")
print("----------------------------------------")
while (True) :
    print("Menu")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil dan genap")
    print("4. Quit")

    no_menu = input ("Masukan Pilihan : ")
    
    if no_menu == "1" :
        print ("Menu -- Hitung Luas Segitiga")
        alas = int(input("\nMasukan Alas Segitiga : "))
        tinggi = int(input("Masukan Tinggi Segitiga : "))

        rumus1 = 1/2 * alas * tinggi
        print("\nLuas Segitiga : ", rumus1)
        print("--------------------------")
    elif no_menu == "2" :
        print("Menu -- Hitung Luas Persegi Panjang")
        panjang = int(input("\nMasukan Panjang persegi : "))
        lebar = int(input("Masukan Lebar Persegi : "))

        rumus2 = panjang * lebar
        print("\nLuas Persegi Panjang : ", rumus2)
        print("--------------------------")
    elif no_menu == "3" :
        print("Menu -- Menentukan Angka Ganjil atau Genap")
        angka = int(input("\n Masukan Angka : "))
        
        if (angka % 2 == 0) : 
            print("\nAngka", angka, "Merupakan angka Genap")
        else : 
            print("\nAngka", angka, "Merupakan Angka Ganjil")

        print("-------------------------")

    else :
        menu = input ("\nTerima Kasih")
        print("-------------------------")
        break