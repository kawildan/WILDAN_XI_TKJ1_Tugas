import os

def cek_file(file_path):
    if os.path.exists(file_path):
        print("File sudah ada.")
    else:
        print("File belum ada.")

# Ganti 'file_path' dengan path lengkap ke file yang ingin Anda periksa
file_path = '/path/ke/file/yang/akan/diperiksa.txt'
cek_file(file_path)
