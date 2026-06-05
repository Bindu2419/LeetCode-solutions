class Solution {
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> li = new ArrayList<>();

        if (root == null) {
            return li;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {

            int s = q.size();

            for (int i = 0; i < s; i++) {

                TreeNode curr = q.poll();

                // If last node of this level
                if (i == s - 1) {
                    li.add(curr.val);
                }

                if (curr.left != null) {
                    q.add(curr.left);
                }

                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
        }

        return li;
    }
}
