# Bab 7: Control Flow Python

# Percabangan if, elif, else
nilai = 85

if nilai >= 90:
    print("Predikat: A")
elif nilai >= 80:
    print("Predikat: B")
elif nilai >= 70:
    print("Predikat: C")
else:
    print("Perlu belajar lagi")

# Perulangan for
print("\nPerulangan For:")
for angka in range(1, 4):
    print("Angka:", angka)

# Perulangan while
print("\nPerulangan While:")
hitung = 1

while hitung <= 3:
    print("Hitung:", hitung)
    hitung += 1
