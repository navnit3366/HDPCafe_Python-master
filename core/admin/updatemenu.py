# Logic Update Menu.

def updateMenu(L):
    n=len(L)
    for x in L:
        print(x)
    loop=True
    while loop:
        i=1
        print("Pilih id menu yang ingin diubah", end=": ")
        id = int(input())
        while i <= (n-1) and L[i][0] != id:
            i = i+1
        if L[i][0]==id:
            print("Masukkan data perubahan")
            print("Nama menu", end=": ")
            nama=input()
            print("Harga menu", end=": ")
            harga=int(input())
            print("Jenis menu(1: Makanan, 2: Minuman)", end=": ")
            jenis=int(input())
            L[i]=[id,nama,harga,jenis]
            for x in L:
                print(x)
        else:
            print("Menu dengan id", id,"tidak ditemukan")
            input()
        loop2=True
        while loop2:
            print("Apakah anda ingin mengubah menu dengan id lain?(Y/N)", end=": ")
            jawab=input()
            if jawab=="Y" or jawab=="y":
                break
            elif jawab=="N" or jawab=="n":
                loop=False
                break
            else:
                print("Input salah")
                input()
    return L