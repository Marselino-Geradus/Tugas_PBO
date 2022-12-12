while True:
    print('''
                            ----------------------------
                            Nama: Marselino Geradus
                            NIM: D0221364
                            Kelas: Informatika-G
                            ----------------------------
''')

    
    print('='*39)
    print('     =|= PROGRAM MENGHITUNG LUAS DAN KELILING =|=  ')
    print('''
                        1. Luas dan Keliling Persegi
                        2. Luas dan Keliling Lingkaran
                        3. Luas dan Keliling Segitiga
                ''')
    print('='*39)
    print()

    pilih = input("~ Masukkan pilihan: ")
    if pilih == '1':
        print(">>> Luas dan Keliling Persegi <<<")
        s = int(input("=> Masukan panjang sisi: "))
        luasp = s**2
        kelp = 4*s
        print(">> Luas persegi = ",luasp, ' cm')
        print('>> Keliling persegi = ',kelp, ' cm')
        print('~'*41)
        print('~'*41)
        
    elif pilih == '2':
        print(">>> Luas dan Keliling Lingkaran <<<")
        r = float(input("~ Masukkan jari-jarinya: "))
        phi = 3.14
        luasl = phi*r*r
        kell = 2*phi*r
        print(">> Luas lingkaran = ",luasl, ' cm')
        print('>> Keliling lingkaran = ',kell, ' cm')
        print('~'*41)
        print('~'*41)
        
        
    elif pilih == '3':    
        print(">>> Luas dan Keliling Segitiga <<<")
        a = int(input("~ Masukan alas: "))
        t = int(input("~ Masukan tinggi: "))
        luass = int((a*t)/2)

        sisiA = int(input('Sisi A : '))
        sisiB = int(input('Sisi B : '))
        sisiC = int(input('Sisi C : '))
        kels = sisiA + sisiB + sisiC
        print(">> Luas segitiga  = ", luass, ' cm')
        print('>> Keliling segitiga = ',kels, ' cm')
        print('~'*41)
        print('~'*41)
        
    else:
        print("pilihan tidak terdeteksi")
        break
