import java.io.*;
import java.util.*;

public class Main {
    static int findMax(int[] array) {
        int max = array[0];
        for (int n : array) {
            if (n > max) {
                max = n;
            }
        }
        return max;
    }

    static double newScoreSum(int[] array) {
        double sum = 0;
        int max = findMax(array);

        for (int n : array) {
            sum += (double) n / max * 100;
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] array = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(newScoreSum(array) / N);
    }
}