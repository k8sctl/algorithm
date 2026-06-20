class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        
        int s_index = 0;
        int l_index = numbers.length - 1;
        
        for (int count = 0 ; count < k-1 ; count++) {
            
            if (s_index == l_index) {
                s_index = 1;
            } else if (s_index == l_index-1) {
                s_index = 0;
            } else {
                s_index += 2;
            }
        }
        
        answer = numbers[s_index];
        
        return answer;
    }
}