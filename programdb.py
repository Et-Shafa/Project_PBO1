import sqlite3
import transaksi as catat
import jenislaundry as jenislaundry

db = "laundryin.db"

# * connect ke database
conn = sqlite3.connect(db)


def insertjenis():
    askid = input("ID Jenis : ")
    askjenis = input("Jenis : ")
    askhargajenis = input("Harga Jenis : ")
    injenis = jenislaundry.Tipe(askid, askjenis, askhargajenis)
    res = conn.execute(
        "select * from jeniscuci where idjeniscuci = ? or jenis = ?", (injenis.getidjenis, injenis.getjenis))
    if res.fetchone() is None:
        conn.execute("insert into jeniscuci values (?,?,?)",
                     (injenis.getidjenis, injenis.getjenis, injenis.gethargajenis))
    conn.commit()


# def updatejenis(): xxxxxxxxx
#     inama = input("Nama data barang yang ingin di update : ")
#     iharga = int(input("Harga baru : "))
#     # barang1 = item.Barang(inama, iharga)
#     conn.execute(
#         "UPDATE jeniscuci set harga = ?  WHERE nama_barang = ?", (iharga, inama))
#     conn.commit()


def deletejenis():
    ask = input("ID Jenis laundry : ")
    # dltjenis = jenislaundry.Tipe()
    conn.execute("DELETE FROM jeniscuci WHERE idjeniscuci = ?",
                 (ask, ))
    conn.commit()

def viewjenis():
    cursor = conn.cursor().execute("select * from jeniscuci")
    for row in cursor:
        print(f'{row[0]} | {row[1]} | {row[2]}')


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
# updatejenis() xxxxxxx
# deletejenis()
# viewjenis()
# conn.close()
