class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 or t2
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)

        return node
