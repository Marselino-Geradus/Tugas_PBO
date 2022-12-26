class Luas():
    def menu(namaBangun):
        print("="*50)
        print("=", f"Menghitung Luas {namaBangun}".center(46), "=")
        print("="*50)
        if namaBangun == "Persegi":
            sisi = float(input("~ Masukkan Panjang Sisi (cm) :"))
            Luas.persegi(sisi)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Persegi Panjang":
            Panjang = float(input("~ Masukkan Panjang Sisi (cm) :"))
            Lebar = float(input("~ Masukkan Lebar Sisi (cm) :"))
            Luas.persegiPanjang(Panjang, Lebar)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Segitiga":
            alas = float(input("~ Masukkan panjang Alas (cm) :")) 
            tinggi = float(input("~ Masukkan Tinggi (cm) :"))
            Luas.segitiga(alas, tinggi)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Lingkaran":
            r = float(input("~ Masukkan Jari - Jari Lingkaran (cm) : "))
            Luas.lingkaran(r)
            Luas.enter()
            Luas.start()
        else:
            Luas.start() 

    def persegi (input_sisi):
        luas = input_sisi * input_sisi
        print(">>> Luas Persegi adalah", luas, "Sentimeter Kuadrat")
    def persegiPanjang(Panjang, Lebar):
        luas = Panjang * Lebar
        print(">>> Luas Persegi Panjang adalah", luas, "Sentimeter Kuadrat")
    def lingkaran (r):
        luas = 22/7 * (r**2)
        print(">>> Luas Lingkaran adalah", luas, "Sentimeter Kuadrat")
    def segitiga (alas, tinggi):
        luas = 1/2 * alas * tinggi
        print(">>> Luas Segitiga adalah", luas , "Sentimeter Kuadrat")
    def enter():
        print()
        enter = input("~ Tekan ENTER untuk lanjut")


    def start():
        print("-"*50)
        print('=', ' Menghitung Luas Bangun Datar'.center(47), '=')
        print("-"*50)
        print('''
                1. Persegi
                2. Persegi Panjang
                3. Lingkaran
                4. Segitiga
                5. kembali ke Menu''')

        pilihan = input("~ Pilih Menu :")
        if pilihan == "1":
            Luas.menu("Persegi")
        elif pilihan == "2":
            Luas.menu("Persegi Panjang")
        elif pilihan == "3":
            Luas.menu("Lingkaran")
        elif pilihan == "4":
            Luas.menu("Segitiga")
        elif pilihan == "5":
            pass
        else:
            print("~ Perintah tidak ditemukan")
            Luas.enter()
            Luas.start()
        
class Volume():
    def start():
        print("="*50)
        print("=","Menghitung Volume Bangun Ruang".center(46),"=")
        print('-'*50)
        print('''
                1. Kubus
                2. Balok
                3. Tabung
                4. Kerucut
                5. Kembali ke Menu''')

        pilihan = input("~ Pilih menu : ")
        if pilihan == "1":
            Volume.menu("kubus")
        elif pilihan == "2":
            Volume.menu("balok")
        elif pilihan == "3":
            Volume.menu("tabung")
        elif pilihan == "4":
            Volume.menu("kerucut")
        elif pilihan == "5":
            pass
        else:
            print(">>> Perintah tidak ditemukan")
            Volume.enter()
            Volume.start()

    def kubus(sisi):
        volume = sisi **3
        print(">> Volume kubus adalah", volume , "Sentimeter Kubik")
    def balok(panjang, lebar, tinggi):
        volume = panjang * lebar * tinggi
        print(">> Volume balok adalah", volume , "Sentimeter Kubik")
    def tabung(phi, r, t): 
        volume = 22/7 * ((r**2) * t)
        print(">> Volume tabung adalah", volume, "Sentimeter Kubik")
    def kerucut(r, t):
        volume = 1/3 *(3.14 * (r**2) * t)
        print(">> Volume kerucut adalah", volume, "Sentimeter Kubik")
    def enter():
        enter = input(">> Tekan ENTER untuk lanjut")


    def menu(namaBangunRuang):
        print("="*50)
        print("=",f"Menghitung Volume {namaBangunRuang}".center(46),"=")
        print("="*50)
        if namaBangunRuang == "kubus":
            rusuk = float(input("~ Masukkan Panjang Rusuk (cm) :"))
            Volume.kubus(rusuk)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "balok":
            panjang = float(input("~ Masukkan Panjang Balok : "))
            lebar = float(input("~ Masukkan Lebar Balok : "))
            tinggi = float(input("~ Masukkan Tinggi Balok : "))
            Volume.balok(panjang, lebar, tinggi)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "kerucut":
            r = float(input("~ Masukkan Jari-Jari Alas (cm) :"))
            t = float(input("~ Masukkan Tinggi Kerucut (cm) :"))
            Volume.kerucut(r, t)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "tabung":
            r = float(input("~ Masukkan Jari - Jari (cm) :"))
            t = float(input("~ Masukkan Tinggi Tabung (cm) :"))
            Volume.tabung(r, t)
            Volume.enter()
            Volume.start()
        else:
            pass



while True:
    print("-"*50)
    print("~ Nama: Marselino Geradus")
    print("~ NIM : D0221364 ")
    print('~ Prodi : Teknik Informatika - G')
    print("-"*50)

    print()
    print("="*50)
    print("=","PROGRAM SEDERHANA".center(46),"=")
    print('='*50)

    print('~'*49)
    print('''
            MENGHITUNG LUAS DAN VOLUME
            --------------------------
            1. Menghitung Luas
            2. Menghitung Volume
            3. Exit Program'''.center(46))


    menu = input("~ Pilih menu : ")
    if menu == "1":
        Luas.start()
    elif menu == "2":
        Volume.start()
    else :
        break
        