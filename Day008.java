import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		int bil1 , bil2 , perhitungan,hasil;
		System.out.println(" Kalkulator ");
		Scanner input = new Scanner(System.in);
        System.out.print(" angka pertama : ");
        bil1 = input.nextInt();
        System.out.print(" angka kedua : ");
        bil2 = input.nextInt();
        
        System.out.println("_____________" + 
                           "\n ");
        System.out.println(" Kalkulator ");
        System.out.println("_____________ ");
        System.out.print( "Pilih perhitungan yang ingin anda lakukan !" + 
                           "\n 1. Tambah" + 
                           "\n 2. Kurang" + 
                           "\n 3. Kali" + 
                           "\n 4. Bagi" + 
                           "\n_____________" + 
                           "\n Pilih Angka : " );
         perhitungan = input.nextInt( );
         if (perhitungan == 1 ){
             hasil = bil1 + bil2 ;
             System.out.println(bil1 + " + " + bil2 + " = " + hasil);
         }
         else if (perhitungan == 2 ){
             hasil = bil1 - bil2 ;
             System.out.println(bil1 + " - " + bil2 + " = " + hasil);
         }
         else if (perhitungan == 3 ){
             hasil = bil1 * bil2 ;
             System.out.println(bil1 + " x " + bil2 + " = " + hasil);
         }
         else if (perhitungan == 4 ){
             hasil = bil1 / bil2 ;
             System.out.println(bil1 + " / " + bil2 + " = " + hasil);
             }
         else {
             System.out.println("periksa pilihan perhitungan yang anda masukkan!");
         }
             
  
             
         
         
        
	}
}