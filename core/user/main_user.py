# Tampilan Awal User

from core.user.layout_makanan import makanan
from core.user.layout_minuman import minuman
from core.user.layout_checkout import checkout
from core.user.layout_keranjang import keranjang

def main_user():
    print("Selamat Datang Di HDP Mart, Selamat Berbelanja!")
    print()
    La = []
    total=0
    loop = True
    while loop:
        print("==================================")
        print("1. Aneka Minuman")
        print("2. Aneka Makanan")
        print("3. Lihat Cart")
        print("4. Checkout")
        print("5. Kembali ke menu Utama")
        print("==================================")
        print()

        try:
            pilih = int(input("Masukan Pilihan = "))
        except ValueError:
            pilih=0
        if pilih == 1 :
            La, total=minuman(La, total)
        elif pilih == 2 :
            La, total=makanan(La, total)
        elif pilih == 3:
            if La==[]:
                print("Anda belum memesan menu apapun")
                input()
            else:
                La, total=keranjang(La, total)
        elif pilih == 4 :
            if La==[]:
                print("Anda belum memesan apapun")
                input()
            else:
                La, total = checkout(La, total)
        elif pilih == 5 :
            La=[]
            total=0
            break
        else:
            print("Menu tidak ditemukan")
            input()