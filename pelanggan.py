class Pelanggan:

    def __init__(self, nama, nohp, email):
        self.nama = nama
        self.__nohp = nohp
        self.__email = email

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
    def setemail(self):
        pass

    @property
    def getemail(self):
        pass

    @setemail.setter
    def setemail(self, input):
        self.__email = input

    @getemail.getter
    def getemail(self):
        return self.__email