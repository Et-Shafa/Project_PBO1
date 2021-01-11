from abc import ABC, abstractmethod
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


print("""
Pembayaran
    1. Lunas
    2. Belum bayar""")
bayar = input("Pilihan = ")


# print(pay(bayar))


print("""lalalsl : {}""".format(pay(bayar)))

# tran = catat.Catat(tglselesai, totalpakaian, statusbayar)
