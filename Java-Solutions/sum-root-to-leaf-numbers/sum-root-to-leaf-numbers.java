/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentSum) {

        if (node == null)
            return 0;

        // Build current number
        currentSum = currentSum * 10 + node.val;

        // If leaf node
        if (node.left == null && node.right == null) {
            return currentSum;
        }

        // Recur for left and right
        return dfs(node.left, currentSum) +
               dfs(node.right, currentSum);
    }
}
