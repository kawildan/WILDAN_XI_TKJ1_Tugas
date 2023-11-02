#Nama: Wildan Rangga A.P
#Kelas: XI TKJ 1
#Absen: 26
#Soal: Seorang petani ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jarak sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelajari itu dapat berlari lebih dari 10 kilometer.


jarak = 5 
minggu = 0  

while jarak <= 10:
    minggu += 1
    pertambahan_jarak = 0.10 * jarak
    jarak += pertambahan_jarak

print("Pelajari dapat berlari lebih dari 10 kilometer setelah", minggu, "minggu.")