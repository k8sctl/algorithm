import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> store = new HashMap<>();
        
        // 각 숫자의 빈도수 계산
        for (int num : array) {
            store.put(num, store.getOrDefault(num, 0) + 1);
        }
        
        // 최대 빈도수 찾기
        int maxCount = Collections.max(store.values());
        
        // 최빈값 수집
        List<Integer> modes = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : store.entrySet()) {
            if (entry.getValue() == maxCount) {
                modes.add(entry.getKey());
            }
        }
        
        // 최빈값이 여러 개면 -1, 하나면 반환
        return modes.size() > 1 ? -1 : modes.get(0);
    }
}