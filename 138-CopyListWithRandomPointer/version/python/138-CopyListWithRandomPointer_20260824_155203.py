# Last updated: 8/24/2026, 3:52:03 PM
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        mp = {}
        cur = head

        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next)
            mp[cur].random = mp.get(cur.random)
            cur = cur.next

        return mp[head]