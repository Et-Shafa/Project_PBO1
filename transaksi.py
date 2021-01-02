class Catat:

    def __init__(self, tglselesai, jumlahpakaian):
        self.tglselesai = tglselesai
        self.jumlahpakaian = jumlahpakaian

    @property
    def settglselesai(self):
        pass

    @property
    def gettglselesai(self):
        pass

    @settglselesai.setter
    def settglselesai(self, input):
        self.tglselesai = input

    @gettglselesai.getter
    def gettglselesai(self):
        return self.tglselesai

    @property
    def setjumlahpakaian(self):
        pass

    @property
    def getjumlahpakaian(self):
        pass

    @setjumlahpakaian.setter
    def setjumlahpakaian(self, input):
        self.jumlahpakaian = input

    @getjumlahpakaian.getter
    def getjumlahpakaian(self):
        return self.jumlahpakaian

    # def totalhargajenis(self, jenis, hargajenis):
    #     jenis = jenislaundry.Tipe.getjenis
    #     hargajenis = jenislaundry.Tipe.gethargajenis
    #
    # def hargatotal(self):
    #     return self.totalharga + 10

        # jenis laundry, pilihan
        # harga, pilihan
        # (jumlah, total(dari jenis cuci)), program
        # harga total program

        # fitur(1. catat transaksi, 2. rekap)

# class Nota(Catat):
