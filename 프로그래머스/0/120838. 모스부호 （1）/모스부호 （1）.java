class Solution {
    public String solution(String letter) {
        StringBuilder answer = new StringBuilder();
        
        String[] morse = {
            ".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."
        };
        
        for (String code : letter.split(" ")) {
            for (int i = 0; i < morse.length; i++) {
                if (code.equals(morse[i])) {
                    answer.append((char)('a' + i));
                     break;
                }
            }
        }
        
        return answer.toString();
    }
}