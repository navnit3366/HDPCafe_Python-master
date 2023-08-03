# Logic untuk mencari Menu

def cari(L, n):
    print("Masukkan data menu yang dicari", end=": ")
    if n==1 or n==3:
        cari = int(input())
    else:
        cari=input()
    i = 0
    loop2 = True
    while i < len(L) and loop2:
        if L[i][n-1] == cari:
            print("Menu ditemukan")
            print(L[i])
            input()
            loop2 = False
        else:
            i = i + 1
    if loop2:
        print("Menu dengan data", cari, "tidak ditemukan")
        input()

def cariMenu(L):
    loop=True
    while loop:
        print("1. Cari berdasarkan ID")
        print("2. Cari berdasarkan nama menu")
        print("3. Cari berdasarkan harga")
        print("4. Kembali")
        print("Pilih menu (1-4)", end=": ")
        jawab=int(input())
        if jawab==1 or jawab==2 or jawab==3:
            cari(L, jawab)
        elif jawab==4:
            break
        else:
            print("Input salah")