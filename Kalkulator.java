package membuat.simple_calculator;

import java.util.Scanner;

public class Kalkulator {
    public static void main(String[] args) {
    // Buat variabel kosong
        String pilih_menu;
        int nilai_1 = 0;
        int nilai_2 = 0;
        int hasil;
        
        Scanner input_pilihan = new Scanner(System.in);
        System.out.println("==========================");
        System.out.println("|   OPERATOR ARITMETIKA   |");
        System.out.println("==========================");
        System.out.println("    1. Tambah");
        System.out.println("    2. Kurang");
        System.out.println("    3. Kali");
        System.out.println("    4. Bagi");
        System.out.println("    5. Pangkat");
        System.out.println("---------------------------");
        System.out.println(">>> Masukkan pilihan: (1/2/3/4/5): ");
        pilih_menu = input_pilihan.nextLine();
        
    // Logika
        if (pilih_menu.equals("1")) {
            System.out.println("> Masukkan nilai A: ");
            nilai_1 = input_pilihan.nextInt();
            System.out.println("> Masukkan nilai B: ");
            nilai_2 = input_pilihan.nextInt();
            
            hasil = nilai_1 + nilai_2;
            System.out.println("## Hasil penjumlahan = "+hasil);
            
        }   else if (pilih_menu.equals("2")) {
            System.out.println("> Masukkan nilai A: ");
            nilai_1 = input_pilihan.nextInt();
            System.out.println("> Masukkan nilai B: ");
            nilai_2 = input_pilihan.nextInt();
            
            hasil = nilai_1 - nilai_2;
            System.out.println("## Hasil Pengurangan = "+hasil);
            
        }   else if (pilih_menu.equals("3")) {
            System.out.println("> Masukkan nilai A: ");
            nilai_1 = input_pilihan.nextInt();
            System.out.println("> Masukkan nilai B: ");
            nilai_2 = input_pilihan.nextInt();
            
            hasil = nilai_1 * nilai_2;
            System.out.println("## Hasil Perkalian = "+hasil);
            
        }   else if (pilih_menu.equals("4")) {
            System.out.println("> Masukkan nilai A: ");
            nilai_1 = input_pilihan.nextInt();
            System.out.println("> Masukkan nilai B: ");
            nilai_2 = input_pilihan.nextInt();
            
            hasil = nilai_1 / nilai_2;
            System.out.println("## Hasil Pembagian = "+hasil);
            
        }   else if (pilih_menu.equals("5")) {
            System.out.println("> Masukkan nilai A: ");
            nilai_1 = input_pilihan.nextInt();
            System.out.println("> Masukkan nilai B: ");
            nilai_2 = input_pilihan.nextInt();
            
            hasil = (int) Math.pow(nilai_1, nilai_2);
            System.out.println("## Hasil Perpangkatan = "+hasil);
            
        }   else {
            System.out.println("!!! Menu yang Anda masukkan salah! Mohon periksa kembali !!!");
        }
    }     
}
