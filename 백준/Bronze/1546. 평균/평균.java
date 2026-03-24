import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] scores = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
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