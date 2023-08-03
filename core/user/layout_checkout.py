# logic untuk layout checkout

import os.path
from core.user.notapembelian import cetak
from core.user.notapembelian_native import notanative

def checkout(La, total):
    print()
    print("========================")
    print("HDP's Cafe CHECKOUT")
    print("========================")
    print()
    print("Berikut adalah Total Pembayaran dari Pembelanjaan anda :")
    print()
    for x in La:
        print(str(x[1])+"---"+"Rp."+str(x[2]))
    print()
    print("==========================")
    print("Total Harga :", "Rp."+str(total))
    input()
    print("Lanjutkan Pembayaran? (1-2)")
    print()
    print("1. Ya")
    print("2. Batalkan")
    print()
    loop = True
    while loop:
        try:
            pilihCheckout = int(input("Masukan Pilihan = "))
        except ValueError:
            pilihCheckout = 0
        if pilihCheckout == 1 :
            lanjutPembayaran(La, total)
            La = []
            total = 0
            break
        elif pilihCheckout ==2 :
            print("Pesanan Anda dibatalkan, Tekan Enter untuk Kembali ke Menu.")
            La=[]
            total=0
            break
        else:
            print("Menu tidak ditemukan")
            input()
    return La, total

def lanjutPembayaran(La, total):
    print()
    print("==========================")
    print("Lanjut Pembayaran")
    print("==========================")
    print()
    print("Total Harga :", "Rp."+str(total))
    print()
    loop=True
    while loop:
        try:
            uangKonsumen = int(input("Silahkan Input Uang Anda, Untuk Membayar : "))
        except ValueError:
            uangKonsumen = 0
        if (uangKonsumen >= total):
            loop2=True
            loop=False
            while loop2:
                kembali = uangKonsumen-total
                print("Kembalian anda :", "Rp."+str(kembali))
                a, p, b = notanative(La, total, kembali, uangKonsumen)
                j = ""
                for z in p:
                    k = str(z[1]) + " " + str(z[2]) + " " + str(z[3])
                    j = j + k
                isi = str(a) + str(j) + str(b)
                print(isi)
                nota = input("Apakah anda ingin mencetak receipt? (Y/N) : ")
                if nota == "Y" or nota == "y" :
                    cetak(isi)
                    break
                elif nota == "N" or nota == "n":
                    print("Tidak Mencetak nota, Silahkan Tekan Enter untuk Kembali.")
                    break
                else:
                    print("Input Salah")
                    input()
        else :
            print("Uang Tidak Mencukupi atau Input Salah")
            input()
