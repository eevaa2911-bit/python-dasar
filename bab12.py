# Bab 12: Encapsulation Python

class Rekening:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    # Method untuk menambah saldo
    def setor(self, jumlah):
        self.__saldo += jumlah
        print("Berhasil menambah saldo:", jumlah)

    # Method untuk melihat saldo
    def lihat_saldo(self):
        print("Nama pemilik:", self.nama)
        print("Saldo saat ini:", self.__saldo)


# Membuat object
rekening1 = Rekening("Eva", 100000)

# Melihat saldo awal
rekening1.lihat_saldo()

# Menambah saldo
rekening1.setor(50000)

# Melihat saldo setelah ditambah
rekening1.lihat_saldo()
