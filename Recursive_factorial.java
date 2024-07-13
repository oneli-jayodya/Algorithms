package dataStructuers;

public class Recursive_factorial {

	static int factorial(int n) {
		if(n == 0 || n == 1) {
			return 1;
		}else {
			return n *factorial(n-1); //like non-tail
		}
	}
	
	public static void main(String[] args) {
		System.out.println(factorial(3));

	}

}
