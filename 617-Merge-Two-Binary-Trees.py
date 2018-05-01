class Solution_recursive:
    def mergeTrees(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 or t2
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)

        return node

class Solution_iterative:
    def mergeTrees(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 or t2
        root = TreeNode(None)
        stack1, stack2, stack = [t1], [t2], [root]
        while stack1 or stack2:
            one, two, node = stack1.pop(), stack2.pop(), stack.pop()

            node.val = (one and one.val or 0) + (two and two.val or 0)

            if (one and one.left) or (two and two.left):
                stack1.append(one and one.left)
                stack2.append(two and two.left)
                node.left = TreeNode(None)
                stack.append(node.left)
            if (one and one.right) or (two and two.right):
                stack1.append(one and one.right)
                stack2.append(two and two.right)
                node.right = TreeNode(None)
                stack.append(node.right)

        return root
