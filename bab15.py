# Bab 15: Abstraction Python

from abc import ABC, abstractmethod

# Class abstrak
class Kendaraan(ABC):

    @abstractmethod
    def bergerak(self):
        pass

# Class turunan
class Mobil(Kendaraan):

    def bergerak(self):
        print("Mobil bergerak menggunakan empat roda.")

# Membuat object
mobil1 = Mobil()

# Memanggil method
mobil1.bergerak()
