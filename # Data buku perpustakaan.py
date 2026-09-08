# Data buku perpustakaan
daftar_buku = (
    "Dasar dasar pemograman",
    "Pengantar teknologi informasi",
    "Bahasa inggris",
    "pendidkan pancasila",
    "Sistem Operasi"
)

pinjaman = []

print("=== PERPUSTAKAAN FT ===")
print("Daftar buku:")

for buku in daftar_buku:
    print("-", buku)

while True:
    print("\nMenu:")
    print("1. Pinjam buku")
    print("2. Hapus buku pinjaman")
    print("3. Selesai")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama_buku = input("Masukkan judul buku yang ingin dipinjam: ")

        if nama_buku in daftar_buku:
            pinjaman.append(nama_buku)
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak tersedia.")

    elif pilihan == "2":
        nama_buku = input("Masukkan judul buku yang ingin dihapus: ")

        if nama_buku in pinjaman:
            pinjaman.remove(nama_buku)
            print("Buku berhasil dihapus dari daftar pinjaman.")
        else:
            print("Buku tersebut tidak ada dalam daftar pinjaman.")

    elif pilihan == "3":
        print("\nProgram selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

print("\n=== DAFTAR BUKU YANG DIPINJAM ===")

if len(pinjaman) == 0:
    print("Belum ada buku yang dipinjam.")
else:
    for buku in pinjaman:
        print("-", buku)
