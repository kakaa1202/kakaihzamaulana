targets = {"andi": 70, "budi": 75, "citra": 80}

nama = input("Nama : ").strip()
target = targets.get(nama.lower())

if target is None:
    print("Nama mahasiswa tidak ditemukan.")
else:
    print(f"Target nilai {nama}: {target}")

    percobaan = 0
    lulus = False

    while percobaan < 3 and not lulus:
        percobaan += 1
        nilai = int(input(f"Nilai {percobaan} : "))
        if nilai >= target:
            lulus = True

    if lulus:
        print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
    else:
        print(f"{nama} tidak lulus setelah {percobaan} kali percobaan!")