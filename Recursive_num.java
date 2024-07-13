package dataStructuers;

public class Recursive_num {

	static void number(int n) {
		
		if(n == 1) {
			System.out.print(n+" ");
		}else {
			number(n-1);
			System.out.print(n+" ");
		}
	}
	public static void main(String[] args) {
		number(12);
	}

}
