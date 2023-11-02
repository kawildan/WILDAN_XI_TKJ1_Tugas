#nama: WILDAN RANGGA ADI PUTRA
#Kelas: XI TKJ 1
#Absen: 27
#Soal:Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.

def tentukan_status_proyek(status_persiapan):
    if status_persiapan.lower() == "siap":
        return "Proyek diluncurkan."
    elif status_persiapan.lower() == "tunda":
        return "Proyek ditunda."
    else:
        return "Status persiapan proyek tidak valid."

status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

hasil = tentukan_status_proyek(status_persiapan)
print(hasil)
