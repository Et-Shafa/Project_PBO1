import transaksi as catat
import pelanggan
import jenislaundry as jenisLaundry
import programdb as programdb
from datetime import datetime as dt


#
# saat_ini = dt.now()
# tgl = saat_ini.strftime('%d-%m-%Y')  # format dd/mm/YY
# print('Tanggal:', saat_ini)
# print(type(saat_ini))
#
#
# tgl_text = '27-07-2005'
# print(tgl_text, type(tgl_text))  # tipe data str
# tgl_date = dt.strptime(tgl_text, '%d-%m-%Y')  # konversi string ke date dengan format tertentu
# print(tgl_date, type(tgl_date))
#
#
# coba1 = catat.Catat("1", 2, 2, 2, 5)
#
# cetak = coba1.hargatotal()
# print(coba1.hargatotal())

# print("""\t Laundry.in
# --------------------------------
# 1. Catat transaksi
# 2. Lihat riwayat transaksi
# 3. Cetak nota
# 4. Jenis laundry
# 5. Rekap data
# """)

print("""\t 1. Catat transaksi
--------------------------------
""")
# nama = input("Nama : ")
# nohp = input("Nomor HP : ")
# email = input("Email : ")
#
# pelanggan = pelanggan.Pelanggan(nama, nohp, email)
# programdb.insertpelanggan(pelanggan.getnama, pelanggan.getnohp, pelanggan.getemail)

# tglterima = dt.now()
# tglselesai = input("Tanggal Selesai : ")
# jumlahpakaian = input("Jumlah Pakaian : ")
# tglselesai = dt.strptime(tglselesai, '%d-%m-%Y')

# print("""\t 2. Lihat riwayat transaksi
# --------------------------------
# 1. Mingguan
# 2. Bulanan
# 3. Tahunan
# """)

# print("""\t 4. Jenis Laundry
# --------------------------------
# 1. Lihat jenis
# 2. Tambahkan jenis
# 3. Hapus jenis
# """)
#
# jenis = input("pilihan : ")
# if jenis == '1':
#     programdb.viewjenis()
# elif jenis == '2':
#     askid = input("ID Jenis : ")
#     askjenis = input("Jenis : ")
#     askhargajenis = input("Harga Jenis : ")
#     injenis = jenisLaundry.Tipe(askid, askjenis, askhargajenis)
#     programdb.insertjenis(injenis.getidjenis, injenis.getjenis, injenis.gethargajenis)
# else:
#     ask = input("ID Jenis laundry : ")
#     askid = jenisLaundry.Tipe(ask, "", "")
#     programdb.deletejenis(askid.getidjenis)



programdb.conn.close()

