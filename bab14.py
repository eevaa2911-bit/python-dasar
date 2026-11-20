# Bab 14: Polymorphism Python

# Class Kucing
class Kucing:
    def suara(self):
        print("Kucing mengeluarkan suara Meong!")

# Class Anjing
class Anjing:
    def suara(self):
        print("Anjing mengeluarkan suara Guk guk!")

# Membuat object
hewan = [Kucing(), Anjing()]

# Memanggil method yang sama
for item in hewan:
    item.suara()
