// Last updated: 8/24/2026, 12:21:27 PM
class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0]; 
        int maxSum = nums[0];   
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum; 
    }
}