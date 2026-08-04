# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left and root.right:
                return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1
            elif root.right:
                if self.maxDepth(root.right)>1:
                    return False
                else:
                    return True
            elif root.left:
                if self.maxDepth(root.left)>1:
                    return False
                else:
                    return True
        return True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(self.maxDepth(root.right)+1, self.maxDepth(root.left)+1)
        return 0