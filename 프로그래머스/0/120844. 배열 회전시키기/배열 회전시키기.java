class Solution {
    public int[] solution(int[] numbers, String direction) {
        int n = numbers.length;
        int[] answer = new int[n];
        
        if (direction.equals("right")) {
            for (int i = 0; i < n; i++) {
                answer[(i + 1) % n] = numbers[i];
            }
        } else {  // "left"
            for (int i = 0; i < n; i++) {
                answer[i] = numbers[(i + 1) % n];
            }
        }
        
        return answer;
    }
}