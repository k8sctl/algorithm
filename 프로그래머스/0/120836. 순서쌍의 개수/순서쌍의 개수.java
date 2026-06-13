class Solution {
    public int solution(int n) {
        int count = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                count += 2;         
                if (i == n / i) count--;
            }
        }
        return count;
    }
}