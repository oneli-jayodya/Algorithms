package dataStructuers;

public class Recursive_SumDigit {
	
	static int cal(int num) {
		if(num<10){
			return num;			
		}else {
			int res = num%10;
			num = num/10;
			return (res+cal(num)); //tail
//			return num%10 + cal(num/10);
		}
	}

	public static void main(String[] args) {
		System.out.print(cal(1234));
	}

}
