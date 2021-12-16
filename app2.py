numbers_mapping = {
    "1" :"satu",
    "2" :"dua",
    "3" :"tiga",
    "4" :"empat"

    }

numbers = input ("Masukkan angka : ")

output = ""

for n in numbers:
    terbilang = numbers_mapping.get(n, "invalid")

    output = output + terbilang + " "

print (output)