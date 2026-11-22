from paket_wisata import PaketWisata
class WisataBudaya(PaketWisata):
    def __init__(self, kode_paket, nama_paket, harga, kuota, daerah_budaya, jenis_budaya, pemandu_lokal):
        super().__init__(kode_paket, nama_paket, harga, kuota)

        self.__daerah_budaya = daerah_budaya
        self.__jenis_budaya = jenis_budaya
        self.__pemandu_lokal = pemandu_lokal

    def get_daerah_budaya(self):
        return self.__daerah_budaya

    def get_jenis_budaya(self):
        return self.__jenis_budaya

    def get_pemandu_lokal(self):
        return self.__pemandu_lokal

    def ubah_pemandu_lokal(self, pemandu_baru):
        if not pemandu_baru.strip():
            return False
        self.__pemandu_lokal = pemandu_baru.strip()
        return True

    def info_wisata_budaya(self):
        return (
            f"Daerah: {self.__daerah_budaya} | "
            f"Jenis: {self.__jenis_budaya} | "
            f"Pemandu: {self.__pemandu_lokal}"
        )

    def tampilkan_info(self):
        print("[KATEGORI: WISATA BUDAYA]")
        super().tampilkan_info()
        print(f"Daerah       : {self.__daerah_budaya}")
        print(f"Jenis Budaya : {self.__jenis_budaya}")
        print(f"Pemandu Lokal: {self.__pemandu_lokal}")