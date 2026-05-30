class Solution {
    public int solution(int n, int k) {
        int freeDrink = n / 10;
        k -= freeDrink;
        int result = (12000 * n) + (2000 * k);
        return result;
    }
}