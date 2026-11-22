from wisata_alam import WisataAlam
from wisata_budaya import WisataBudaya
from pelanggan import Pelanggan


def cari_paket_by_kode(daftar_paket, kode):
    for paket in daftar_paket:
        if paket.get_kode_paket().lower() == kode.lower():
            return paket
    return None


def cari_pelanggan_by_id(daftar_pelanggan, id_pelanggan):
    for plg in daftar_pelanggan:
        if plg.get_id_pelanggan().lower() == id_pelanggan.lower():
            return plg
    return None


def main():
    daftar_paket = [
        WisataAlam(
            "PW001", "Eksplorasi Kawah Putih", 350000, 10,
            "Ciwidey, Kab. Bandung", "Mudah", "Jaket Tebal & Masker"
        ),
        WisataAlam(
            "PW002", "Pendakian Sunrise Gunung Putri", 275000, 5,
            "Lembang, Bandung Barat", "Sedang", "Sepatu Tracking & Senter"
        ),
        WisataBudaya(
            "PW003", "Tur Seni Saung Angklung Udjo", 220000, 8,
            "Bandung Timur", "Seni Musik & Tari Tradisional", "Kang Asep"
        ),
    ]

    pandu = Pelanggan("PL001", "Pandu Malik Samudra", "082380997587", "pandu@email.com")
    pandu.pesan_paket(daftar_paket[0], 2)
    pandu.pesan_paket(daftar_paket[2], 1)

    daftar_pelanggan = [pandu]

    while True:
        print("\n===================================================")
        print("      APLIKASI PAKET WISATA - BIRO PERJALANAN      ")
        print("===================================================")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Ubah Data")
        print("5. Cek Status Data")
        print("6. Keluar dari Program")
        print("===================================================")

        pilihan = input("Pilih menu (1-6): ").strip()
        if pilihan == "1":
            print("\n--- SUBMENU TAMBAH DATA ---")
            print("1. Tambah Paket Wisata Alam")
            print("2. Tambah Paket Wisata Budaya")
            print("3. Tambah Pelanggan Baru")
            print("4. Pemesanan Paket Wisata oleh Pelanggan")
            sub = input("Pilih jenis data (1-4): ").strip()

            try:
                if sub == "1":
                    kode = input("Kode Paket (mis. PW004)                : ").strip()
                    if cari_paket_by_kode(daftar_paket, kode):
                        print("Gagal: Kode paket sudah terdaftar!")
                        continue
                    nama = input("Nama Paket                             : ").strip()
                    harga = int(input("Harga (Rp)                             : "))
                    kuota = int(input("Kuota Peserta                          : "))
                    lokasi = input("Lokasi Wisata Alam                     : ").strip()
                    kesulitan = input("Tingkat Kesulitan (Mudah/Sedang/Sulit) : ").strip().capitalize()
                    perlengkapan = input("Perlengkapan Wajib                     : ").strip()

                    daftar_paket.append(
                        WisataAlam(kode, nama, harga, kuota, lokasi, kesulitan, perlengkapan)
                    )
                    print("Berhasil menambahkan data Paket Wisata Alam!")

                elif sub == "2":
                    kode = input("Kode Paket (mis. PW005)                : ").strip()
                    if cari_paket_by_kode(daftar_paket, kode):
                        print("Gagal: Kode paket sudah terdaftar!")
                        continue
                    nama = input("Nama Paket                             : ").strip()
                    harga = int(input("Harga (Rp)                             : "))
                    kuota = int(input("Kuota Peserta                          : "))
                    daerah = input("Daerah Budaya                          : ").strip()
                    jenis = input("Jenis Budaya                           : ").strip()
                    pemandu = input("Nama Pemandu Lokal                     : ").strip()

                    daftar_paket.append(
                        WisataBudaya(kode, nama, harga, kuota, daerah, jenis, pemandu)
                    )
                    print("Berhasil menambahkan data Paket Wisata Budaya!")

                elif sub == "3":
                    id_plg = input("ID Pelanggan (mis. PL002)              : ").strip()
                    if cari_pelanggan_by_id(daftar_pelanggan, id_plg):
                        print("Gagal: ID pelanggan sudah terdaftar!")
                        continue
                    nama = input("Nama Pelanggan                         : ").strip()
                    no_telp = input("No. Telepon                            : ").strip()
                    email = input("Email                                  : ").strip()

                    daftar_pelanggan.append(Pelanggan(id_plg, nama, no_telp, email))
                    print("Berhasil menambahkan data Pelanggan!")

                elif sub == "4":
                    id_plg = input("Masukkan ID Pelanggan                  : ").strip()
                    plg = cari_pelanggan_by_id(daftar_pelanggan, id_plg)
                    if not plg:
                        print("Data pelanggan tidak ditemukan!")
                        continue

                    kode = input("Masukkan Kode Paket Wisata             : ").strip()
                    paket = cari_paket_by_kode(daftar_paket, kode)
                    if not paket:
                        print("Data paket wisata tidak ditemukan!")
                        continue

                    jumlah = int(input("Jumlah Peserta yang Dipesan            : "))
                    if plg.pesan_paket(paket, jumlah):
                        print(f"Berhasil memesan paket '{paket.get_nama_paket()}' untuk {plg.get_nama()}!")
                    else:
                        print("Pemesanan gagal: Kuota tidak mencukupi atau jumlah tidak valid!")
                else:
                    print("Pilihan submenu tidak valid.")
            except ValueError as err:
                print(f"Terjadi kesalahan input: {err}")

        elif pilihan == "2":
            print("\n================== DAFTAR PAKET WISATA ==================")
            if not daftar_paket:
                print("Belum ada data paket wisata.")
            else:
                for paket in daftar_paket:
                    paket.tampilkan_info()
                    print("-" * 57)

            print("\n==================== DAFTAR PELANGGAN ====================")
            if not daftar_pelanggan:
                print("Belum ada data pelanggan.")
            else:
                for plg in daftar_pelanggan:
                    plg.tampilkan_info()
                    print("-" * 57)

        elif pilihan == "3":
            print("\n--- SUBMENU CARI DATA ---")
            print("1. Cari Paket Wisata (berdasarkan Kode / Nama)")
            print("2. Cari Pelanggan (berdasarkan ID / Nama)")
            sub = input("Pilih target pencarian (1-2): ").strip()

            if sub == "1":
                keyword = input("Masukkan Kode atau Nama Paket: ").strip().lower()
                ketemu = False
                for paket in daftar_paket:
                    if (
                        keyword in paket.get_kode_paket().lower()
                        or keyword in paket.get_nama_paket().lower()
                    ):
                        print()
                        paket.tampilkan_info()
                        print("-" * 45)
                        ketemu = True
                if not ketemu:
                    print("Paket wisata tidak ditemukan.")

            elif sub == "2":
                keyword = input("Masukkan ID atau Nama Pelanggan: ").strip().lower()
                ketemu = False
                for plg in daftar_pelanggan:
                    if (
                        keyword in plg.get_id_pelanggan().lower()
                        or keyword in plg.get_nama().lower()
                    ):
                        print()
                        plg.tampilkan_info()
                        print("-" * 45)
                        ketemu = True
                if not ketemu:
                    print("Pelanggan tidak ditemukan.")
            else:
                print("Pilihan submenu tidak valid.")

        elif pilihan == "4":
            print("\n--- SUBMENU UBAH DATA ---")
            print("1. Ubah Harga Paket Wisata")
            print("2. Tambah Kuota Paket Wisata")
            print("3. Ubah Detail Khusus Paket (Kesulitan Alam / Pemandu Budaya)")
            print("4. Ubah Email Pelanggan")
            print("5. Ubah No. Telepon Pelanggan")
            sub = input("Pilih data yang ingin diubah (1-5): ").strip()

            try:
                if sub == "1":
                    kode = input("Masukkan Kode Paket Wisata   : ").strip()
                    paket = cari_paket_by_kode(daftar_paket, kode)
                    if not paket:
                        print("Paket wisata tidak ditemukan!")
                        continue
                    harga_baru = int(input("Masukkan Harga Baru (Rp)     : "))
                    if paket.ubah_harga(harga_baru):
                        print(f"Harga '{paket.get_nama_paket()}' berhasil diubah menjadi Rp{paket.get_harga():,}!")
                    else:
                        print("Gagal: Harga baru tidak boleh negatif!")

                elif sub == "2":
                    kode = input("Masukkan Kode Paket Wisata   : ").strip()
                    paket = cari_paket_by_kode(daftar_paket, kode)
                    if not paket:
                        print("Paket wisata tidak ditemukan!")
                        continue
                    tambahan = int(input("Jumlah Kuota yang Ditambahkan: "))
                    if paket.tambah_kuota(tambahan):
                        print(f"Kuota '{paket.get_nama_paket()}' bertambah menjadi {paket.get_kuota()} peserta!")
                    else:
                        print("Gagal: Jumlah penambahan harus lebih dari 0!")

                elif sub == "3":
                    kode = input("Masukkan Kode Paket Wisata   : ").strip()
                    paket = cari_paket_by_kode(daftar_paket, kode)
                    if not paket:
                        print("Paket wisata tidak ditemukan!")
                        continue
                    if isinstance(paket, WisataAlam):
                        tingkat = input("Tingkat Kesulitan Baru (Mudah/Sedang/Sulit): ").strip().capitalize()
                        if paket.ubah_tingkat_kesulitan(tingkat):
                            print("Tingkat kesulitan Wisata Alam berhasil diperbarui!")
                        else:
                            print("Gagal: Pilihan tingkat kesulitan tidak valid!")
                    elif isinstance(paket, WisataBudaya):
                        pemandu = input("Nama Pemandu Lokal Baru: ").strip()
                        if paket.ubah_pemandu_lokal(pemandu):
                            print("Nama pemandu lokal Wisata Budaya berhasil diperbarui!")
                        else:
                            print("Gagal: Nama pemandu tidak boleh kosong!")

                elif sub == "4":
                    id_plg = input("Masukkan ID Pelanggan        : ").strip()
                    plg = cari_pelanggan_by_id(daftar_pelanggan, id_plg)
                    if not plg:
                        print("Pelanggan tidak ditemukan!")
                        continue
                    email_baru = input("Masukkan Email Baru          : ").strip()
                    if plg.ubah_email(email_baru):
                        print(f"Email {plg.get_nama()} berhasil diperbarui menjadi {plg.get_email()}!")
                    else:
                        print("Gagal: Format email tidak valid! Email lama tetap dipertahankan.")

                elif sub == "5":
                    id_plg = input("Masukkan ID Pelanggan        : ").strip()
                    plg = cari_pelanggan_by_id(daftar_pelanggan, id_plg)
                    if not plg:
                        print("Pelanggan tidak ditemukan!")
                        continue
                    telp_baru = input("Masukkan No. Telepon Baru    : ").strip()
                    if plg.ubah_no_telepon(telp_baru):
                        print(f"No. Telepon {plg.get_nama()} berhasil diperbarui menjadi {plg.get_no_telepon()}!")
                    else:
                        print("Gagal: Nomor telepon harus angka minimal 10 digit!")
                else:
                    print("Pilihan submenu tidak valid.")
            except ValueError:
                print("Input tidak valid: Harus berupa angka!")

        elif pilihan == "5":
            print("\n=== STATUS KETERSEDIAAN PAKET WISATA ===")
            for paket in daftar_paket:
                print(f"- [{paket.get_kode_paket()}] {paket.get_nama_paket()} -> {paket.cek_status()}")

            print("\n=== STATUS PEMESANAN PELANGGAN ===")
            for plg in daftar_pelanggan:
                print(f"- [{plg.get_id_pelanggan()}] {plg.get_nama()} -> {plg.cek_status_pesanan()}")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan Aplikasi Paket Wisata. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 sampai 6.")


if __name__ == "__main__":
    main()