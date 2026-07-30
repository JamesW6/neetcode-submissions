# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):
            return root
        temp=root.right
        if root.left!=None:
            root.right=root.left
            self.invertTree(root.right)
        else:
            root.right=None
        if temp!=None:
            root.left=temp
            self.invertTree(root.left)
        else:
            root.left=None            
        return root