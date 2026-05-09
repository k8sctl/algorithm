class Solution {
    public int solution(int slice, int n) {
        int quantity = 1;
        
        while ((slice * quantity) < n) {
            quantity += 1;
        }
        
        return quantity;
    }
}