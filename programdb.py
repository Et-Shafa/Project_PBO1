import sqlite3
import transaksi as catat
import jenislaundry as jenislaundry

db = "laundryin.db"

# * connect ke database
conn = sqlite3.connect(db)


def viewjenis():
    cursor = conn.cursor().execute("select * from jeniscuci")
    for row in cursor:
        print(f'{row[0]} | {row[1]} | {row[2]}')


def insertjenis(idinsr, jenis, harga):
    res = conn.execute(
        "select * from jeniscuci where idjeniscuci = ? or jenis = ?", (idinsr, jenis))
    if res.fetchone() is None:
        conn.execute("insert into jeniscuci values (?,?,?)", (idinsr, jenis, harga))
    conn.commit()


def deletejenis(iddlt):
    conn.execute("DELETE FROM jeniscuci WHERE idjeniscuci = ?", (iddlt, ))
    conn.commit()

def insertpelanggan(nama, nohp, email):
    res = conn.execute(
        "select * from pelanggan where nama = ?", (nama, ))
    if res.fetchone() is None:
        conn.execute("insert into pelanggan values (? , ?, ?, ?)", (None, nama, nohp, email))
    conn.commit()

def inserttra(idpelanggan, tglterima, tglselesai, idjenis, jumlahberatjenis, totalhargajenis, totalpakaian, totalharga):
    res = conn.execute(
        "select * from transaksi where idjeniscuci = ? or jenis = ?", (id, jenis))
    if res.fetchone() is None:
        conn.execute("insert into transaksi values (?, ?, ?,?,?,?,?,?,?,?,?)", ("", nama, nohp, email, tglterima, tglselesai, idjenis, jumlahberatjenis, totalhargajenis, totalpakaian, totalharga))
    conn.commit()

# def updatejenis(): xxxxxxxxx
#     inama = input("Nama data barang yang ingin di update : ")
#     iharga = int(input("Harga baru : "))
#     # barang1 = item.Barang(inama, iharga)
#     conn.execute(
#         "UPDATE jeniscuci set harga = ?  WHERE nama_barang = ?", (iharga, inama))
#     conn.commit()

# def read():
#     cursor = conn.cursor().execute("select * from barang")
#     for row in cursor:
#         print(f'{row[0]}, {row[1]}, {row[2]}')


# def readByName():
#     asknama = input("Cari data berdasar nama : ")
#     cursor = conn.cursor().execute(
#         "select * from barang where nama_barang = ?", (asknama, ))
#     for row in cursor:
#         print(f'{row[0]}, {row[1]}, {row[2]}')

# conn.execute("insert into jeniscuci values (?,?,?)",
#              ("jenis04", "coba", 2000))
# conn.commit()

# insertjenis()
# deletejenis()
# viewjenis()
# conn.close()
