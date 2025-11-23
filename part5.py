 # operasi aritmatika

 # X / + -

# operasi penjumlahan +

a = 12
b = 9
hasil = a + b
print(a, "+", b, "=", hasil)

# pengurangan -

a = 9
b = 12
hasil = a -b
print(a, "-", b, "=", hasil)

# perkalian *

a = 9
b = 12
hasil = a * b
print(a, "x", b, "=", hasil)

# pembagian /

a = 15
b = 4
hasil = a/b
print(a, ":", b, "=", hasil)

# perpangkatan menggunakan ** (eksponesial)

a = 9
b = 12
hasil = a ** b
print(a, "pangkat", b, "=", hasil)

#sisa pembagian (modulus) %

a = 12
b = 9
hasil = a % b
print(a, "mod", b, "=", hasil)

# floor division

a = 15
b = 4
hasil = a // b
print(a, "floor divison", b, "=", hasil)



# operasi prioritas
# 1 ()
# perpangkatan / akar
# perkalian pembagian
# penjumlahan pengurarang
# buatlah opreasi penjumlahan yang menggabungkan semua operasi diatas

a = 16
b = 8
c = 10

hasil = (a + b) + a**1 - (b % c) + (b // c) *1
print ("hasil operasi gabungan =",hasil)