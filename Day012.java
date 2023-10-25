public class Main {
    public static void main(String[] args) {
        int tinggi = 5;
        
        for (int i = 1; i <= tinggi; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }
            
            for (int k = i; k <= tinggi; k++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
