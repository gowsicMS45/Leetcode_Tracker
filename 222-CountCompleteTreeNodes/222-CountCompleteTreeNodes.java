// Last updated: 8/24/2026, 12:20:30 PM
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int leftHeight = getHeight(root, true);
        int rightHeight = getHeight(root, false);
        if (leftHeight == rightHeight) {
            return (1 << leftHeight) - 1;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
    
    private int getHeight(TreeNode node, boolean left) {
        int h = 0;
        while (node != null) {
            h++;
            node = left ? node.left : node.right;
        }
        return h;
    }
}
