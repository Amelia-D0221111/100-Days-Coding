import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		String username1;
        int password1 ;
        
        username1 = "amelia" ;
        password1 = 12345;
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("Halaman Login");
        System.out.println("________________");
    
        System.out.print(" Username :");
        String username = input.nextLine();

        System.out.print(" Password :");
        int password = input.nextInt();
        
        if (username.equals(username1) && password == password1 ) {
            System.out.println("Login Berhasil") ;
        }
        else {
            System.out.println("Periksa Kembali");
        }
	}
	
}