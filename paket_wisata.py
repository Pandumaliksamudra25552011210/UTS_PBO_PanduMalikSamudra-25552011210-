class PaketWisata:
    def __init__(self, kode_paket, nama_paket, harga, kuota):
        if harga < 0 or kuota < 0:
            raise ValueError("Harga dan kuota paket wisata tidak boleh negatif!")

        self.__kode_paket = kode_paket
        self.__nama_paket = nama_paket
        self.__harga = harga
        self.__kuota = kuota

    def get_kode_paket(self):
        return self.__kode_paket

    def get_nama_paket(self):
        return self.__nama_paket

    def get_harga(self):
        return self.__harga

    def get_kuota(self):
        return self.__kuota

    def ubah_harga(self, harga_baru):
        if harga_baru < 0:
            return False
        self.__harga = harga_baru
        return True

    def tambah_kuota(self, jumlah):
        if jumlah <= 0:
            return False
        self.__kuota += jumlah
        return True

    def kurangi_kuota(self, jumlah):
        if jumlah <= 0 or jumlah > self.__kuota:
            return False
        self.__kuota -= jumlah
        return True

    def cek_status(self):
        if self.__kuota > 0:
            return f"Tersedia (Sisa kuota: {self.__kuota} peserta)"
        return "Penuh (Kuota habis)"

    def tampilkan_info(self):
        print(f"Kode Paket   : {self.__kode_paket}")
        print(f"Nama Paket   : {self.__nama_paket}")
        print(f"Harga        : Rp{self.__harga:,}")
        print(f"Kuota        : {self.__kuota} peserta")
        print(f"Status       : {self.cek_status()}")