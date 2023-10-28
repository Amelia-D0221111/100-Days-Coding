public class Main {
	public static void main(String[] args) {
		// int ke string dengan integer reference / non primitif
		Integer nilai = 28;
		
		String nilaiKonver = nilai.toString();
		System.out.println(nilaiKonver.getClass().getName());
	}
}