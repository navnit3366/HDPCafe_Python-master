# Menyimpan data bersadarkan parameter 'L' sebagai list dan 'nama' sebagai nama file

import json
def simpanData(L, nama):
    with open(nama, 'w') as file:
        json.dump(L, file)
        print("Data berhasil disimpan, tekan enter untuk melanjutkan")
        input()