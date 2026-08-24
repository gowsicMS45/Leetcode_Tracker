// Last updated: 8/24/2026, 12:20:33 PM
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next; 
            curr.next = prev;           
            prev = curr;              
            curr = next;               
        }

        return prev; 
    }
}
