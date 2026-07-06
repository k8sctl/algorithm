import java.util.Stack;

class Solution {
    public int solution(String s) {
        Stack<Integer> stack = new Stack<>();
        String[] tokens = s.split(" ");
        
        for (String token : tokens) {
            if (token.equals("Z")) {
                stack.pop();  
            } else {
                stack.push(Integer.parseInt(token)); 
            }
        }
        
        int answer = 0;
        for (int num : stack) {
            answer += num;
        }
        
        return answer;
    }
}