# Nama: [WILDAN RANGGA ADI PUTRA]
# Kelas: [XI-TKJ 1]
# Nomor Absen: [27]
# Soal: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan.

# Input total belanjaan pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Mengecek aturan diskon
if total_belanjaan > 500000:
    diskon = 0.1  # Diskon 10%
elif total_belanjaan >= 300000:
    diskon = 0.05  # Diskon 5%

# Menghitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Menghitung total pembayaran setelah diskon
total_setelah_diskon = total_belanjaan - jumlah_diskon

# Menampilkan hasil
print(f"Total belanjaan: Rp {total_belanjaan:,.2f}")
print(f"Diskon: {diskon * 100}%")
print(f"Jumlah diskon: Rp {jumlah_diskon:,.2f}")
print(f"Total pembayaran setelah diskon: Rp {total_setelah_diskon:,.2f}")
