import pickle

# Load mode dari file
filename = "olah-data-predik.data"
with open(filename, 'rb') as file:
    model = pickle.load(file)

#contoh default data
default = [[ 0.087, 0.030, 0.024, 10.756 ]]
print("contoh data default pendapatan")
print(default)

#baca input
x1 = input("Entry tahun 2010: ")
x2 = input("Entry tahun 2011: ")
x3 = input("Entry tahun 2012: ")
x4 = input("Entry tahun 2013: ")

Xuji = [[ float(x1), float(x2), float(x3), float(x4) ]]

#prediksi dari model
print(model.predict(Xuji))