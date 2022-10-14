# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga beserta nama barang

while(True):
    nama_barang = input ('masukan nama barang : ')
    harga_barang = int(input('masukan harga barang : '))
    persen_harga = input ('masukan persen harga : ')
    harga_keuntungan = int(harga_barang) * int(persen_harga) /100
    harga_jual = int(harga_barang)+harga_keuntungan
    print (nama_barang, "dijual dengan harga : ", harga_jual)

    apakah_lanjut = input ('apakah ingin input barang lain? Y untuk ya dan N untuk no : ')
    if(apakah_lanjut != "Y"):
        break