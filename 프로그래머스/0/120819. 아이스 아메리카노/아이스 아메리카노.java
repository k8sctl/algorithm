class Solution {
    public int[] solution(int money) {
        int[] answer = {0, 0};
        int count = 0;
        int iceAmericanoPrice = 5500;
        
        while (money >= iceAmericanoPrice) {
            count++;
            money -= iceAmericanoPrice;
        }
        
        answer[0] = count;
        answer[1] = money;
        
        return answer;
    }
}