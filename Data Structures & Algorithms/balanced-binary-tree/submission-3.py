# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
                return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1
        return True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(self.maxDepth(root.right)+1, self.maxDepth(root.left)+1)
        return 0