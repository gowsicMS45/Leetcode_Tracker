// Last updated: 8/24/2026, 12:21:56 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        java.util.HashMap<Character, Integer> map = new java.util.HashMap<>();
        int maxLength = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            if (map.containsKey(currentChar) && map.get(currentChar) >= left) {
                left = map.get(currentChar) + 1;
            }
            map.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}