# Last updated: 8/24/2026, 12:21:09 PM
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right ,q.right)
        return False

        