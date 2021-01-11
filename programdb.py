import sqlite3

db = "laundryin.db"

# * connect ke database
conn = sqlite3.connect(db)


# * melihat daftar jenis laundry
def viewjenis():
    cursor = conn.cursor().execute("select * from jeniscuci")
    for row in cursor:
        print(f'{row[0]} | {row[1]} | {row[2]}')


# * memasukkan data jenis laundry
def insertjenis(idinsr, jenis, harga):
    res = conn.execute(
        "select * from jeniscuci where idjeniscuci = ? or jenis = ?", (idinsr, jenis))
    if res.fetchone() is None:
        conn.execute("insert into jeniscuci values (?,?,?)",
                     (idinsr, jenis, harga))
    conn.commit()


# * mengapus jenis laundry berdasarkan id
def deletejenis(iddlt):
    conn.execute("DELETE FROM jeniscuci WHERE idjeniscuci = ?", (iddlt, ))
    conn.commit()


# * memasukkan data pelanggan
def insertpelanggan(nama, nohp, email):
    res = conn.execute(
        "select * from pelanggan where nama = ?", (nama, ))
    if res.fetchone() is None:
        conn.execute("insert into pelanggan values (?, ?, ?, ?)",
                     (None, nama, nohp, email))
    conn.commit()


# *melihat data pelanggan
def viewpelanggan():
    cursor = conn.cursor().execute("select * from pelanggan")
    for row in cursor:
        print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')


# * mengambil data pelanggan pada index tertentu
def getdatapelanggan(idpelanggan, index):
    cursor = conn.cursor().execute(
        "select * from pelanggan where idpelanggan = ?", (idpelanggan, ))
    for row in cursor:
        return (f'{row[index]}')


# * mengambil data harga jenis pada index tertentu
def gethargajenis(idjenis):
    cursor = conn.cursor().execute(
        "select * from jeniscuci where idjeniscuci = ?", (idjenis, ))
    for row in cursor:
        return (f'{row[2]}')


# * memasukkan data transaksi
def inserttra(idpelanggan, tglterima, tglselesai, totalpakaian, idjenis, jumlahberatjenis, totalhargajenis):
    conn.execute("insert into transaksi values (?, ?, ?, ?, ?, ?, ?, ?, ?)", (None, idpelanggan,
                                                                              tglterima, tglselesai, totalpakaian, idjenis, jumlahberatjenis, totalhargajenis))
    conn.commit()


# * melihat data transaksi dalam jangka waktu tertentu
def gettransaksi(tanggalawal, tanggalakhir):
    cursor = conn.cursor().execute(
        "select * from transaksi where tglterima >= ? and tglterima <= ?", (tanggalawal, tanggalakhir))
    for row in cursor:
        print(f'''{row[0]} | {row[1]} | {row[2]}''')


# * melihat total pemasukan dalam jangka tertentu
def rekaptransaksi(tanggalawal, tanggalakhir):
    cursor = conn.cursor().execute(
        "select * from transaksi where tglterima >= ? and tglterima <= ?", (tanggalawal, tanggalakhir))
    total = 0
    for row in cursor:
        total += int(row[7])
    return total


# conn.close()
