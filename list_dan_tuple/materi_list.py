# ==========================================
# MATERI PYTHON: LIST
# List adalah urutan objek yang bersifat mutable (dapat diubah). 
# Kamu bisa menambah, menghapus, atau mengganti isinya setelah list tersebut dibuat
# ==========================================
# List adalah struktur data yang digunakan untuk menyimpan kumpulan data.
# Sifat List:
# 1. Mutable (Isinya bisa diubah)
# 2. Terurut (Ordered) - Index dimulai dari 0
# 3. Bisa menampung berbagai tipe data (campuran)
# 4. Ditandai dengan kurung siku []

print("--- 1. Membuat List ---")
# List kosong
list_kosong = []
# List dengan isi data sejenis
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
# List dengan tipe data campuran
campuran = ["Budi", 25, True, 3.14]

print(f"List Buah: {buah}")
print(f"List Campuran: {campuran}")
print()

# List Buah: ['Apel', 'Jeruk', 'Mangga', 'Pisang']
# List Campuran: ['Budi', 25, True, 3.14]

print("--- 2. Mengakses Elemen List ---")
# Menggunakan index (mulai dari 0)
print(f"Buah pertama (index 0): {buah[0]}")
print(f"Buah kedua (index 1): {buah[1]}")
# Index negatif (dari belakang)
print(f"Buah terakhir (index -1): {buah[-1]}")
print()

# Buah pertama (index 0): Apel
# Buah kedua (index 1): Jeruk
# Buah terakhir (index -1): Pisang

print("--- 3. Mengubah Isi List (Mutable) ---")
print(f"Sebelum diubah: {buah}")
buah[1] = "Anggur"  # Mengganti 'Jeruk' dengan 'Anggur'
print(f"Setelah index 1 diubah: {buah}")
print()

# Sebelum diubah: ['Apel', 'Jeruk', 'Mangga', 'Pisang']
# Setelah index 1 diubah: ['Apel', 'Anggur', 'Mangga', 'Pisang']

print("--- 4. Menambah Data ke List ---")
# append() -> Menambah di posisi paling belakang
buah.append("Melon")
print(f"Setelah append('Melon'): {buah}")

# insert() -> Menambah di posisi tertentu
buah.insert(0, "Strawberry") # Masukkan di index 0
print(f"Setelah insert(0, 'Strawberry'): {buah}")

# extend() -> Menggabungkan list lain
sayuran = ["Bayam", "Kangkung"]
buah.extend(sayuran)
print(f"Setelah extend sayuran: {buah}")
print()

# Setelah append('Melon'): ['Apel', 'Anggur', 'Mangga', 'Pisang', 'Melon']
# Setelah insert(0, 'Strawberry'): ['Strawberry', 'Apel', 'Anggur', 'Mangga', 'Pisang', 'Melon']
# Setelah extend sayuran: ['Strawberry', 'Apel', 'Anggur', 'Mangga', 'Pisang', 'Melon', 'Bayam', 'Kangkung']

print("--- 5. Menghapus Data dari List ---")
# remove() -> Menghapus berdasarkan nilai (hanya yg pertama ditemukan)
buah.remove("Pisang")
print(f"Setelah remove('Pisang'): {buah}")

# pop() -> Menghapus berdasarkan index (default: terakhir)
hapus_terakhir = buah.pop()
print(f"Data yg dihapus pop(): {hapus_terakhir}")
print(f"Isi list sekarang: {buah}")

# del -> Menghapus dengan index atau menghapus list itu sendiri
del buah[0]
print(f"Setelah del buah[0]: {buah}")
print()
# Setelah remove('Pisang'): ['Strawberry', 'Apel', 'Anggur', 'Mangga', 'Melon', 'Bayam', 'Kangkung']
# Data yg dihapus pop(): Kangkung
# Isi list sekarang: ['Strawberry', 'Apel', 'Anggur', 'Mangga', 'Melon', 'Bayam']
# Setelah del buah[0]: ['Apel', 'Anggur', 'Mangga', 'Melon', 'Bayam']

print("--- 6. Slicing List (Memotong) ---")
angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List angka: {angka}")
print(f"Ambil index 2 sampai 5 (angka[2:5]): {angka[2:5]}") # index 5 tidak termasuk
print(f"Ambil dari awal sampai index 4 (angka[:4]): {angka[:4]}")
print(f"Ambil dari index 6 sampai akhir (angka[6:]): {angka[6:]}")
print()

print("--- 7. Operasi Lainnya ---")
angka_acak = [5, 2, 9, 1, 5, 6]
print(f"List acak: {angka_acak}")

# len() -> Panjang list
print(f"Jumlah data: {len(angka_acak)}")

# count() -> Menghitung kemunculan data
print(f"Angka 5 muncul sebanyak: {angka_acak.count(5)} kali")

# sort() -> Mengurutkan
angka_acak.sort()
print(f"Setelah diurutkan (sort): {angka_acak}") 
# sort(reverse=True) -> Mengurutkan terbalik
angka_acak.sort(reverse=True)
print(f"Setelah diurutkan terbalik: {angka_acak}")
print()
