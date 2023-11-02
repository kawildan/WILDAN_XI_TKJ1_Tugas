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
