# import programdb as prog
# import transaksi as transaksi
# # idjenis = input("ID Jenis : ")
# # jumlahberat = input("Jumlah berat : ")
# hargajenis = int(prog.gethargajenis("jenis02"))
# print(type(hargajenis))
# totalhargajenis = transaksi.Catat.totalhargajenis(1, 2, hargajenis)
# print(totalhargajenis)
from datetime import datetime as dt

tglselesai = input("Sampai : ")
tglselesai = dt.strptime(tglselesai, '%Y-%m-%d')
print(type(tglselesai))


# # class Jenis:
# #
# #     def main(self, ask):
# #         bagi = ask.split(',')
# #         total = 0
# #         for n in bagi:
# #             if n == "1":
# #                 total = total + self.cucikering()
# #             elif n == "2":
# #                 total = total + self.setrika()
# #             elif n == "3":
# #                 total = total + self.cucisetrika()
# #         print(total)
# #
# #     def cucikering(self):
# #         print("Cuci Kering = 6000")
# #         return 6000
# #
# #     def setrika(self):
# #         print("setrika = 5000")
# #         return 5000
# #
# #     def cucisetrika(self):
# #         print("Cuci Setrika = 7000")
# #         return 7000
# #
# #
# # print("""
# #            Jenis Cuci
# # ---------------------------------
# # 1. Cuci Kering
# # 2. Setrika
# # 3. Cuci Setrika
# # """)
# # Jenis().main(input("Pilihan : "))
