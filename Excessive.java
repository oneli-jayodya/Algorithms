package dataStructuers;

public class Excessive {

	void countdown(int n) {
		if(n == 1) {
			System.out.println(" "+n);
		}else {
		System.out.println(" "+n);
		countdown(n-1);
		}
	}
	
	public static void main(String[] args) {
		
		Excessive m = new Excessive(); 
		m.countdown(5);

	}

}
