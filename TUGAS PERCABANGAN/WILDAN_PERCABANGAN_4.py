# Nama: [WILDAN RANGGA ADI PUTRA]
# Kelas: [XI-TKJ 1]
# Nomor Absen: [27]
# Soal: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium)
def hitung_diskon(total_belanja, status_anggota):
    if status_anggota == "premium":
        if total_belanja > 500000:
            diskon = total_belanja * 0.15
        else:
            diskon = total_belanja * 0.10
    else:  # Anggota biasa
        if total_belanja > 300000:
            diskon = total_belanja * 0.07
        else:
            diskon = 0

    return diskon

total_belanja = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (biasa atau premium): ").lower()

diskon = hitung_diskon(total_belanja, status_anggota)

if diskon > 0:
    print(f"Diskon yang diberikan: Rp {diskon:.2f}")
else:
    print("Tidak ada diskon yang diberikan.")

total_bayar = total_belanja - diskon
print(f"Total yang harus dibayar: Rp {total_bayar:.2f}")
