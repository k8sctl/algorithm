import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N, M 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // N개의 수를 배열에 저장
        int[] arr = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int k = 1; k < N+1; k++) {
            arr[k] = Integer.parseInt(st.nextToken());
        }
        
        int[] sum = new int[N+1];
        for (int i = 1; i < N+1; i++) {
                sum[i] = sum[i-1] + arr[i]; 
        }
        
        // M번 반복
        for (int k = 0; k < M; k++) {
 
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            System.out.println(sum[j] - sum[i-1]);
        }
    }
}