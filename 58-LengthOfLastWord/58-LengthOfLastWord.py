# Last updated: 8/24/2026, 12:21:25 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])