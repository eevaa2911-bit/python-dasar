# Bab 8: Function Python

# Fungsi sederhana
def sapa(nama):
    print("Halo,", nama)
    print("Selamat belajar Python!")

# Fungsi dengan dua parameter
def tambah(a, b):
    return a + b

# Memanggil fungsi
sapa("Eva")

hasil = tambah(10, 5)
print("Hasil penjumlahan:", hasil)

# Fungsi dengan nilai default
def perkenalan(nama, kelas="XI RPL"):
    print("Nama:", nama)
    print("Kelas:", kelas)

perkenalan("Eva")
