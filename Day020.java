public class Main {
    public static void main(String[] args) {
        // Konversi string ke tipe data primitif
        String angkaStr = "123";
        int angkaInt = Integer.parseInt(angkaStr);

        String angkaDesimalStr = "45.67";
        double angkaDesimal = Double.parseDouble(angkaDesimalStr);

        String booleanStr = "true";
        boolean booleanValue = Boolean.parseBoolean(booleanStr);

        // Menampilkan hasil konversi
        System.out.println("Konversi String ke int: " + angkaInt);
        System.out.println("Konversi String ke double: " + angkaDesimal);
        System.out.println("Konversi String ke boolean: " + booleanValue);
    }
}
