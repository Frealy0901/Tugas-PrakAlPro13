teks1 = input("Masukkan file teks 1: ") #meminta user memasukan inputan  file teks
teks2 = input("Masukkan file teks 2: ")
try: # menggunakan try dan except jika ada salah masukan dari user
    handle = open(teks1, 'r') # ini akan membuka file tersebut dan membaca teks tersebut
    handle2 = open(teks2, 'r')
except:
    print("File cannot be opened")
    exit()
a = set() # membuat set yang kosong

for teks in handle: # mengulang teks disetiap handle
    tekslow = teks.lower() # membuat semua teks kata menjadi huruf kecil
    tekspl = tekslow.split()  # split setiap kata 
    for b in tekspl: # untuk teksp1 dimasukan kedalam b
        a.add(b) # b ditambahkan kedalam variabel a
for teks in handle2: # mengulang teks disetiap handle
    tekslow = teks.lower() # membuat semua teks kata menjadi huruf kecil
    tekspl = tekslow.split() # split setiap kata 
    for b in tekspl: # untuk teksp1 dimasukan kedalam b
        a.add(b) # untuk teksp1 dimasukan kedalam b
print(a) # memunculkan variabel a 