class Tipe:
    def __init__(self, idjenis, jenis, hargajenis):
        self.idjenis = idjenis
        self.jenis = jenis
        self.hargajenis = hargajenis

    @property
    def setidjenis(self):
        pass

    @property
    def getidjenis(self):
        pass

    @setidjenis.setter
    def setidjenis(self, input):
        self.idjenis = input

    @getidjenis.getter
    def getidjenis(self):
        return self.idjenis

    @property
    def setjenis(self):
        pass

    @property
    def getjenis(self):
        pass

    @setjenis.setter
    def setjenis(self, input):
        self.jenis = input

    @getjenis.getter
    def getjenis(self):
        return self.jenis

    @property
    def sethargajenis(self):
        pass

    @property
    def gethargajenis(self):
        pass

    @sethargajenis.setter
    def sethargajenis(self, input):
        self.hargajenis = input

    @gethargajenis.getter
    def gethargajenis(self):
        return self.hargajenis
