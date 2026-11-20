# Bab 10: Dictionary Python

# Membuat dictionary
siswa = {
    "nama": "Eva",
    "kelas": "XI RPL",
    "umur": 16,
    "sekolah": "SMK Negeri 2 Subang"
}

# Menampilkan dictionary
print("Data siswa:", siswa)

# Mengakses nilai berdasarkan key
print("Nama:", siswa["nama"])
print("Kelas:", siswa["kelas"])

# Menambahkan data baru
siswa["hobi"] = "Menggambar"

# Mengubah data
siswa["umur"] = 17

print("\nData siswa setelah diperbarui:")

# Perulangan dictionary
for key, value in siswa.items():
    print(key, ":", value)
