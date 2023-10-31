import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<String> buah = new ArrayList<>();
        buah.add("Apel");
        buah.add("Pisang");
        buah.add("Jeruk");
        buah.add("Mangga");

        // Menampilkan isi List
        System.out.println("Isi List:");
        for (String item : buah) {
            System.out.println(item);
        }

        // Menghitung jumlah elemen dalam List
        int itemCount = buah.size();
        System.out.println("Jumlah item dalam list: " + itemCount);

        // Mengakses elemen berdasarkan indeks
        String firstItem = buah.get(0);
        System.out.println("Item pertama: " + firstItem);

        // Menghapus elemen dari List
        buah.remove("Jeruk");

        // Setelah menghapus
        System.out.println("Isi List setelah menghapus Jeruk:");
        for (String item : buah) {
            System.out.println(item);
        }
    }
}
