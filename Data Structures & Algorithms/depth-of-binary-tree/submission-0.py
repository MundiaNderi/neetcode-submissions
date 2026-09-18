# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth of a tree = 1 + maximum depth of its 
        # left and right subtrees.
        # If a node is None, its depth is 0.

        if not root:
            return 0

        # recursively compute the depth of the left subtree
        leftDepth = self.maxDepth(root.left)

        # recursively compute the depth of the right subtree
        rightDepth = self.maxDepth(root.right)

        depth = 1 + max(leftDepth, rightDepth)

        return depth



