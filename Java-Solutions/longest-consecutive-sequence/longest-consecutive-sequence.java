class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for(int n : nums)
            set.add(n);

        int longest = 0;

        for(int n : set) {

            if(!set.contains(n - 1)) {

                int current = n;
                int streak = 1;

                while(set.contains(current + 1)) {
                    current++;
                    streak++;
                }

                longest = Math.max(longest, streak);
            }
        }

        return longest;
    }
}