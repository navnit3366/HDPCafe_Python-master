# Membuat Authentikasi

# untuk ini buat jalaninnya harus pake CMD gabisa pake pycharm, soalnya di pycharm masih ada bugnya masalah getPass!

import getpass
import os
#import header
import json
import os.path

from core.admin.main_admin import main_admin

def auth():
    print("=============================")
    print("Selamat Datang di HDP's Cafe!")
    print("=============================")
    print()
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'user.txt')
    conn=open(filename, "r")
    acc=json.load(conn)
    z = False
    a = 0
    while not z :
        user = input('Username = ')
        #pwd = getpass.getpass('Password = ') Biar bisa jalan di pycharm
        pwd = input('Password = ')
        for x in acc:
            if (user == x[0]) and (pwd == x[1]):
                print ('Selamat Datang',user,'Tekan Enter untuk lanjut')
                input()
                main_admin()
                z = True
                break
        if not z:
            print('Username/Password Salah')
            a = a+1
        if a == 3 :
            print ('sudah 3x salah')
            input()
            print("\n")
            break
    conn.close()
    os.system('cls')
    #header.header()