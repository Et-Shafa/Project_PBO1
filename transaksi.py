class Catat:

    def __init__(self, tglselesai, jumlahpakaian, statusbayar):
        self.tglselesai = tglselesai
        self.jumlahpakaian = jumlahpakaian
        self.statusbayar = statusbayar

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

    def totalhargajenis(self, beratjenis, harga):
        totalharga = beratjenis*harga
        return totalharga

    @property
    def setstatusbayar(self):
        pass

    @property
    def getstatusbayar(self):
        pass

    @setstatusbayar.setter
    def setstatusbayar(self, input):
        self.statusbayar = input

    @getstatusbayar.getter
    def getstatusbayar(self):
        return self.statusbayar
