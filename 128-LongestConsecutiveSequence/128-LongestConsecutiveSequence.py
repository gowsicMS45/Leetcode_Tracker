# Last updated: 8/24/2026, 12:20:55 PM
class Solution(object):
    def longestConsecutive(self, nums):
        s= set(nums)
        max_len =0
        for n in s:
            if n-1 not in s:
                count = 1
                while n + count in s:
                    count+=1
                max_len = max(max_len,count)
        return max_len

        