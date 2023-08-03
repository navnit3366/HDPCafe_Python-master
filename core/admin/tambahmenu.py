# Logic Tambah Menu kedalam list "L"

def tambahMenu(L):
    loop = True
    while loop:
        i=1
        x = len(L)
        print("Masukkan nama menu", end=": ")
        nama = input()
        print("Masukkan harga menu", end=": ")
        harga = int(input())
        print("Masukkan jenis menu (1:makanan, 2:minuman)", end=": ")
        jenis = int(input())
        L.sort()
        while i-1<x:
            if L[i-1][0]==i:
                i=i+1
            else:
                break
        L1 = [i,nama,harga,jenis]
        L.append(L1)
        L.sort()
        for a in L:
            print(a)
        loop2 = True
        while loop2:
            print("Apakah anda ingin menambahkan menu lagi?(Y/N)", end=": ")
            jawab=input()
            if jawab == "N" or jawab == "n":
                loop=False
                break
            elif jawab == "Y" or jawab == "y":
                break
            else:
                print("Input salah")
                input()
    return L