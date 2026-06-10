class Solution {
    public int trailingZeroes(int n) {
        int ans=0;
        if(n<5)
        return 0;
        while(n>0){
            n/=5;
            ans+=n;
        }
        return ans;
    }
}