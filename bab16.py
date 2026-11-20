# Bab 16: Exception Handling Python

print("Belajar Exception Handling")

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
    print("Hasil pembagian:", hasil)

except ValueError:
    print("Error: Masukkan angka yang valid!")

except ZeroDivisionError:
    print("Error: Angka tidak boleh nol!")

finally:
    print("Program selesai.")
