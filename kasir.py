from operator import truediv

total = 0
barang = []
harga = []

while True:
    print("""Daftar Barang\n
    1. Roti \t 5000
    2. Es Krim \t 7000
    3. Keripik \t 8000
    4. Buku \t 5000
    5. Pensil \t 7000
    """)

    kode = int(input("masukkan kode barang :"))
    if kode == 1:
        barang.append('roti')
        harga.append('5000')
        total += 5000
    elif kode == 2:
        barang.append('Es Krim')
        harga.append('7000')
        total += 7000
    elif kode == 3:
        barang.append('Keripik')
        harga.append('8000')
        total += 8000
    elif kode == 4:
        barang.append('Buku')
        harga.append('5000')
        total += 5000
    elif kode == 5:
        barang.append('Pensil')
        harga.append('7000')
        total += 7000

    else:
        print('kode tidak valid')

    lanjut = input('lanjut belanja (y/t) :')
    if lanjut == 't' :
        print("")
        break

print('barang yang dibeli :', barang)
print('harga barangnya :', harga)
print('total bayar :', total, '\n')

uang = int(input('masukkan uang anda :'))
if uang > total:
    print('kembalinya :', uang - total)
elif uang == total:
    print('uang pas')
else:
    print('uangnya kurang', uang - total)
    input('')


    