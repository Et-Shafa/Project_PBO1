import transaksi as catat
import pelanggan as pelanggan
import jenislaundry as jenisLaundry
import programdb as programdb
from datetime import datetime as dt

Start = True

while Start:
    print("""
\t Laundry.in
--------------------------------
1. Catat transaksi
2. Jenis laundry
3. Riwayat Transaksi
4. Rekap
5. Selesai
""")
    ask = input("Pilihan : ")
    if ask == "1":
        startone = True
        while startone:
            print("""
    \t 1. Catat transaksi
    --------------------------------
    1. Tambah pelanggan
    2. Lihat pelanggan
    3. Transaksi
    4. Menu utama
    5. Selesai
    """)
            pilih = input("Pilihan: ")
            if pilih == "1":
                nama = input("Nama : ")
                nohp = input("Nomor HP : ")
                email = input("Email : ")
                pelanggan = pelanggan.Pelanggan(nama, nohp, email)
                programdb.insertpelanggan(
                    pelanggan.getnama, pelanggan.getnohp, pelanggan.getemail)
            elif pilih == "2":
                programdb.viewpelanggan()
            elif pilih == "3":
                idpelanggan = input("ID Pelanggan : ")
                tglterima = dt.now()
                tglselesai = input("Tanggal Selesai : ")
                tglselesai = dt.strptime(tglselesai, '%d-%m-%Y')
                totalpakaian = input("Total pakaian : ")
                tambah = True
                totalHarga = 0
                arrjenis = []
                arrhargajenis = []
                arrjumlahberatj = []
                arrtotalhj = []
                while tambah:
                    print("\n")
                    programdb.viewjenis()
                    idjenis = input("ID Jenis : ")
                    jumlahberat = float(input("Jumlah berat : "))
                    hargajenis = float(programdb.gethargajenis(idjenis))
                    totalhargajenis = catat.Catat.totalhargajenis(
                        1, jumlahberat, hargajenis)
                    print("Total harga jenis :", totalhargajenis)
                    arrjenis.append(idjenis)
                    arrhargajenis.append(hargajenis)
                    arrjumlahberatj.append(jumlahberat)
                    arrtotalhj.append(totalhargajenis)
                    totalHarga = totalHarga + totalhargajenis
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
                """.format(programdb.getdatapelanggan(idpelanggan, 1), programdb.getdatapelanggan(idpelanggan, 2), programdb.getdatapelanggan(idpelanggan, 3), tglterima, tglselesai, totalpakaian, arrjenis, arrhargajenis, arrjumlahberatj, arrtotalhj, totalHarga))
            elif pilih == "4":
                startone = False
            else:
                pass

    elif ask == "2":
        starttwo = True
        while starttwo:
            print("""
    \t 2. Jenis Laundry
    --------------------------------
    1. Lihat jenis
    2. Tambahkan jenis
    3. Hapus jenis
    4. Menu utama
    5. Selesai
    """)

            jenis = input("pilihan : ")
            if jenis == '1':
                programdb.viewjenis()
            elif jenis == '2':
                askid = input("ID Jenis : ")
                askjenis = input("Jenis : ")
                askhargajenis = input("Harga Jenis : ")
                injenis = jenisLaundry.Tipe(askid, askjenis, askhargajenis)
                programdb.insertjenis(injenis.getidjenis,
                                      injenis.getjenis, injenis.gethargajenis)
            elif jenis == '3':
                ask = input("ID Jenis laundry : ")
                askid = jenisLaundry.Tipe(ask, "", "")
                programdb.deletejenis(askid.getidjenis)
            elif jenis == '4':
                starttwo = False
            else:
                pass

    elif ask == "3":
        print("format inputan : yy-mm-dd || Contoh inputan : 2021-01-01")
        awal = input("Dari : ")
        akhir = input("Sampai : ")
        # awal = dt.strptime(awal, '%Y-%m-%d')
        # akhir = dt.strptime(akhir, '%Y-%m-%d')
        programdb.gettransaksi(awal, akhir)
    #     startthree = True
    #     while startthree:
    #         print(
    #             """\t 3. Riwayat Transaksi
    # --------------------------------
    # 1. Harian
    # 2. Mingguan
    # 3. Bulanan
    # 4. Tahunan
    # 5. Menu utama
    # 6. Selesai
    # """)
    #         pilih = input("pilihan : ")
    #         if pilih == "1":
    #             pass
    #         elif pilih == "2":
    #             pass
    #         elif pilih == "3":
    #             pass
    #         elif pilih == "4":
    #             pass
    #         elif pilih == "5":
    #             startthree = False
    #         elif pilih == "6":
    #             startthree = False
    #             Start = False

    elif ask == "4":
        pass
        # print("format inputan : yy-mm-dd || Contoh inputan : 2021-01-01")
        # awal = input("Dari : ")
        # akhir = input("Sampai : ")
    #     startfour = True
    #     while startfour:
    #         print("""
    # \t 4. Riwayat Transaksi
    # --------------------------------
    # 1. Harian
    # 2. Mingguan
    # 3. Bulanan
    # 4. Tahunan
    # 5. Menu utama
    # 6. Selesai
    # """)
    #         pilih = input("pilihan : ")
    #         if pilih == "1":
    #             pass
    #         elif pilih == "2":
    #             pass
    #         elif pilih == "3":
    #             pass
    #         elif pilih == "4":
    #             pass
    #         elif pilih == "5":
    #             startfour = False
    #         elif pilih == "6":
    #             startfour = False
    #             Start = False

    elif ask == "5":
        Start = False
    else:
        pass


programdb.conn.close()
