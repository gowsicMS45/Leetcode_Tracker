// Last updated: 8/24/2026, 12:21:11 PM
class Solution {
            ArrayList<Integer> ans= new ArrayList();
    public List<Integer> inorderTraversal(TreeNode root) {
       
        if(root!=null){
            inorderTraversal(root.left);
            ans.add(root.val);
            inorderTraversal(root.right);
        }
        return ans;
    }
}

  