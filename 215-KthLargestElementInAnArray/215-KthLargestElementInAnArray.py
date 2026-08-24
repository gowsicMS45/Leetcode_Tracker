# Last updated: 8/24/2026, 12:20:32 PM
class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap , num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]