class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] result = Arrays.copyOf(nums, 2 * n);  // copy nums into size 2n
        System.arraycopy(nums,0,result,n,n);
        return result;
    }
}