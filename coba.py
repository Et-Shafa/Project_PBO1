import transaksi as catat
import pelanggan
import jenislaundry as jenisLaundry
import programdb as programdb
from datetime import datetime as dt


idpelanggan = input("ID Pelanggan : ")
tglterima = dt.now()
tglselesai = input("Tanggal Selesai : ")
tglselesai = dt.strptime(tglselesai, '%d-%m-%Y')
totalpakaian = input("Total pakaian : ")
tambah = True
total = 0
arrjenis = []
for a in arrjenis:
    print(a)
arrhargajenis = []
arrjumlahberatj = []
arrtotalhj = []
while tambah:
    programdb.viewjenis()
    idjenis = input("ID Jenis : ")
    jumlahberat = float(input("Jumlah berat : "))
    hargajenis = float(programdb.gethargajenis(idjenis))
    totalhargajenis = catat.Catat.totalhargajenis(1, jumlahberat, hargajenis)
    print("Total harga jenis :", totalhargajenis)
    arrjenis.append(idjenis)
    arrhargajenis.append(hargajenis)
    arrjumlahberatj.append(jumlahberat)
    arrtotalhj.append(totalhargajenis)
    total = total*totalhargajenis
    print(""""
Tambah ?
\t 1. Ya
\t 2. Tidak""")
    tran = catat.Catat(tglselesai, totalpakaian)
    # programdb.inserttra(idpelanggan, tglterima, tran.gettglselesai, tran.getjumlahpakaian, idjenis,
    #                     jumlahberat, totalhargajenis)
    pilihan = input("Pilihan : ")
    if pilihan == "1":
        pass
    else:
        tambah = False

print(""""
NOTA || Laundry.in
    Nama : {}
    Nomor Hp : {}
    Email: {}
    Tanggal diterima : {}
    Tanggal selesai : {}
    Total pakaian : {}
    Jenis \t\t\t Harga jenis \t\t\t Total berat \t\t\t Total Harga jenis
    {} \t\t\t {} \t\t\t {} \t\t\t {}
    Total harga : {}
        """.format(programdb.getdatapelanggan(idpelanggan, 1),
                   programdb.getdatapelanggan(idpelanggan, 2), programdb.getdatapelanggan(idpelanggan, 3),
                   tglterima, tglselesai, totalpakaian, arrjenis, arrhargajenis, arrjumlahberatj, arrtotalhj, total))


