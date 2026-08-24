# Last updated: 8/24/2026, 12:21:13 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        nums1.sort()