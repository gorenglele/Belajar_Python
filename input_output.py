angka = input("Masukkan angka: ")
angka1 = input("Masukkan angka lagi: ")

result = angka + angka1
print("Hasil penjumlahan:", result)

data = input("Masukkan tag (pisahkan dengan koma): ")
# Contoh input user: python,coding,belajar

list_tag = data.split(",") 

print(list_tag)
# Output: ['python', 'coding', 'belajar']

test = "saya suka belajar python"
list_kata = test.split(" ") 

