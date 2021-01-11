import transaksi as catat
import pelanggan as pelanggan
import jenislaundry as jenisLaundry
import programdb as programdb
from datetime import datetime as dt

 def pay(bayar):
    if bayar == "1":
        return 'Lunas'
    elif bayar == "2":
        return 'Belum bayar'
    else:
        return 'inputan kurang tepat'
Start = True

while Start:
    print("""
--------------------------------------------------
                    Laundry.in
--------------------------------------------------
1. Catat transaksi
2. Jenis laundry
3. Riwayat Transaksi
4. Rekap
5. Selesai """)
    ask = input("Pilihan : ")
    if ask == "1":
        startone = True
        while startone:
            print("""
--------------------------------------------------
        Laundry.in/ 1. Catat transaksi
--------------------------------------------------
1. Tambah pelanggan
2. Lihat pelanggan
3. Transaksi
4. Menu utama
5. Selesai """)
            pilih = input("Pilihan: ")
            if pilih == "1":
                print("""
--------------------------------------------------
 Laundry.in/1. Catat transaksi/1. Tambah pelanggan
--------------------------------------------------""")
                nama = input("Nama : ")
                nohp = input("Nomor HP : ")
                email = input("Email : ")
                pelanggan = pelanggan.Pelanggan(nama, nohp, email)
                programdb.insertpelanggan(
                    pelanggan.getnama, pelanggan.getnohp, pelanggan.getemail)
            elif pilih == "2":
                print("""
--------------------------------------------------
 Laundry.in/1. Catat transaksi/2. Lihat pelanggan
--------------------------------------------------""")
                programdb.viewpelanggan()
            elif pilih == "3":
                print("""
--------------------------------------------------
    Laundry.in/1. Catat transaksi/3. Transaksi
--------------------------------------------------""")
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
                    print("------------------------------")
                    programdb.viewjenis()
                    print("------------------------------")
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
                    print("""
Tambah ?
    1. Ya
    2. Tidak""")
                    tran = catat.Catat(tglselesai, totalpakaian)
                    programdb.inserttra(idpelanggan, tglterima, tran.gettglselesai, tran.getjumlahpakaian, idjenis,
                                        jumlahberat, totalhargajenis)
                    pilihan = input("Pilihan : ")
                    if pilihan == "1":
                        pass
                    else:
                        tambah = False
                        print(totalHarga)
                       


selesai = True
while selesai:
    print("""
Pembayaran
    1. Lunas
    2. Belum bayar""")
    bayar = input("Pilihan = ")
    print(pay(bayar))
                print(""""
            NOTA || Laundry.in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nama                : {}
Nomor Hp            : {}
Email               : {}
Tanggal diterima    : {}
Tanggal selesai     : {}
Total pakaian       : {}
Jenis               Harga jenis         Total berat         Total Harga jenis
{}                  {}                  {}                  {}
Total harga         : Rp{}
status pembayaran   : {}
            """.format(programdb.getdatapelanggan(idpelanggan, 1), programdb.getdatapelanggan(idpelanggan, 2), programdb.getdatapelanggan(idpelanggan, 3), tglterima, tglselesai, totalpakaian, arrjenis, arrhargajenis, arrjumlahberatj, arrtotalhj, totalHarga))
            elif pilih == "4":
                startone = False
            elif pilih == "5":
                startone = False
                Start = False
            else:
                pass

    elif ask == "2":
        starttwo = True
        while starttwo:
            print("""
--------------------------------------------------
          Laundry.in/ 2. Jenis Laundry
--------------------------------------------------
1. Lihat jenis
2. Tambahkan jenis
3. Hapus jenis
4. Menu utama
5. Selesai """)
            jenis = input("pilihan : ")
            if jenis == '1':
                print("""
--------------------------------------------------
    Laundry.in/2. Jenis Laundry/1. Lihat jenis
--------------------------------------------------""")
                programdb.viewjenis()
            elif jenis == '2':
                print("""
--------------------------------------------------
Laundry.in/2. Jenis Laundry/2. Tambahkan jenis
--------------------------------------------------""")
                askid = input("ID Jenis : ")
                askjenis = input("Jenis : ")
                askhargajenis = input("Harga Jenis : ")
                injenis = jenisLaundry.Tipe(askid, askjenis, askhargajenis)
                programdb.insertjenis(injenis.getidjenis,
                                      injenis.getjenis, injenis.gethargajenis)
            elif jenis == '3':
                print("""
--------------------------------------------------
    Laundry.in/2. Jenis Laundry/3. Hapus jenis
--------------------------------------------------""")
                ask = input("ID Jenis laundry : ")
                askid = jenisLaundry.Tipe(ask, "", "")
                programdb.deletejenis(askid.getidjenis)
            elif jenis == '4':
                starttwo = False
            elif pilih == "5":
                startone = False
                Start = False
            else:
                pass

    elif ask == "3":
        print("""
--------------------------------------------------
        Laundry.in/ 3. Riwayat Transaksi
--------------------------------------------------""")
        print("format inputan : yy-mm-dd || Contoh inputan : 2021-01-01")
        awal = input("Dari : ")
        akhir = input("Sampai : ")
        programdb.gettransaksi(awal, akhir)

    elif ask == "4":
        print("""
--------------------------------------------------
              Laundry.in/ 4. Rekap
--------------------------------------------------""")
        print("format inputan : yy-mm-dd || Contoh inputan : 2021-01-01")
        awal = input("Dari : ")
        akhir = input("Sampai : ")
        programdb.rekaptransaksi(awal, akhir)

    elif ask == "5":
        Start = False

    else:
        pass


programdb.conn.close()
