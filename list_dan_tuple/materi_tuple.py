# ==========================================
# MATERI PYTHON: TUPLE
# Tuple adalah urutan objek yang bersifat immutable (tidak dapat diubah). 
# Kamu tidak bisa menambah, menghapus, atau mengganti isinya setelah tuple tersebut dibuat
# ==========================================
# Tuple mirip dengan List, tapi ada perbedaan SANGAT PENTING.
# Sifat Tuple:
# 1. Immutable (Isinya TIDAK BISA DIUBAH setelah dibuat)
# 2. Terurut (Ordered) - Index dimulai dari 0
# 3. Ditandai dengan kurung biasa ()
# 4. Lebih hemat memori & lebih cepat aksesnya dibanding List

print("--- 1. Membuat Tuple ---")
# Tuple kosong
tuple_kosong = ()
# Tuple dengan satu elemen (CIRI KHAS: WAJIB pakai koma)
tuple_satu = (10,)
# Jika tanpa koma, dianggap integer biasa
bukan_tuple = (10) 

# Tuple biasa
koordinat = (10, 20)
warna = ("Merah", "Hijau", "Biru")
# Tuple campuran
data_user = ("Raihan", 17, True)

print(f"Tipe tuple_satu: {type(tuple_satu)}")
print(f"Tipe bukan_tuple: {type(bukan_tuple)}")
print(f"Tuple Warna: {warna}")
print()

print("--- 2. Mengakses Elemen Tuple ---")
# Mirip list, pakai index kurung siku []
print(f"Warna pertama: {warna[0]}")
print(f"Warna terakhir: {warna[-1]}")
print()

print("--- 3. Sifat Immutable (Tidak Bisa Diubah) ---")
# Coba ubah isi tuple (Akan Error jika dijalankan baris di bawah)
try:
    warna[0] = "Kuning"  
    # # <-- Ini akan menyebabkan TypeError
    print("Mencoba mengubah warna[0] menjadi 'Kuning'...")
except TypeError as e:
    print(f"ERROR: {e}")
    print("Penjelasan: Item di tuple tidak bisa diassignment ulang (immutable).")
print()
# --- 3. Sifat Immutable (Tidak Bisa Diubah) ---
# ERROR: 'tuple' object does not support item assignment
# Penjelasan: Item di tuple tidak bisa diassignment ulang (immutable).

print("--- 4. Unpacking Tuple (Membongkar Isi) ---")
# Kita bisa memasukkan nilai tuple langsung ke variabel
x, y = koordinat
print(f"Koordinat asli: {koordinat}")
print(f"Nilai x: {x}")
print(f"Nilai y: {y}")

mhs = ("Budi", "Informatika", 3.75)
nama, jurusan, ipk = mhs
print(f"Mahasiswa: {nama}, Jurusan: {jurusan}, IPK: {ipk}")
print()

print("--- 5. Operasi Tuple ---")
angka = (1, 2, 3, 1, 4, 1, 5)

# count() -> Menghitung jumlah kemunculan
print(f"Tuple angka: {angka}")
print(f"Angka 1 muncul: {angka.count(1)} kali")

# index() -> Mencari posisi pertama
print(f"Angka 4 ada di index ke: {angka.index(4)}")

# len() -> Panjang tuple
print(f"Panjang tuple: {len(angka)}")
print()

print("--- 6. Kapan Pakai List vs Tuple? ---")
print("Gunakan LIST jika:")
print("- Data akan sering berubah (ditambah, dihapus, diedit).")
print("- Contoh: Daftar belanja, antrian tiket, log chat.")
print()
print("Gunakan TUPLE jika:")
print("- Data bersifat tetap/konstan (tidak boleh berubah).")
print("- Ingin performa lebih cepat (iterasi tuple lebih cepat sedikit dari list).")
print("- Sebagai key dalam dictionary (karena immutable).")
print("- Contoh: Nama hari, Koordinat (latitude, longitude), konfigurasi database.")
