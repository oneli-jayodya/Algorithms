package dataStructuers;

public class ExcecuteTime {

	public static void main(String[] args) {
		
		int[] number = {1,2,3,4,5};
		long start = System.nanoTime();
		
		for(int num : number) {
			System.out.print(num+" ");
		}
		
		long end = System.nanoTime();
		
		long execute = end - start;
		System.out.println("\n"+execute);

	}

}
