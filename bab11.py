# Bab 11: Class dan Object Python

# Membuat class
class Siswa:

    # Constructor
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    # Method
    def perkenalan(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Saya sedang belajar Python.")

# Membuat object
siswa1 = Siswa("Eva", "XI RPL")
siswa2 = Siswa("Andi", "XI RPL")

# Memanggil method
print("Data Siswa 1:")
siswa1.perkenalan()

print("\nData Siswa 2:")
siswa2.perkenalan()
