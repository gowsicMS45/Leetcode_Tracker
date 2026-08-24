// Last updated: 8/24/2026, 12:20:52 PM
class Solution {
    public boolean hasCycle(ListNode head) {
        Map<ListNode,Integer> map = new HashMap<>();
        ListNode temp = head;
        while(temp !=null) {
            if(map.containsKey(temp)) return true;
            map.put(temp,temp.val);
            temp = temp.next;
        }
        return false;
    }
}
        
