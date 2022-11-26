nama = "Marselino Geradus"
kelas = "Informatika_G 021"
no_rek = int(input("> Nomor rekening: "))
pin = int(input('> Pin: '))
saldo = int(input('> Saldo: '))

while True:
    print('\n' *3)
    print("=" * 20)
    print("=" + "ATM SEDERHANA".center(31) + "=")
    print("=" * 20)
    print(f'''
Hai {nama}!
Selamat Datang di Mesin ATM Sederhana!''')
    print('~'*20)
    print('''Menu Transaksi :
1. Informasi Saldo
2. Tarik Tunai
3. Keluar
''')
    pilihan = input("Masukkan pilihan Anda : ")
    print()
    if pilihan == '1':
        print(f"~~~ Saldo rekening Anda : Rp. {saldo} ~~~")
        konfirmasi = input("(Tekan tombol apapun untuk lanjut)")
    elif pilihan == '2':
        while True:
            if saldo >= 50000:
                uang = int(input("> Masukkan jumlah penarikan : "))
                if uang % 50000 == 0:
                    saldo1 = saldo - uang
                    print("~~ Saldo ditarik : Rp. ", uang)
                    print("~~ Sisa saldo Anda : Rp. ", saldo1)
                    saldo = saldo1
                    konfirmasi = input("(Tekan tombol apapun untuk lanjut)")
                    break
                  
                else:
                    print('''Nominal tidak diketahui. Silahkan masukkan jumlah penarikan kelipatan 50.000''')
                    konfirmasi = input("(Tekan tombol apapun untuk lanjut)")
            else:
                print(">> Transaksi Gagal! Saldo tidak mencukupi. <<")
                konfirmasi = input("(Tekan enter untuk kembali)")
                break
    elif pilihan == '3':
      break
    else:
      print("Perintah tidak ditemukan")
      konfirmasi = input("(Tekan tombol apapun untuk lanjut)")
