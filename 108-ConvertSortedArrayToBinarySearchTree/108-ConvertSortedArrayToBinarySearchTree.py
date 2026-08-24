# Last updated: 8/24/2026, 12:21:04 PM
class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root