# import programdb as programDb
#
# a = input()
# programDb.gethargajenis(a)
#
# # from datetime import datetime as dtm
# # masuk_str = '05-08-2005'
# # masuk_date = dtm.strptime(masuk_str, '%d-%m-%Y')
# # print(masuk_date, type(masuk_date))
# #
# #
# #
# #
# # # from datetime import timedelta
# # # import requests
# # # # from bs4 import BeautifulSoup
# # #
# # #
# # # class Machine():
# # #
# # #     WASHER = "Washer"
# # #     DRYER = "Dryer"
# # #     AVAILABLE_STATUS = "Available"
# # #
# # #     def __init__(self, name, mtype, status, remaining_time):
# # #         self.name = name
# # #         self.type = mtype
# # #         self.status = status
# # #         self.remaining_time = remaining_time
# # #
# # #     @property
# # #     def is_washer(self):
# # #         return self.type == self.WASHER
# # #
# # #     @property
# # #     def is_dryer(self):
# # #         return self.type == self.DRYER
# # #
# # #     @property
# # #     def is_available(self):
# # #         return self.status == self.AVAILABLE_STATUS
# # #
# # #     def __str__(self):
# # #         if self.remaining_time > timedelta(minutes=2):
# # #             return "{} ({}) has {} minutes remaining".format(self.name, self.type,
# self.remaining_time.seconds // 60)
# # #         return "{} ({}) is {}".format(self.name, self.type, self.status)
# # #
# # #     @classmethod
# # #     def from_soup(cls, soup):
# # #         name = "".join(soup.select(".name")[0].stripped_strings)
# # #         mtype = soup.select(".type")[0].string
# # #         status = soup.select(".status")[0].string
# # #         remaining_time = "".join(soup.select(".time")[0].stripped_strings)
# # #         minutes = 0
# # #         if len(remaining_time) > 0:
# # #             minutes = int(remaining_time.split()[0])
# # #         return cls(name, mtype, status, timedelta(minutes=minutes))
# # #
# # #
# # # class Room():
# # #
# # #     HOUSING_PAGE = "https://housing.gmu.edu/laundry"
# # #     ENDPOINT = "http://quantum-cloud-2.alscloud.net/washalertweb/washalertweb.aspx?location={}"
# # #
# # #     def __init__(self, uuid):
# # #         self.uuid = uuid
# # #         self.washers = []
# # #         self.dryers = []
# # #         self.name = "Laundry Room"
# # #         self.populate_fields(uuid)
# # #
# # #     def populate_fields(self, uuid):
# # #         res = requests.get(self.ENDPOINT.format(uuid))
# # #         soup = BeautifulSoup(res.text, "html.parser")
# # #         table = soup.table
# # #         self.name = table.tr.string
# # #         rows = soup.table.find_all("tr")
# # #         machine_rows = [row for row in rows if row.get("class") is not None]
# # #         for machine_row in machine_rows:
# # #             machine = Machine.from_soup(machine_row)
# # #             if machine.is_washer:
# # #                 self.washers.append(machine)
# # #             elif machine.is_dryer:
# # #                 self.dryers.append(machine)
# # #
# # #     def get_available_washers(self):
# # #         return [washer for washer in self.washers if washer.is_available]
# # #
# # #     def get_available_dryers(self):
# # #         return [dryer for dryer in self.dryers if dryer.is_available]
# # #
# # #     def print_info(self):
# # #         print("Washers:")
# # #         for washer in self.washers:
# # #             print("\t", washer)
# # #         print("Dryers")
# # #         for dryer in self.dryers:
# # #             print("\t", dryer)
# # #
# # #     def __str__(self):
# # #         return "{}: {}/{} open washers, {}/{} open dryers".format(self.name,
# # #                                                                   len(self.get_available_washers(
# # #                                                                   )),
# # #                                                                   len(self.washers),
# # #                                                                   len(self.get_available_dryers(
# # #                                                                   )),
# # #                                                                   len(self.dryers))
# # #
# # #     @classmethod
# # #     def get_room_to_readable_url_map(cls, url=None):
# # #         if url is None:
# # #             url = cls.HOUSING_PAGE
# # #         res = requests.get(cls.HOUSING_PAGE)
# # #         soup = BeautifulSoup(res.text, "html.parser")
# # #         html_links = soup.select(".content-area li > a")
# # #         links = dict()
# # #         for hl in html_links:
# # #             links[hl.string] = hl["href"]
# # #         return links
# # #
# # #     @classmethod
# # #     def get_room_to_uuid_map(cls, readable_url_map=None):
# # #         if readable_url_map is None:
# # #             readable_url_map = cls.get_room_to_readable_url_map()
# # #         room_to_uuid = dict()
# # #         for room, readable_url in readable_url_map.items():
# # #             room_to_uuid[room] = cls.get_uuid_from_readable_url(readable_url)
# # #         return room_to_uuid
# # #
# # #     @classmethod
# # #     def get_uuid_from_readable_url(cls, readable_url):
# # #         res = requests.get(readable_url)
# # #         soup = BeautifulSoup(res.text, "html.parser")
# # #         iframe_src = soup.find('iframe')['src']
# # #         uuid = iframe_src[-36:]
# # #         return uuid
# # #
# # #     import transaksi as catat
# # #     import pelanggan as pelanggan
# # #     import jenislaundry as jenisLaundry
# # #     import programdb as programdb
# # #     from datetime import datetime as dt
# # #
# # #     #
# # #     # saat_ini = dt.now()
# # #     # tgl = saat_ini.strftime('%d-%m-%Y')  # format dd/mm/YY
# # #     # print('Tanggal:', saat_ini)
# # #     # print(type(saat_ini))
# # #     #
# # #     #
# # #     # tgl_text = '27-07-2005'
# # #     # print(tgl_text, type(tgl_text))  # tipe data str
# # #     # tgl_date = dt.strptime(tgl_text, '%d-%m-%Y')  # konversi string ke date dengan format tertentu
# # #     # print(tgl_date, type(tgl_date))
# # #     #
# # #     #
# # #     # coba1 = catat.Catat("1", 2, 2, 2, 5)
# # #     #
# # #     # cetak = coba1.hargatotal()
# # #     # print(coba1.hargatotal())
# # #
# # #     # print("""\t Laundry.in
# # #     # --------------------------------
# # #     # 1. Catat transaksi
# # #     # 2. Lihat riwayat transaksi
# # #     # 3. Cetak nota
# # #     # 4. Jenis laundry
# # #     # 5. Rekap data
# # #     # """)
# # #
# # #     print("""\t 1. Catat transaksi
# # #     --------------------------------
# # #     """)
# # #     nama = input("Nama : ")
# # #     nohp = input("Nomor HP : ")
# # #     email = input("Email : ")
# # #
# # #     pelanggan = pelanggan.Pelanggan(nama, nohp, email)
# # #     programdb.insertpelanggan(pelanggan.getnama, pelanggan.getnohp, pelanggan.getemail)
# # #
# # #     # tglselesai = input("Tanggal Selesai : ")
# # #     # jumlahpakaian = input("Jumlah Pakaian : ")
# # #     # tglterima = dt.now()
# # #     # tglselesai = dt.strptime(tglselesai, '%d-%m-%Y')
# # #
# # #     # print("""\t 2. Lihat riwayat transaksi
# # #     # --------------------------------
# # #     # 1. Mingguan
# # #     # 2. Bulanan
# # #     # 3. Tahunan
# # #     # """)
# # #
# # #     # print("""\t 4. Jenis Laundry
# # #     # --------------------------------
# # #     # 1. Lihat jenis
# # #     # 2. Tambahkan jenis
# # #     # 3. Hapus jenis
# # #     # """)
# # #     #
# # #     # jenis = input("pilihan : ")
# # #     # if jenis == '1':
# # #     #     programdb.viewjenis()
# # #     # elif jenis == '2':
# # #     #     askid = input("ID Jenis : ")
# # #     #     askjenis = input("Jenis : ")
# # #     #     askhargajenis = input("Harga Jenis : ")
# # #     #     injenis = jenisLaundry.Tipe(askid, askjenis, askhargajenis)
# # #     #     programdb.insertjenis(injenis.getidjenis, injenis.getjenis, injenis.gethargajenis)
# # #     # else:
# # #     #     ask = input("ID Jenis laundry : ")
# # #     #     askid = jenisLaundry.Tipe(ask, "", "")
# # #     #     programdb.deletejenis(askid.getidjenis)
# # #
# # #     programdb.conn.close()
# # #
# # #
