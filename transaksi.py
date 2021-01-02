class Catat:

    def __init__(self, nama, nohp, tglselesai, jumlahpakaian):
        self.nama = nama
        self.__nohp = nohp
        self.tglselesai = tglselesai
        self.jumlahpakaian = jumlahpakaian

    @property
    def setnama(self):
        pass

    @property
    def getnama(self):
        pass

    @setnama.setter
    def setnama(self, input):
        self.nama = input

    @getnama.getter
    def getnama(self):
        return self.nama

    @property
    def setnohp(self):
        pass

    @property
    def getnohp(self):
        pass

    @setnohp.setter
    def setnohp(self, input):
        self.__nohp = input

    @getnohp.getter
    def getnohp(self):
        return self.__nohp

    @property
    def settglselesai(self):
        pass

    @property
    def gettglselesai(self):
        pass

    @settglselesai.setter
    def settglselesai(self, input):
        self.tglselesai = input

    @getnohp.getter
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
