class Solution {
    public int solution(int n) {
        int answer = 0;
        int quotient = n / 7;
        int remainder = n % 7;
        if (remainder != 0) quotient += 1;
        answer = quotient;
        return answer;
    }
}