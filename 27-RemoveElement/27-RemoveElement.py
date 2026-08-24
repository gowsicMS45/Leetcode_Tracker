# Last updated: 8/24/2026, 12:21:32 PM
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)

        