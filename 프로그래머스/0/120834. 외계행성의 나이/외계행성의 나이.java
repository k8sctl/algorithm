class Solution {
    public String solution(int age) {
        String alpha = "abcdefghij";
        String ageStr = String.valueOf(age);
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < ageStr.length(); i++) {
            int digit = ageStr.charAt(i) - '0';  // 문자 → 숫자
            sb.append(alpha.charAt(digit));      // 숫자 → 알파벳
        }
        
        return sb.toString();
    }
}