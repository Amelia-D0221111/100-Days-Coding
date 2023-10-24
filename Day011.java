import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int bilangan;
        System.out.println("Menentukan Bilangan Genap atau Ganjil");
        System.out.println("______________________________");
        System.out.print("Masukan Bilangan = ");
        bilangan = input.nextInt();
        
        if (bilangan %2 == 0){
            System.out.println("Bilangan " + bilangan + " merupakan Bilangan Genap");
        }
        
        else {
             System.out.println("Bilangan " + bilangan + " merupakan Bilangan Ganjil");
        }
    
  }
}