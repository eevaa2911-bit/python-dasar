# Bab 17: File Handling Python

# Menulis ke file
with open("catatan.txt", "w") as file:
    file.write("Halo, saya sedang belajar Python.\n")
    file.write("Ini adalah contoh File Handling.\n")

print("Data berhasil ditulis ke file.")

# Membaca isi file
with open("catatan.txt", "r") as file:
    isi = file.read()

print("\nIsi file:")
print(isi)
