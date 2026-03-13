# ==========================================
# STUDI KASUS: LIST DAN TUPLE
# ==========================================
# Skenario:
# Kita membuat sistem sederhana untuk manajemen nilai siswa.
# - Data Siswa (Nama, NIM) -> Tuple (karena identitas jarang berubah)
# - Nilai Mata Pelajaran -> List (karena nilai bisa bertambah atau diremedial/diubah)

def main():
    print("=== PROGRAM MANAJEMEN NILAI SISWA ===")
    
    # 1. Menggunakan Tuple untuk Identitas (Immutable)
    # Format: (Nama, NIM)
    siswa1 = ("Raihan", "123456")
    
    # 2. Menggunakan List untuk Nilai (Mutable)
    nilai_siswa1 = [80, 90, 75]
    
    print(f"Mahasiswa: {siswa1[0]} (NIM: {siswa1[1]})")
    print(f"Nilai Awal: {nilai_siswa1}")
    
    # Menghitung Rata-rata Awal
    rata_rata = sum(nilai_siswa1) / len(nilai_siswa1)
    print(f"Rata-rata Awal: {rata_rata:.2f}")
    
    print("\n--- Skenario 1: Siswa Mengikuti Ujian Tambahan ---")
    # Menambah nilai baru ke List
    nilai_baru = 85
    nilai_siswa1.append(nilai_baru)
    print(f"Menambahkan nilai {nilai_baru}...")
    print(f"Daftar Nilai Sekarang: {nilai_siswa1}")
    
    print("\n--- Skenario 2: Perbaikan Nilai (Remedial) ---")
    # Mengubah nilai pertama (index 0) yang tadinya 80 menjadi 85
    print(f"Nilai pada index 0 (sebelum): {nilai_siswa1[0]}")
    nilai_siswa1[0] = 85
    print(f"Nilai pada index 0 (sesudah): {nilai_siswa1[0]}")
    print(f"Daftar Nilai Setelah Remedial: {nilai_siswa1}")
    
    # Menghitung Rata-rata Akhir
    rata_rata_akhir = sum(nilai_siswa1) / len(nilai_siswa1)
    print(f"\nRata-rata Akhir: {rata_rata_akhir:.2f}")

    print("\n--- Kesimpulan ---")
    print("Identitas siswa disimpan di TUPLE karena tidak boleh sembarangan diubah.")
    print("Nilai siswa disimpan di LIST karena dinamis (bisa tambah, ubah, hapus).")

if __name__ == "__main__":
    main()
