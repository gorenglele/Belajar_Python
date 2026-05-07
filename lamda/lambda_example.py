def main():
    print("=== Contoh Penggunaan Lambda di Python ===")
    
    # 1. Lambda Dasar
    # Membuat fungsi lambda untuk penjumlahan
    add = lambda x, y: x + y
    print(f"\n1. Penjumlahan dengan lambda (2 + 3): {add(2, 3)}")

    # 2. Menggunakan lambda dengan fungsi map()
    # map() menerapkan fungsi ke setiap elemen dalam iterable
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(f"\n2. Mengkuadratkan list angka dengan map():")
    print(f"   List awal : {numbers}")
    print(f"   Hasil     : {squared_numbers}")

    # 3. Menggunakan lambda dengan fungsi filter()
    # filter() menyaring elemen berdasarkan kondisi fungsi (yang mengembalikan True)
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"\n3. Menyaring angka genap dengan filter():")
    print(f"   Angka genap: {even_numbers}")

    # 4. Menggunakan lambda untuk mengurutkan data (sorted/sort)
    # sort() menggunakan argumen 'key' untuk menentukan dasar pengurutan
    pairs = [(1, 'satu'), (4, 'empat'), (3, 'tiga'), (2, 'dua')]
    
    # Urutkan berdasarkan elemen kedua dari tuple (indeks 1)
    pairs.sort(key=lambda pair: pair[1])
    print(f"\n4. Mengurutkan list of tuples berdasarkan teks (elemen ke-2):")
    print(f"   Hasil urutan: {pairs}")

if __name__ == "__main__":
    main()
