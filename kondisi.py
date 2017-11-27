# kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau true
nilai = 9

# jika kondisi benar maka program akan mengeksekusi perintah dibawahnya
if (nilai>7):
    print ("selamat anda lulus")

# jika kondisi salah maka program tidak akan mengeksekusi perintah dibawahnya
if (nilai>10):
    print ("selamat anda lulus")

# kondisi if else adalah jika kondisi bernilai true maka akan dieksekusi bagian if jika salah akan dieksekusi bagian else
if (nilai > 10):
    print (nilai+" lebih besar dari 10")
else:
    print (nilai, " kurang dari 10")

# contoh penggunaan elif
hari = "senin"
if hari=="senin":
    print  "sekarang hari senin"
elif hari=="selasa":
    print "sekarang hari selasa"
elif hari=="rabu":
    print "sekarang hari rabu"
elif hari=="kamis":
    print "sekarang hari kamis"
elif hari=="jum'at":
    print "sekarang hari jum'at"
elif hari=="sabtu":
    print "sekarang hari sabtu"
elif hari=="minggu":
    print "sekarang hari minggu"
