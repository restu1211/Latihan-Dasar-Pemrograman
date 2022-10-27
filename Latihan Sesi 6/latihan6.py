print("======== Restu Ramdani ========")
print("======== Latihan Sesi6 ========")
print("\n===== Program Grade Nilai =====")

while (True) :
    nama = input ("Masukan Nama anda   : ")
    nilai = input("Masukan Nilai Anda  : ")

    if(nilai.isnumeric() == True) :
        nilai_int = int(nilai)
        if nilai_int >= 90:
            grade = "A"
            predikat = 'Dengan Pujian'

        elif nilai_int >= 80:
            grade = "B"
            predikat = "Sangat Memuaskan"

        elif nilai_int >= 70:
            grade = "C"
            predikat = "Memuaskan"

        elif nilai_int >= 60:
            grade = "D"
            predikat = "Tidak Memuaskan"

        elif nilai_int >= 0:
            grade = "E"
            predikat = "Tidak Lulus"

        print ("\n=================================")
        print ("Nama                : ", nama)
        print ("Grade Anda          : ", grade)
        print ("Predikat Anda       : ", predikat)
    else:
        print("Input nilai anda salah!")

    apakah_lanjut = input ('\napakah ingin input nilai lain? Y untuk ya dan N untuk no : ')
    if (apakah_lanjut != "Y"):
        break

    print("\n=================================")

