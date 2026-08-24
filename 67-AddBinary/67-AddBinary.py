# Last updated: 8/24/2026, 12:21:21 PM
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
