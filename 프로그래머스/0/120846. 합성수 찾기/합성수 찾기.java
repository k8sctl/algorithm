class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int num = 1 ; num <= n ; num++) {
            int count = 0;  
            for (int i = 1 ; i <= num ; i++) {
                if (num % i == 0) {
                    count++;
                } 
                if (count >= 3) {
                    answer++;
                    break;
                }
            }
        }
        return answer;
    }
}