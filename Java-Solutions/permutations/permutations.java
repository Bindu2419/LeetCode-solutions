import java.util.*;

class Solution {
    
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        
        backtrack(nums, used, new ArrayList<>(), result);
        
        return result;
    }
    
    private void backtrack(int[] nums, boolean[] used,
                           List<Integer> current,
                           List<List<Integer>> result) {
        
        // Base case
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            
            if (used[i]) continue;   // skip if already used
            
            // Choose
            used[i] = true;
            current.add(nums[i]);
            
            // Explore
            backtrack(nums, used, current, result);
            
            // Un-choose (Backtrack)
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}
