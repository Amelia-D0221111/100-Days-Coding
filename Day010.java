import java.util.Scanner;
public class Main {
	public static void main(String[] args){
	    Scanner input = new Scanner(System.in);
	    System.out.print("____________________________" + 
	                       "\n Menghitung Luas : " + 
	                       "\n 1. Persegi" + 
	                       "\n 2. Persegi Panjang" + 
	                       "\n 3. Segitiga" + 
	                       "\n 4. Lingkaran" + 
	                       "\n_________________________________" + 
	                       "\n Masukkan Angka Pilihan Anda :  ");
	    int Pilihan = input.nextInt();
	    System.out.println("______________________________");
	    if (Pilihan == 1){
	        System.out.println(" Menghitung luas Persegi --> ") ;
	        System.out.print(" Masukkan Sisi Persegi : ");
	        double sisi = input.nextDouble();
	        System.out.println(" Luas Persegi dengan sisi " + sisi
	                         +   " cm = " + 
	                           (sisi*sisi) + " cm");
	        
	        }
	    else if (Pilihan == 2 ){
	        System.out.println(" Menghitung Luas Persegi Panjang --> " );
	        System.out.print(" Masukkan Panjang : ");
	        double panjang = input.nextDouble();
	        System.out.print(" Masukkan Lebar : ");
	        double lebar = input.nextDouble();
	        System.out.println(" Luas Persegi Panjang dengan " + panjang +
	                           " cm x " + lebar +
	                           " cm = " + (panjang*lebar) + 
	                           " cm");
	       }
	    else if (Pilihan == 3 ){
	        System.out.println(" Menghitung Luas Segitiga --> " );
	        System.out.print(" Masukkan Alas : ");
	        double alas = input.nextDouble();
	        System.out.print(" Masukkan Tinggi : ");
	        double tinggi = input.nextDouble();
	        System.out.println(" Luas Segitiga dengan 1/2 * " + alas +
	                           " cm x " + tinggi  +
	                           " cm = " + (0.5 * (alas * tinggi))+ 
	                           " cm");
	       }
	    else if (Pilihan == 4 ){
	        System.out.println(" Menghitung Luas Lingkaran --> " );
	        System.out.print(" Masukkan Jari-jari (R) : ");
	        double r = input.nextDouble();
	        System.out.println(" Luas Lingkaran dengan Phi (π) =  3.14   " + 
	                           "\n Jari-jari (R) = " +  r + 
	                           " adalah " + (3.14 * (Math.pow(r,2))) + 
	                           " cm");
	       }
	    else {
	        System.out.println(" Periksa kembali pilihan anda!");
	    }
	
	}
}