try:
    hasil = 5 / "2"
    print("Hasil pembagian adalah =", hasil)
except ZeroDivisionError:
    # tangani error jiia ada bilangan yang dibagi dengan nol di blok try
    print("Bilangan tidak dapat dibagi dengan nol")
except TypeError:
    # tangani error jika kedua bilangan berbeda tipe data di blok try
    print("Kedua bilangan berbeda tipe")