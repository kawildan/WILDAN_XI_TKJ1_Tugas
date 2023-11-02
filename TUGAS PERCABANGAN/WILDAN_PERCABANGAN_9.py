#nama: WILDAN RANGGA ADI PUTRA
#Kelas: XI TKJ 1
#Absen: 27
#Soal: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

def tentukan_jenis_pinjaman(durasi):
    if durasi <= 7:
        return "Peminjaman Pendek"
    elif durasi > 7 and durasi <= 30:
        return "Peminjaman Menengah"
    else:
        return "Peminjaman Panjang"

durasi_peminjaman = int(input("Masukkan durasi peminjaman buku (dalam hari): "))

jenis_pinjaman = tentukan_jenis_pinjaman(durasi_peminjaman)
print(f"Jenis pinjaman: {jenis_pinjaman}")
