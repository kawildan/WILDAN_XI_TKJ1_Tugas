def cek_perlu_restart(pembaruan):
    if pembaruan.lower() == "ya":
        return "Sistem perlu di-restart."
    else:
        return "Sistem tidak perlu di-restart."

pembaruan = input("Apakah pembaruan perangkat lunak memerlukan restart? (ya/tidak): ")

hasil = cek_perlu_restart(pembaruan)
print(hasil)
