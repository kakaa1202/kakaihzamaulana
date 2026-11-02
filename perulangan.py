# Program Sistem Penilaian Mahasiswa dengan For, If, dan Input

# Memasukkan jumlah mahasiswa
jumlah_mhs = int(input("jumlah mahasiswa : "))

total_nilai = 0

# Perulangan untuk memasukkan nilai setiap mahasiswa
for i in range(1, jumlah_mhs + 1):
    nilai = float(input(f"Masukkan Nilai mahasiswa {i} : "))
    total_nilai += nilai
    
    #menentukan status/label nilai per mahasiswa
    if nilai >= 75:
        status = "Lulus"
    else:
        status = "Remedial"
        
    print(f"Status mahasiswa {i}: {status}")

# Menghitung nilai rata-rata
rata_rata = total_nilai / jumlah_mhs

print(f"\nNila rata - rata : {rata_rata}")