class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # revert children
        root.left, root.right = root.right, root.left
        # recursion
        if root.left is not None:
            self.invertBinaryTree(root.left)
        if root.right is not None:
            self.invertBinaryTree(root.right)
