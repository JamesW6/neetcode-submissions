# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root):
            if type(root.val)!=type(" "):
                root.val="0"
            if root.left and root.right:
                root.right.val=str(int(root.val)+1)
                root.left.val=root.right.val
                right_depth=self.diameterOfBinaryTree(root.right)+1
                left_depth=self.diameterOfBinaryTree(root.left)+1
                return max(right_depth, left_depth, left_depth+right_depth-int(root.val))
            elif root.right:
                root.right.val=str(int(root.val)+1)
                return self.diameterOfBinaryTree(root.right)+1
            elif root.left:
                root.left.val=str(int(root.val)+1)
                return self.diameterOfBinaryTree(root.left)+1
        return 0
