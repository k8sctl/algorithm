class Solution {
    public int[] solution(int[] num_list) {
        int index_length = num_list.length;
        int[] answer = new int[index_length];
        
        for (int num : num_list) {
            answer[--index_length] = num;
        }
        
        return answer;
    }
}