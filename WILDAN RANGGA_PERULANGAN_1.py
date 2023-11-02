#Nama: Wildan Rangga A.P
#Kelas: XI TKJ 1
#Absen: 26
#Soal: Seorang petani memiliki 100 ekor ayam dipeternakannya. Setiap Bulan, jumhlah ayam bertambah 5% dari jumhlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumhlah ayam melebihi 200 ekor.

ayam = 100 
target = 200  
bulan = 0 

while ayam <= 200:
    bulan += 1
    pertambahan_ayam = 0.05 * ayam
    ayam += pertambahan_ayam

print("Jumhlah ayam melebihi 200 ekor pada bulan ke-", bulan)
