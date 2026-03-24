import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
    	// 필요한 변수 선언
        int n = 0;
        String sNum = "";
        int sum = 0;
        
        // 입력에 필요한 scanner 객체 생성
        Scanner sc = new Scanner(System.in);
        
        // 입력
        n = sc.nextInt();
        sc.nextLine();
        
        sNum = sc.nextLine();
        
        // 처리
        for (int i = 0 ; i < n ; i++) {
        	char c = sNum.charAt(i);
            int num = c - '0';
            sum = sum + num;
        }
        
        // 출력
        System.out.print(sum);
    }
}