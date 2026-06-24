tugas = []

def tambah_tugas():
    tugas_baru = input("Masukkan tugas: ")
    tugas.append(tugas_baru)
    print("Tugas berhasil ditambahkan!")

def lihat_tugas():
    if len(tugas) == 0:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i in range(len(tugas)):
            print(f"{i+1}. {tugas[i]}")

def tandai_selesai():
    lihat_tugas()
    if len(tugas) > 0:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        tugas[nomor - 1] = tugas[nomor - 1] + " (Selesai)"
        print("Tugas berhasil ditandai selesai!")

def hapus_tugas():
    lihat_tugas()
    if len(tugas) > 0:
        nomor = int(input("Masukkan nomor tugas yang dihapus: "))
        tugas.pop(nomor - 1)
        print("Tugas berhasil dihapus!")

while True:
    print("\n===== TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        tandai_selesai()
    elif pilihan == "4":
        hapus_tugas()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")