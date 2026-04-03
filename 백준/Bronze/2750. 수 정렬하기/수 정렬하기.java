import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for (int i = 0 ; i < arr.length ; i++) {
            arr[i] = sc.nextInt();
        }
        
        for (int i = 0 ; i < arr.length ; i++) {
            int min = arr[i];
            for (int j = i+1 ; j < arr.length ; j++) {
                if (arr[j] < min) {
                    min = arr[j];
                    arr[j] = arr[i];
                    arr[i] = min;
                }
            }
        }
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}