import transaksi as catat
import pelanggan
import jenislaundry as jenisLaundry
import programdb as programdb
from datetime import datetime as dt

Start = True

while Start:
    print("""\t Laundry.in
--------------------------------
1. Catat transaksi
2. Lihat riwayat transaksi
3. Cetak nota
4. Jenis laundry
5. Rekap data
6. Selesai
""")
    ask = input("Pilihan : ")
    if ask == "1":
        startone = True
        while startone:
            print("""\t 1. Catat transaksi
--------------------------------
1. Tambah pelanggan
2. Lihat pelanggan
3. Transaksi
4. Menu utama
""")
            pilih = input("Pilihan: ")
            if pilih == "1":
                nama = input("Nama : ")
                nohp = input("Nomor HP : ")
                email = input("Email : ")
                pelanggan = pelanggan.Pelanggan(nama, nohp, email)
                programdb.insertpelanggan(pelanggan.getnama, pelanggan.getnohp, pelanggan.getemail)
            elif pilih == "2":
                programdb.viewpelanggan()
            elif pilih == "3":
                idpelanggan = input("ID Pelanggan : ")
                tglterima = dt.now()
                tglselesai = input("Tanggal Selesai : ")
                tglselesai = dt.strptime(tglselesai, '%d-%m-%Y')
                totalpakaian = input("Total pakaian : ")
                tambah = True
                while tambah:
                    programdb.viewjenis()
                    idjenis = input("ID Jenis : ")
                    jumlahberat = int(input("Jumlah berat : "))
                    hargajenis = int(programdb.gethargajenis(idjenis))
                    totalhargajenis = catat.Catat.totalhargajenis(1, jumlahberat, hargajenis)
                    print(totalhargajenis)
                    print(""""
Tambah ?
\t 1. Ya
\t 2. Tidak""")
                    tran = catat.Catat(tglselesai, totalpakaian)
                    programdb.inserttra(idpelanggan, tglterima, tran.gettglselesai, tran.getjumlahpakaian, idjenis,
                                        jumlahberat, totalhargajenis)
                    pilihan = input("Pilihan : ")
                    if pilihan == "1":
                        pass
                    else:
                        tambah = False
            elif pilih == "4":
                startone = False
            else:
                pass

    elif ask == "2":
        pass

    elif ask == "3":
        pass

    elif ask == "4":
        print("""\t 4. Jenis Laundry
        --------------------------------
        1. Lihat jenis
        2. Tambahkan jenis
        3. Hapus jenis
        """)

        jenis = input("pilihan : ")
        if jenis == '1':
            programdb.viewjenis()
        elif jenis == '2':
            askid = input("ID Jenis : ")
            askjenis = input("Jenis : ")
            askhargajenis = input("Harga Jenis : ")
            injenis = jenisLaundry.Tipe(askid, askjenis, askhargajenis)
            programdb.insertjenis(injenis.getidjenis, injenis.getjenis, injenis.gethargajenis)
        else:
            ask = input("ID Jenis laundry : ")
            askid = jenisLaundry.Tipe(ask, "", "")
            programdb.deletejenis(askid.getidjenis)

    elif ask == "5":
            pass

    elif ask == "6":
        Start = False

    else:
        pass


# # print(tglselesai)
# # print(type(tglselesai))
# totalpakaian = input("Jumlah Pakaian : ")
# jumlahberatjenis = input("Jumlah berat : ")


# print("""\t 2. Lihat riwayat transaksi
# --------------------------------
# 1. Mingguan
# 2. Bulanan
# 3. Tahunan
# """)





programdb.conn.close()

