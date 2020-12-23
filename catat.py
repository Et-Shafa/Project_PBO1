import jenislaundry as jenislaundry


class Catat:

    def __init__(self, nama, nohp, tglselesai, jumlahbaju, totalharga):
        self.nama = nama
        self.__nohp = nohp
        self.tglselesai = tglselesai
        self.jumlahbaju = jumlahbaju
        self.totalharga = totalharga

    @property
    def settotalharga(self):
        pass

    @property
    def gettotalharga(self):
        pass

    @settotalharga.setter
    def settotalharga(self, input):
        self.totalharga = input

    @gettotalharga.getter
    def gettotalharga(self):
        return self.totalharga

    def totalhargajenis(self, jenis, hargajenis):
        jenis = jenislaundry.Tipe.getjenis
        hargajenis = jenislaundry.Tipe.gethargajenis

    def hargatotal(self):
        return self.totalharga + 10

        # jenis laundry, pilihan
        # harga, pilihan
        # (jumlah, total(dari jenis cuci)), program
        # harga total program

        # fitur(1. catat transaksi, 2. rekap)

# class Nota(Catat):
