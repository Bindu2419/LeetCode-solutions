class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {

        Set<List<Integer>> ans = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {

            for(int j = i + 1; j < nums.length; j++) {

                HashSet<Long> set = new HashSet<>();

                for(int k = j + 1; k < nums.length; k++) {

                    long fourth = (long)target - nums[i] - nums[j] - nums[k];

                    if(set.contains(fourth)) {

                        List<Integer> temp = Arrays.asList(
                            nums[i],
                            nums[j],
                            nums[k],
                            (int)fourth
                        );

                        Collections.sort(temp);
                        ans.add(temp);
                    }

                    set.add((long)nums[k]);
                }
            }
        }

        return new ArrayList<>(ans);
    }
}
// class Solution {
//     public List<List<Integer>> fourSum(int[] nums, int target) {

//         Arrays.sort(nums);

//         List<List<Integer>> ans = new ArrayList<>();

//         for(int i = 0; i < nums.length - 3; i++) {

//             if(i > 0 && nums[i] == nums[i - 1])
//                 continue;

//             for(int j = i + 1; j < nums.length - 2; j++) {

//                 if(j > i + 1 && nums[j] == nums[j - 1])
//                     continue;

//                 int left = j + 1;
//                 int right = nums.length - 1;

//                 while(left < right) {

//                     long sum = (long)nums[i] + nums[j] + nums[left] + nums[right];

//                     if(sum == target) {

//                         ans.add(Arrays.asList(
//                             nums[i],
//                             nums[j],
//                             nums[left],
//                             nums[right]
//                         ));

//                         while(left < right && nums[left] == nums[left + 1])
//                             left++;

//                         while(left < right && nums[right] == nums[right - 1])
//                             right--;

//                         left++;
//                         right--;

//                     }
//                     else if(sum < target) {
//                         left++;
//                     }
//                     else {
//                         right--;
//                     }
//                 }
//             }
//         }

//         return ans;
//     }
// }
// class Solution {
//     public List<List<Integer>> fourSum(int[] nums, int target) {
//         Set<List<Integer>> set=new HashSet<>();
//         for(int i=0;i<nums.length;i++){
//             for(int j=i+1;j<nums.length;j++){
//                 for(int k=j+1;k<nums.length;k++){
//                     for(int l=k+1;l<nums.length;l++){
//                         long sum=(long)nums[i]+nums[j]+nums[k]+nums[l];
//                     if(sum==target){
//                         List<Integer> temp =Arrays.asList(nums[i],nums[j],nums[k],nums[l]);
//                         Collections.sort(temp);
//                         set.add(temp);
//                     }
//                     }
//                 }
//             }
//         }
//         return new ArrayList<>(set);  
//     }
// }