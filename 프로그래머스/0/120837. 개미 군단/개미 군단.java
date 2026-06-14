class Solution {
    public int solution(int hp) {
        int result = 0;
        
        result += hp / 5;
        hp = hp % 5;
        
        result += hp / 3;
        hp = hp % 3;
        
        result += hp;
    
        return result;
    }
}