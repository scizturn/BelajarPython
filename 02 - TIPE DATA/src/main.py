# Tipe data = macam macam data di python

# a = 10, a adalah variable dengan nilai 10

# tipe data: Angka satuan (integer)
data_integer = 1 # yang tidak desimal
print("data : ", data_integer, ", bertipe :", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float, ", bertipe :", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "scizturn"
print("data : ", data_string, ", bertipe :", type(data_string))

# tipe data: biner true/fales (boolean)
data_bool = True
print("data : ", data_bool, ", bertipe :", type(data_bool))

## tipe data khusus

#bilangan kompleks
data_complex = complex (5,6)
print("data : ", data_complex, ", bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double #contoh

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe :", type(data_c_double))

