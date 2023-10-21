import java.util.Scanner;
public class Main {
	public static void main(String[] args){
	    int totalBelanja;
	    double totalBayar;
	    Scanner input = new Scanner(System.in);
	    System.out.println("____________________");
	    System.out.println("Menghitung Diskon");
	    System.out.println("____________________");
	    System.out.print("Harga total Belanja : Rp.");
	    
	    totalBelanja = input.nextInt();
	   System.out.println("____________________");
	     if (totalBelanja>=150000 && totalBelanja <= 300){
	        totalBayar = totalBelanja - (totalBelanja * 0.1);
	        System.out.println( "Potongan Diskon 10% =  Rp. " + (totalBelanja * 0.1) + "\nTotal Bayar = Rp." + totalBayar);
	    }
	     else if (totalBelanja>= 350000 && totalBelanja <= 500000){
	        totalBayar = totalBelanja - (totalBelanja * 0.2);
	        System.out.println( "Potongan Diskon 20% = Rp. " + (totalBelanja * 0.1) + "\nTotal Bayar = Rp." + totalBayar);
	    }
	     else if  (totalBelanja>=550000 ){
	        totalBayar = totalBelanja - (totalBelanja * 0.1);
	        System.out.println( "Potongan Diskon 30% = Rp. " + (totalBelanja * 0.3) + "\nTotal Bayar = Rp." + totalBayar);
	    }
	    else {
	        System.out.println("Total Bayar = Rp. " + 
	                           totalBelanja);
	        System.out.println("silahkan belanja minimal Rp.150000 untuk mendapatkan diskon");
	    }
	    
	}
}