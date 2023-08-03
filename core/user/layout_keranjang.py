def keranjang(La, total):
    loop = True
    while loop:
        total=0
        for x in La:
            print(str(x[0])+".",x[1],x[2])
            total=total+x[2]
        print("Total harga :", total)
        print()
        print("1. Hapus menu yang dipesan")
        print("2. Kembali")
        print("Pilih menu", end=": ")
        try:
            pilih=int(input())
        except ValueError:
            pilih=0
        if pilih == 1:
            print("Pilih id menu yang ingin dihapus(1 menu setiap penghapusan)", end=": ")
            try:
                hapus=int(input())
            except ValueError:
                hapus=0
            for i, x in enumerate(La):
                if x[0]==hapus:
                    hps=La.pop(i)
                    break
                else:
                    if i+1==len(La):
                        print("Menu tidak ditemukan")
        elif pilih==2:
            break
    return La, total
#tes