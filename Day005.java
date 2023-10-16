public class Main {
	public static void main(String[] args) {
	    String nama = "Clara";
	    int nilai = 7;
	    if (nilai >= 90 && nilai <=100 ){
	        System.out.println(nama + "kamu Lulus dengan nilai " + nilai + "(A)");
	    }
	    else if (nilai >= 80 && nilai <=89 ){
	        System.out.println(nama + " kamu Lulus dengan nilai " + nilai + "(A-)");
	    }
	    else if (nilai >= 70 && nilai <=79 ){
	        System.out.println(nama + " kamu Lulus dengan nilai " + nilai + "(B)");
	    }
	    else if (nilai >= 60 && nilai <=69 ){
	        System.out.println(nama + " kamu Lulus dengan nilai " + nilai + "(C)");
	    }
	    else if (nilai >= 50 && nilai <=59 ){
	        System.out.println(nama + " kamu Lulus dengan nilai " + nilai + "(D)");
	    }
	    else if (nilai >= 0 && nilai <=40  ){
	        System.out.println(nama + " silahkan ujian kembali karena nilai kamu " + nilai + "(E)");
	    }
	    else {
	        System.out.println (" periksa kembali");
	    }
	        
	}
}