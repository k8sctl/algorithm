import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int difference = 0;
        int min_difference = 100;
        
        Arrays.sort(array);  // ← 이것만 추가!
        
        for (int i = 0 ; i < array.length ; i++) {
            
            if (array[i] > n) {
                difference = array[i] - n;
            } else {
                difference = n - array[i];
            }
                
            if (min_difference > difference) {
                min_difference = difference;
                answer = array[i];
            }
        }
        
        return answer;
    }
}