#Nama: Wildan Rangga A.P
#Kelas: XI TKJ 1
#Absen: 26
#Soal: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisaapel kurang dari 20 buah.

jumhlah_apel = 10
hari = 0

while jumhlah_apel >= 20:
    hari += 1
    penjualan = 0.10 * jumhlah_apel
    jumhlah_apel -= penjualan

print("Dibutuhkan", hari, " hari agar sisa apel kurang dari 20 buah.")