# Bab 13: Inheritance Python

# Class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan.")

# Class anak
class Kucing(Hewan):
    def suara(self):
        print(self.nama, "mengeluarkan suara Meong!")

# Membuat object
kucing1 = Kucing("Milo")

# Memanggil method dari class induk
kucing1.makan()

# Memanggil method dari class anak
kucing1.suara()
