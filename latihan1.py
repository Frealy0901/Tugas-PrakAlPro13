jmlh_ktgri = int(input("masukan jumlah kategori : "))
data_aplikasi = {}

for i in range(jmlh_ktgri):
    nama = input("masukan nama katgori : ")
    print("masukan 5 nama aplikasi di kategori ", nama)
    apk = list()
    
    for j in range(5):
        nama_apk = input("masukan nama aplikasi : ")
        apk.append(nama_apk)
    data_aplikasi[nama] = apk
print(data_aplikasi)
print()

daftar_apk = list()
for apk in data_aplikasi.values():
    daftar_apk.append(set(apk))
print(daftar_apk)
print()

hasil = daftar_apk
for x in range(1,jmlh_ktgri):
    unik = daftar_apk[i] ^ daftar_apk[i-1]
else:
    unik = daftar_apk[0] ^ daftar_apk[i]
print()
print("apllikasi yang hanya muncul di satu kategori saja: ", unik)

print()
if jmlh_ktgri > 2:
    for y in range(1,jmlh_ktgri):
        intr = daftar_apk[i] and daftar_apk[i-1]
    else:
        intr = daftar_apk[0] and daftar_apk[i]
    print("aplikasi yang muncul di dua kategori sekaligus:", intr)
