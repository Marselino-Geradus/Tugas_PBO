import math

class Volume:
    def __init__(self):
        self.sisi = 0
        self.panjang = 0 
        self.lebar = 0
        self.tinggi = 0
        self.jari_jari = 0

    def balok(self):
        print("Volume Balok:", self.panjang * self.lebar * self.tinggi)

    def kubus(self):
        print("Volume Kubus:", self.sisi**3)

    def tabung(self):
        print("Volume Tabung:", math.pi * (self.jari_jari ** 2) * self.tinggi)
        

class Luas:
    def __init__(self):
        self.sisi = 0
        self.panjang = 0 
        self.lebar = 0
        self.tinggi = 0
        self.jari_jari = 0

    def balok(self):
        print("Luas Balok:", 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi))

    def kubus(self):
        print("Luas Kubus:", 6 * (self.sisi**2))

    def tabung(self):
        print("Luas Tabung:", 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi))

def ulang():
    print("Ingin menghitung lagi? (y/n)")
    inp = input("=> ").lower()
    return True if inp == "y" else False

volume = Volume()
luas = Luas()
 


while True:
    print('~'*30)
    print("Nama : Marselino Geradus")
    print("Kelas : Informatika_G")
    print('~'*30)
    print()

    print('='*30)
    print("Pilih menu: ")
    print("""
1. Volume
2. Luas""")
    pilih = input("~ Pilih: ")
    while pilih == '1' or pilih == '2':
        if pilih == '1':
            print()
            print("""
1. Balok
2. Tabung
3. Kubus
4. Tekan ENTER untuk kembali""")
            
            print()
            pilih2 = input("~ Pilih: ")
            if pilih2 == '1':
                while True:
                    p = float(input("Masukkan Panjang: "))
                    l = float(input("Masukkan Lebar: "))
                    t = float(input("Masukkan Tinggi: "))
                    volume.panjang = p
                    volume.lebar = l
                    volume.tinggi = t
                    print()
                    volume.balok()

                    if ulang() != True:
                        break
            elif pilih2 == '2':
                while True:
                    j = float(input("Masukkan Jari-jari: "))
                    t = float(input("Masukkan Tinggi: "))
                    volume.jari_jari = j 
                    volume.tinggi = t
                    print()
                    volume.tabung()

                    if ulang() != True:
                        break
            elif pilih2 == '3':
                while True:
                    s = float(input("Masukkan Sisi: "))
                    volume.sisi = s
                    print()
                    volume.kubus()

                    if ulang() != True:
                        break
            elif pilih2 == '4':
                break
            else:
                print("Masukan Anda salah! Mohon pilih ulang!")
                break
            
        if pilih == '2':
            print()
            print("""
1. Balok
2. Tabung
3. Kubus
4. Keluar""")
            pilih2 = int(input("~ Pilih: "))
                  
            if pilih2 == 1:
                while True:
                    p = float(input("Masukkan Panjang: "))
                    l = float(input("Masukkan Lebar: "))
                    t = float(input("Masukkan Tinggi: "))
                    luas.panjang = p
                    luas.lebar = l
                    luas.tinggi = t
                    print()
                    luas.balok()

                    if ulang() != True:
                        break
            elif pilih2 == 2:
                while True:
                    j = float(input("Masukkan Jari-jari: "))
                    t = float(input("Masukkan Tinggi: "))
                    luas.jari_jari = j 
                    luas.tinggi = t
                    print()
                    luas.tabung()

                    if ulang() != True:
                        break
            elif pilih2 == 3:
                while True:
                    s = float(input("Masukkan Sisi: "))
                    luas.sisi = s
                    print()
                    luas.kubus()

                    if ulang() != True:
                        break
            elif pilih2 == 4:
                break
            else:
                print("Masukkan Anda salah!")
    else:
        break
        print("Inputan Anda salah! Mohon mulai ulang.")