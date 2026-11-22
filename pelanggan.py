class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_telepon, email):
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__no_telepon = no_telepon
        self.__email = ""
        self.__daftar_pesanan = []

        if not self.ubah_email(email):
            raise ValueError("Format email awal tidak valid (harus mengandung '@' dan '.')!")

    def get_id_pelanggan(self):
        return self.__id_pelanggan

    def get_nama(self):
        return self.__nama

    def get_no_telepon(self):
        return self.__no_telepon

    def get_email(self):
        return self.__email

    def get_daftar_pesanan(self):
        return list(self.__daftar_pesanan)

    def ubah_email(self, email_baru):
        if "@" not in email_baru or "." not in email_baru:
            return False
        self.__email = email_baru
        return True

    def ubah_no_telepon(self, no_telepon_baru):
        if not no_telepon_baru.strip().isdigit() or len(no_telepon_baru.strip()) < 10:
            return False
        self.__no_telepon = no_telepon_baru.strip()
        return True

    def pesan_paket(self, paket_wisata, jumlah_peserta=1):
        if jumlah_peserta <= 0:
            return False
        if not paket_wisata.kurangi_kuota(jumlah_peserta):
            return False

        for item in self.__daftar_pesanan:
            if item[0] is paket_wisata:
                item[1] += jumlah_peserta
                return True

        self.__daftar_pesanan.append([paket_wisata, jumlah_peserta])
        return True

    def hitung_total_biaya(self):
        total = 0
        for paket, jumlah in self.__daftar_pesanan:
            total += paket.get_harga() * jumlah
        return total

    def cek_status_pesanan(self):
        if len(self.__daftar_pesanan) > 0:
            jumlah_jenis = len(self.__daftar_pesanan)
            total_peserta = sum(item[1] for item in self.__daftar_pesanan)
            return f"Aktif ({jumlah_jenis} paket wisata, total {total_peserta} peserta)"
        return "Belum memesan paket wisata"

    def tampilkan_info(self):
        print(f"ID Pelanggan : {self.__id_pelanggan}")
        print(f"Nama         : {self.__nama}")
        print(f"No. Telepon  : {self.__no_telepon}")
        print(f"Email        : {self.__email}")
        print(f"Status       : {self.cek_status_pesanan()}")

        if self.__daftar_pesanan:
            print("Rincian Paket Dipesan:")
            for paket, jumlah in self.__daftar_pesanan:
                subtotal = paket.get_harga() * jumlah
                print(
                    f"  - [{paket.get_kode_paket()}] {paket.get_nama_paket()} "
                    f"({jumlah} peserta x Rp{paket.get_harga():,}) = Rp{subtotal:,}"
                )
            print(f"Total Biaya  : Rp{self.hitung_total_biaya():,}")