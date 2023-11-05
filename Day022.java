import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> angka1 = new ArrayList<>();
        List<Integer> angka2= new ArrayList<>();

        // Menambahkan elemen ke dalam angka1
        angka1.add(5);
        angka1.add(2);
        angka1.add(8);

        // Menambahkan elemen ke dalam angka 2
        angka2.add(1);
        angka2.add(7);
        angka2.add(3);

        System.out.println("List Pertama :  " + angka1);

        System.out.println("List Kedua :  " + angka2);

        // Menggabungkan kedua list
        List<Integer> gabung = new ArrayList<>(angka1);
        gabung.addAll(angka2);
        System.out.println("Gabungan kedua list: " + gabung);

        // Mengurutkan list
        Collections.sort(gabung);
        System.out.println("List setelah diurutkan: " + gabung);

    }
}
