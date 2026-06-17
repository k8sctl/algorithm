class Solution {
    public long solution(int balls, int share) {
        // nCr = (n-1)C(r-1) + (n-1)C(r)
        if (share == 0 || share == balls) return 1;
        return solution(balls - 1, share - 1) + solution(balls - 1, share);
    }
}