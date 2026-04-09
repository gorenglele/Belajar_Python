class KTP:
    def __init__(self, nik, nama, kota):
        self.nik = nik
        self.nama = nama
        self.kota = kota

    def info(self):
        return f"{self.nama} ({self.nik}) - {self.kota}"

    def pindah_kota(self, kota_baru):
        kota_lama = self.kota
        self.kota = kota_baru
        print(f"{self.nama} pindah dari {kota_lama} ke {kota_baru}")

# Bikin KTP
andi = KTP("3201010101", "Andi", "Bandung")
budi = KTP("3171020202", "Budi", "Jakarta")

print(andi.info())         # Andi (3201010101) - Bandung
andi.pindah_kota("Surabaya")  # Andi pindah dari Bandung ke Surabaya
print(andi.info())         # Andi (3201010101) - Surabaya