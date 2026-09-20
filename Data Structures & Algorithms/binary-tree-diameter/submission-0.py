# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path between any two nodes in a tree
        # path can not include the same node twice.
        # path does not necessarily have to pass through the root.
        # height = 1 + max(left, right)
        # diameter = left + right

        self.res = 0;

        # returns height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res




