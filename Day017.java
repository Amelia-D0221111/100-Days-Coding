public class Main {
 public static void main(String[] args) {
  
   // Array Nama
   String[] nama = {"Amelia", "Edwin"};

   // mencetak elemen
   System.out.println("Elemen Array:");
   
   for(int i = 0; i < nama.length; i++) {
   	System.out.println(String.valueOf(i+1) + ". " + nama[i]);
   }
 }
}