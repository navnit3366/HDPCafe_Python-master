# Tampilan Awal Admin

import os.path

from core.admin.updatemenu import updateMenu
from core.admin.hapusmenu import hapusMenu
from core.admin.carimenu import cariMenu
from core.admin.lihatmenu import lihatMenu
from core.admin.simpanData import simpanData
from core.admin.tambahmenu import tambahMenu


def main_admin():
    loop = True
    while loop:
        print()
        print("Selamat Datang Di HDP's Cafe")
        print()
        print("==================================")
        print("1. Tambah Menu")
        print("2. Update Menu")
        print("3. Hapus Menu")
        print("4. Cari Menu")
        print("5. Lihat Menu")
        print("6. Kembali ke Menu Utama")
        print("==================================")
        print()
        pilih = int(input("Masukan Pilihan = "))

        if os.path.exists("menu.txt"):
            L=lihatMenu("menu.txt")
            if pilih == 1:
                L1=tambahMenu(L)
                simpanData(L1, 'menu.txt')
            elif pilih == 2:
                L1=updateMenu(L)
                simpanData(L1, 'menu.txt')
            elif pilih == 3:
                L1=hapusMenu(L)
                simpanData(L1, 'menu.txt')
            elif pilih == 4:
                cariMenu(L)
            elif pilih == 5:
                for x in L:
                    print(x)
                input()
            elif pilih == 6:
                break
            else:
                print("Menu tidak ditemukan")
                input()
        else:
            L=[]
            if pilih == 1:
                L1=tambahMenu(L)
                simpanData(L1)
            elif pilih == 7:
                break
            elif pilih == 2 or pilih == 3 or pilih == 4 or pilih == 5 or pilih == 6:
                print("File 'menu' belum ada, buat terlebih dahulu")
                input()
            else:
                print("Menu tidak ditemukan")
                input()
    return pilih
