# Last updated: 8/24/2026, 12:21:34 PM
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        res = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[res]=nums[i]
                res +=1
        return res

        