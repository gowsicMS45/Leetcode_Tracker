# Last updated: 8/24/2026, 12:20:10 PM
class Solution(object):
    def longestPalindrome(self, s):

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        oddFound = False

        for count in freq.values():

            length += (count // 2) * 2

            if count % 2 == 1:
                oddFound = True

        if oddFound:
            length += 1

        return length