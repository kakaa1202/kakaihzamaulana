Nilai_Tugas = int(input("masukkan nilai tugas :"))
Uts = int(input("masukkan nilai Uts :"))
Uas = int(input("masukkan nilai Uas :"))
kehadiran_mahasiswa = int(input("masukkan nilai kehadiran :"))

nilai_akhir = (20 / 100 * Nilai_Tugas) + (30 / 100 * Uts) + (50 / 100 * Uas)

print ("======Hasil======")
print ("Nilai akhir =", nilai_akhir)
print (kehadiran_mahasiswa,"%")

if nilai_akhir >= 70 and kehadiran_mahasiswa >= 80:
    if nilai_akhir >= 70 and kehadiran_mahasiswa >= 80 and nilai_akhir % 2 == 0:
        print("Status      :LULUS DENGAN PREDIKAT")
    elif nilai_akhir>= 60 and kehadiran_mahasiswa >= 70:
        print("Status      :LULUS")
else:
    print("Status       :BELUM LULUS")