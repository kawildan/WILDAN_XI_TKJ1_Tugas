def tentukan_hasil(tugas, ujian):
    if tugas > 70 and ujian > 60:
        return "Lulus"
    else:
        return "Gagal"

nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))

hasil = tentukan_hasil(nilai_tugas, nilai_ujian)
print(f"Hasil: {hasil}")

