# Materi Manipulasi String (String Manipulation) di Python

# 1. Penggabungan String (Concatenation)
nama_depan = "Budi"
nama_tengah = "gess"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print("1. Penggabungan String:")
print("Nama lengkap:", nama_lengkap)
print("-" * 30) # Ini juga bentuk repitisi (pengulangan string)

# 2. String Slicing (Memotong String)
# string[start:stop:step]
teks = "Belajar Python asik sekali"
print("2. String Slicing:")
print("Teks Asli:", teks)
print("Dari index 8 sampai 14:", teks[8:14])    # Mengambil kata "Python"
print("Dari awal sampai index 7:", teks[:9])    # Mengambil kata "Belajar"
print("Dari index 15 sampai akhir:", teks[8:]) # Mengambil kata "asik sekali"
print("String dibalik:", teks[::-1])            # Membalik urutan huruf
print("-" * 30)

# 3. Method String Bawaan (Built-in String Methods)
kalimat = "   halo Selamat DaTang Di dUNia PYTHON   "
print("3. Built-in String Methods:")
print("Kalimat asli:", repr(kalimat))
print("Upper (Huruf Besar):", kalimat.upper())
print("Lower (Huruf Kecil):", kalimat.lower())
print("Title (Kapital di setiap kata):", kalimat.title())
print("Capitalize (Kapital di awal kalimat):", kalimat.capitalize())
print("Strip (Menghilangkan spasi di awal dan akhir):", repr(kalimat.strip()))

# Mengganti kata (Replace)
kalimat_baru = kalimat.strip()
print("Replace 'PYTHON' dengan 'Programming':", kalimat_baru.replace("PYTHON", "Programming"))
print("-" * 30)

# 4. Split and Join (Memecah dan Menggabungkan String)
print("4. Split dan Join:")
data_csv = "Apel,Jeruk,Mangga,Pisang"
list_buah = data_csv.split(",") # Memecah string menjadi list
print("Hasil split (String -> List):", list_buah)

gabungan_buah = " & ".join(list_buah) # Menggabungkan list menjadi string
print("Hasil join (List -> String):", gabungan_buah)
print("-" * 30)

# 5. String Formatting (Format String)
print("5. String Formatting:")
nama = "Lendra"
umur = 20
pekerjaan = "Programmer"

# Cara 1: F-String (Paling disarankan dan modern di Python 3.6+)
info_fstring = f"Halo, perkenalkan nama saya {nama}. Saya berumur {umur} tahun dan bekerja sebagai {pekerjaan}."
print("F-String:", info_fstring)

# Cara 2: .format()
info_format = "Halo, perkenalkan nama saya {}. Saya berumur {} tahun dan bekerja sebagai {}.".format(nama, umur, pekerjaan)
print("Format():", info_format)
print("-" * 30)

# 6. Pengecekan pada String (Boolean Methods)
tes_kata = "Python2023"
print("6. Pengecekan Boolean pada String:")
print(f"Apakah '{tes_kata}' isalnum() (huruf/angka)?", tes_kata.isalnum())
print(f"Apakah '{tes_kata}' isalpha() (hanya huruf)?", tes_kata.isalpha())
print(f"Apakah '{tes_kata}' isdigit() (hanya angka)?", tes_kata.isdigit())

cek_huruf_kecil = "semua kecil"
print(f"Apakah '{cek_huruf_kecil}' islower()?", cek_huruf_kecil.islower())
print("-" * 30)
