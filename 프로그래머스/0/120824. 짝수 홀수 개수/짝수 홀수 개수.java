class Solution {
    public int[] solution(int[] num_list) {
        int evenCount = 0;
        int oddCount = 0;
        int[] answer = {evenCount, oddCount};
        final int EVEN_INDEX = 0;
        final int ODD_INDEX = 1;
        
        for (int num : num_list) {
            if (num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        
        answer[EVEN_INDEX] = evenCount;
        answer[ODD_INDEX] = oddCount;
        
        return answer;
    }
}