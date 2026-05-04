class Solution {
    public int solution(int n) {
        int result = 1;
        while(true) {
           if ((result * 6) % n == 0) {
               return result;
           }
            result++;
        }
    }
}