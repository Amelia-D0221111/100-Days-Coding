public class Main {
	public static void main(String[] args) {
		String nama,alamat;
		nama = "Amelia";
		alamat = "Polewali Mandar";
		int umur = 20;
		float tinggi = 1.59f;
		double berat = 60.0;
		char size = 'L';
		boolean mahasiswa = true;
		
		System.out.println("Biodata Singkat");
		System.out.println("__________________");
		System.out.println("Nama : " + nama);
		System.out.println("Umur : " + umur);
		System.out.println("Alamat : " + alamat);
		System.out.println("Tinggi : " + tinggi + " m");
		System.out.println("Berat : "+ berat + " kg");
		System.out.println("Ukuran Baju : " +size);
		System.out.println("Apakah Mahasiswa ? : " + mahasiswa);
	}
}