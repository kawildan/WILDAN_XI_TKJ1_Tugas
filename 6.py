def kategorikan_produk(penjualan):
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif penjualan >= 500:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"
    return kategori

penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

kategori = kategorikan_produk(penjualan)
print(f"Kategori produk: {kategori}")

