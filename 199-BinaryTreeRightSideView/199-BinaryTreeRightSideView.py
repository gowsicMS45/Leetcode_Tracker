# Last updated: 8/24/2026, 12:20:38 PM
from collections import deque

class Solution:
    def rightSideView(self, root):
        ans = []

        if root is None:
            return ans

        q = deque()
        q.append(root)
        q.append(None)

        while q:
            temp = q.popleft()

            if temp is None:
                if q:
                    q.append(None)
                continue

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

            if q[0] is None:
                ans.append(temp.val)

        return ans