import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] scores = new int[N];
        
      	for (int i = 0 ; i < N ; i++) {
        	scores[i] = sc.nextInt();
        }
        
        int sum = 0;
        int maxScore = scores[0];
        
        for (int score : scores) {
        	if (score > maxScore) {
            	maxScore = score;
            }
    		sum += score;
        }
        System.out.print(sum * 100.0 / maxScore / N);
    }
}