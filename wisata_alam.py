from paket_wisata import PaketWisata
class WisataAlam(PaketWisata):
    def __init__(self, kode_paket, nama_paket, harga, kuota, lokasi_alam, tingkat_kesulitan, perlengkapan):
        super().__init__(kode_paket, nama_paket, harga, kuota)

        if tingkat_kesulitan not in ("Mudah", "Sedang", "Sulit"):
            raise ValueError("Tingkat kesulitan harus 'Mudah', 'Sedang', atau 'Sulit'!")

        self.__lokasi_alam = lokasi_alam
        self.__tingkat_kesulitan = tingkat_kesulitan
        self.__perlengkapan = perlengkapan

    def get_lokasi_alam(self):
        return self.__lokasi_alam

    def get_tingkat_kesulitan(self):
        return self.__tingkat_kesulitan

    def get_perlengkapan(self):
        return self.__perlengkapan

    def ubah_tingkat_kesulitan(self, tingkat_baru):
        if tingkat_baru not in ("Mudah", "Sedang", "Sulit"):
            return False
        self.__tingkat_kesulitan = tingkat_baru
        return True

    def info_wisata_alam(self):
        return (
            f"Lokasi: {self.__lokasi_alam} | "
            f"Kesulitan: {self.__tingkat_kesulitan} | "
            f"Perlengkapan: {self.__perlengkapan}"
        )

    def tampilkan_info(self):
        print("[KATEGORI: WISATA ALAM]")
        super().tampilkan_info()
        print(f"Lokasi Alam  : {self.__lokasi_alam}")
        print(f"Kesulitan    : {self.__tingkat_kesulitan}")
        print(f"Perlengkapan : {self.__perlengkapan}")