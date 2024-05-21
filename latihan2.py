data = 'saya pergi ke pasar' # masukan kalimat 
data_list = list(data) # rubah kalimmat tersebut kedalam list

print("list ke set") # memunculkan list ke set
print("sebelum ->",data_list) # memunculkan data list
print("sesudah ->", set(data_list)) # memunculkan data list yang dirubah ke set
print() # memunculkan print kosong 
data_set = set(data) # membuat variabel data set dan rubah kalimat yang sudah ada menjadi set
print("set ke list")  # memunculkan set ke list
print("sebelum -> ", data_set) # memunculkan set sebelum dirubah ke list
print("sesudah -> ", list(data_set)) # memunculkan sesudah dirubah ke list
print() # memunculkan print kosong
data_tuple = tuple(data) # membuat variabel data tuple dan rubah kalimat yang sudah dimasukan ke tuple
print("tuple ke set") # memunculkan tuple ke set
print("sebelum -> ", data_tuple) # memunculkan data tuple yang belum di rubah ke set
print("sesudah -> ", set(data_tuple)) # memunculkan data tuple yang sudah dirubah ke set
print() # memunculkan print kosong
print("set ke tuple") # memunculkan set ke tuple
print("sebelum -> ",data_set) # sebelum di rubah ketuple
print("sesudah -> ", tuple(data_set)) # sesudah dirubah ke tuple