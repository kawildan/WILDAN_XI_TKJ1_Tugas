#nama: WILDAN RANGGA ADI PUTRA
#Kelas: XI TKJ 1
#Absen: 27
#Soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.


def cek_perlu_restart(pembaruan):
    if pembaruan.lower() == "ya":
        return "Sistem perlu di-restart."
    else:
        return "Sistem tidak perlu di-restart."

pembaruan = input("Apakah pembaruan perangkat lunak memerlukan restart? (ya/tidak): ")

hasil = cek_perlu_restart(pembaruan)
print(hasil)
