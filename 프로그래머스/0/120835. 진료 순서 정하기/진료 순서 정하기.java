import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] solution(int[] emergency) {
        // 1. 내림차순 정렬 복사본
        int[] sorted = emergency.clone();
        Arrays.sort(sorted);

        // 2. 값 → 순위 매핑
        HashMap<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < sorted.length; i++) {
            rankMap.put(sorted[i], sorted.length - i);
        }

        // 3. 원본 순서대로 순위 반환
        int[] result = new int[emergency.length];
        for (int i = 0; i < emergency.length; i++) {
            result[i] = rankMap.get(emergency[i]);
        }

        return result;
    }
}