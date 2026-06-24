data_siswa = []

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai siswa: "))

    rata = nilai  
    grade = tentukan_grade(rata)
    siswa = {
        "nama": nama,
        "nilai": nilai,
        "rata": rata,
        "grade": grade
    }

    data_siswa.append(siswa)
    print("Data berhasil ditambahkan!\n")

def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

def tampilkan_data():
    if len(data_siswa) == 0:
        print("Belum ada data!\n")
    else:
        print("\n=== DATA SISWA ===")
        for siswa in data_siswa:
            print(f"Nama  : {siswa['nama']}")
            print(f"Nilai : {siswa['nilai']}")
            print(f"Rata  : {siswa['rata']}")
            print(f"Grade : {siswa['grade']}")
            print("------------------")

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data Siswa")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")