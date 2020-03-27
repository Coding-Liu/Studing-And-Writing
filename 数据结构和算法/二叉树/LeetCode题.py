# Invert Binary Tree（翻转二叉树）


class Solution:
    def invert_tree(self, root):
        if root:
            root.lchild, root.rchild = root.rchild, root.lchild
            self.invert_tree(root.lchild)
            self.invert_tree(root.rchild)
        return root


# Maximum Depth of Binary Tree（二叉树的最大深度）


class Solution:
    def max_depth(self, root):
        if not root:
            return 0
        else:
            left_depth = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            if left_depth > right_depth:
                depth = left_depth
            else:
                depth = right_depth
            return depth + 1
