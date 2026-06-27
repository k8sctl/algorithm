class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        String vowels = "aeiou";
        
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (vowels.indexOf(c) == -1) {
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}