class Solution {

    public int minOperations(int[] nums, int[] numsDivide) {

        // Step 1: Find GCD of numsDivide
        int g = numsDivide[0];
        for (int n : numsDivide) {
            g = gcd(g, n);
        }

        // Step 2: Sort nums
        Arrays.sort(nums);

        // Step 3: Find smallest divisor of g
        for (int i = 0; i < nums.length; i++) {
            if (g % nums[i] == 0) {
                return i;  // i deletions
            }
        }

        return -1;
    }

    private int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
