# logic untuk layout makanan
from core.admin.lihatmenu import lihatMenu

def makanan(La, total):
    #total=0
    print()
    print("=============================")
    print("Daftar Menu Makanan :")
    print("=============================")
    print()
    L=lihatMenu("menu.txt")
    ada=False
    for x in L:
        if x[3]==1:
            print(str(x[0])+".", x[1])
            ada=True
        else:
            pass
    if ada:
        print()
        loop=True
        while loop:
            print("Silahkan Pilih Menu", end=": ")
            a=int(input())
            La.append(L[a-1])
            total=total+L[a-1][2]
            for z in La:
                print(z[1],z[2])
            print("Total harga =", total)
            loop2=True
            while loop2:
                try:
                    tambah=input("Apakah anda ingin memilih menu lagi(Y/N)?")
                except ValueError:
                    tambah=0
                if tambah=="N" or tambah=="n":
                    loop=False
                    break
                elif tambah=="Y" or tambah=="y":
                    break
                else:
                    print("Input Salah")
        print()
        input("Tekan enter untuk kembali")
    else:
        print("Menu makanan belum tersedia, tunggu sampai admin menambahkan menu makanan")
        input()
    return La, total
#tes