import os
# soal 2 bagian a
# contoh program kuis menggunakan for

# isi pilihan jawaban
pilihan_jwbn = ["Jokowi", "Joko Widodo", "Pranowo"]
jwbn_benar = "Joko Widodo"
print ("="*4, "Selamat Belajar", "="*4)
print ("\nSiapakah Presiden Indonesia saat ini?")

for i in (pilihan_jwbn):
    print (i)

a = input ("Jawaban Anda: ")

if jwbn_benar == a:
    if os.name == 'nt':
        os.system('cls')
    print ("Jawaban Anda Benar")
else:
    print ("Salah")

# soal 2 bagian b
print("="*3, "Program Array Pada Nama + Menggunakan Perulangan While", "="*3)
nama_depan = input("Masukkan Nama Depan Anda: ")
nama_tengah = input("Masukkan Nama Tengah Anda: ")
nama_belakang = input("Masukkan Nama Belakang Anda: ")

db_nama = [nama_depan, nama_tengah, nama_belakang]

i = 0
nama_lengkap = ""

while i < len(db_nama):
    if db_nama[i]:  # Cek apakah nilai tidak kosong
        nama_lengkap += db_nama[i] + " "
    else:
        nama_lengkap += "Tidak Ada " + db_nama[i] + " "  # Jika kosong, tambahkan pesan

    i += 1

print("\nNama Lengkap Anda adalah:", nama_lengkap.strip())
