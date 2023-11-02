#Nama: Wildan Rangga A.P
#Kelas: XI TKJ 1
#Absen: 26
#Soal: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

nilai_investasi = 10000 
target_nilai_investasi = 20000
tingkat_pertumbuhan = 0.06
tahun = 0

while nilai_investasi < target_nilai_investasi:
    nilai_investasi += nilai_investasi * tingkat_pertumbuhan
    tahun += 1

print(f'Dibutuhkan {tahun} tahun agar nilai investasi melebihi ${target_nilai_investasi}.')