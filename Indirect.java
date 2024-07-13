package dataStructuers;

public class Indirect {
	
	static void funA(int n) {
		
		if(n>0) {
			System.out.println(n);
			funB(n-1);
		}
	}
	
	static void funB(int i) {
		if(i>0) {
			System.out.println(i);
			funA(i/2);
		}
	}
	
	public static void main(String[] args) {
		funA(20);

	}

}
