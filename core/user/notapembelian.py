import json
import os.path
from core.admin.simpanData import simpanData

def cetak(isi):
    loop=True
    i=1
    while True:
        nama="nota"+str(i)
        if os.path.exists(nama+".txt"):
            i=i+1
        else:
            with open(nama+".txt", 'w') as file:
                json.dump(isi, file)
                print("Nota berhasil disimpan, tekan enter untuk melanjutkan")
                input()
                break