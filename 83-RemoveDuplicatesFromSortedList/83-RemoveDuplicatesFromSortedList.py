# Last updated: 8/24/2026, 12:21:15 PM
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head