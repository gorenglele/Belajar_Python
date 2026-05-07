# Belajar Lambda di Python

Lambda function di Python adalah fungsi anonim (tanpa nama) yang dibuat menggunakan keyword `lambda`. Fungsi ini sangat berguna ketika kita membutuhkan fungsi sederhana yang hanya digunakan sesekali, terutama sebagai argumen untuk fungsi tingkat tinggi (*higher-order functions*) seperti `map()`, `filter()`, dan `sorted()`.

## Sintaks Dasar
```python
lambda argumen: ekspresi
```

## Perbedaan Lambda vs Function Biasa (`def`)

| Fitur | Function Biasa (`def`) | Lambda Function |
| :--- | :--- | :--- |
| **Kata Kunci** | Menggunakan `def` | Menggunakan `lambda` |
| **Nama** | Memiliki nama (terikat dengan identifier) | Anonim (tidak memiliki nama bawaan) |
| **Baris Kode** | Bisa banyak baris (*multiple statements*) | Hanya satu baris ekspresi tunggal |
| **Return Value** | Harus menulis `return` secara eksplisit | Otomatis mengembalikan hasil (implisit) |
| **Kompleksitas** | Bisa memuat loop, kondisi bertingkat, dll | Hanya bisa satu ekspresi logika sederhana |

## Cara Menjalankan Contoh Code
Buka terminal dan jalankan file Python berikut:
```bash
python lambda_example.py
python perbedaan.py
```
