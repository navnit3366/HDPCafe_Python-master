# Native Nota Menggunakan ASCII

#Pendukung untuk membuat Asci Art
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Asci Art, terlalu banyak font ASCI dan gw masih binggung font yang bagus apa..
init(strip=not sys.stdout.isatty())
cprint(figlet_format('HDP Cafe!', font='starwars'))

def notanative(La, total, kembali, uangKonsumen):
    p=[]
    i=1
    print()
    a=("--------------------------------------------------"
    "\n                     Nota Pembelian"
    "\n                        HDP CAFE"
    "\n                  Jalan Cafetaria No 6"
    "\n--------------------------------------------------\n"
    "\nDaftar Barang yang telah anda beli : \n")
    for x in La:
        pa=[i, x[1], "---", "Rp."+str(x[2])]
        p.append(pa)
    b=("\nTotal Belanja : "+"Rp."+str(total)+"\n"
    "\nUang yang diberikan : "+"Rp."+str(uangKonsumen)+"\n"
    "Kembalian : "+"Rp."+str(kembali)+"\n"
    "Terimakasih Sudah Datang Ke HDP Cafe!\n"
    "--------------------------------------------------")
    return a,p,b