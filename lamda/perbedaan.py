def main():
    print("=== Perbedaan Function Biasa vs Lambda ===")
    
    # ----------------------------------------------------
    # 1. PENGGUNAAN DASAR
    # ----------------------------------------------------
    print("\n1. PENGGUNAAN DASAR:")
    
    # Menggunakan function biasa (def)
    def kuadrat_def(x):
        return x ** 2
    
    # Menggunakan lambda
    kuadrat_lambda = lambda x: x ** 2
    
    print(f"Hasil fungsi biasa: {kuadrat_def(5)}")
    print(f"Hasil lambda      : {kuadrat_lambda(5)}")


    # ----------------------------------------------------
    # 2. LOGIKA KONDISIONAL (If-Else)
    # ----------------------------------------------------
    print("\n2. LOGIKA KONDISIONAL (If-Else):")
    
    # Menggunakan function biasa (def)
    def cek_genap_def(x):
        if x % 2 == 0:
            return "Genap"
        else:
            return "Ganjil"

    # Menggunakan lambda
    # Catatan: Lambda hanya mendukung bentuk "A if kondisi else B" (Ternary Operator)
    cek_genap_lambda = lambda x: "Genap" if x % 2 == 0 else "Ganjil"
    
    print(f"Fungsi biasa (angka 10) : {cek_genap_def(10)}")
    print(f"Lambda       (angka 10) : {cek_genap_lambda(10)}")


    # ----------------------------------------------------
    # 3. KETERBATASAN LAMBDA
    # ----------------------------------------------------
    print("\n3. KETERBATASAN LAMBDA:")
    print("Fungsi 'def' bisa memuat banyak baris proses kompleks seperti loop, try-except, dll.")
    print("Lambda tidak bisa melakukan iterasi 'for' loop multi-baris secara langsung.")
    
    def proses_kompleks_def(data):
        hasil = []
        for x in data:
            if x > 0:
                hasil.append(x * 2)
            else:
                hasil.append(0)
        return hasil

    print(f"Hasil fungsi kompleks (def): {proses_kompleks_def([-1, 2, -3, 4])}")
    print("Hal di atas sangat sulit atau tidak direkomendasikan ditulis pakai Lambda.")

if __name__ == "__main__":
    main()
