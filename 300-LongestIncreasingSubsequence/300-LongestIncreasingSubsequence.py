# Last updated: 8/24/2026, 12:20:17 PM
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
            
        n = len(nums)
        dp = [1] * n
        max_lis = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_lis = max(max_lis, dp[i])
            
        return max_lis