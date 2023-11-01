import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<String> daftarBarang = new ArrayList<>();
        Scanner input = new Scanner(System.in);
        
        System.out.println("Selamat datang di Aplikasi Manajemen Barang");
        
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Tambah Barang");
            System.out.println("2. Lihat Barang");
            System.out.println("3. Keluar");
            System.out.print("Pilih menu (1/2/3): ");
            int pilihan = input.nextInt();
            
            if (pilihan == 1) {
                    System.out.print("Masukkan nama barang: ");
                    String namaBarang = input.next();
                    daftarBarang.add(namaBarang);
                    System.out.println("Barang telah ditambahkan.");
            }
            else if (pilihan == 2){
                    System.out.println("Daftar Barang:");
                    for (String barang : daftarBarang) {
                        System.out.println(barang);

                    }
             }
            else if (pilihan == 3){
                    System.out.println("Terima kasih!");
                    
                    break;
            }
            else {
                    System.out.println("Pilihan tidak valid. Silakan pilih lagi.");
            }
        }
   
    }

}