// Last updated: 8/24/2026, 12:20:20 PM
class Solution {
    public int missingNumber(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int i=0; i<=nums.length;i++){
            map.put(i,1);
        }
        for (int i:nums){
            map.remove(i);
        }
        for(int i : map.keySet())
        return i;
        return -1;
     
    }
}
  