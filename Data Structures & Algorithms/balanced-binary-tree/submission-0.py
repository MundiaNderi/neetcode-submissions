# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     # calculate the height of the tree
    def height(self, node):
        if not node:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # height of the tree
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)



