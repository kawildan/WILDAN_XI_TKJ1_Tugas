performa = int(input("Masukkan nilai performa karyawan (1 hingga 5): "))
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

bonus = (
    0.20 * gaji_tahunan if performa == 5 else
    0.10 * gaji_tahunan if performa == 4 else
    0.05 * gaji_tahunan if performa == 3 else
    0.02 * gaji_tahunan if performa == 2 else
    0
)

print(f"Bonus tahunan karyawan: {bonus:.2f}")
