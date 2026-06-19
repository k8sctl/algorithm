class Solution {
    public int[][] solution(int[] num_list, int n) {
        int rows = num_list.length / n;
        int[][] answer = new int[rows][n];
        
        int num_index = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < n; j++) {
                answer[i][j] = num_list[num_index];
                num_index++;
            }
        }
        
        return answer;
    }
}