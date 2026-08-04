# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            root=self.findNode(root,subRoot)
            if root:
                if self.isEqual(root,subRoot):
                    return True
                else:
                    return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left,subRoot)
        return False
    def isEqual(self, p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        elif p.val==q.val:
            return self.isEqual(p.left,q.left) and self.isEqual(p.right,q.right)
        else:
            return False
    def findNode(self, root:Optional[TreeNode], subRoot:Optional[TreeNode]) -> Optional[TreeNode]:
        if root!=None:
            if root.val==subRoot.val:
                return root
            else:
                checkLeft=self.findNode(root.left, subRoot)
                checkRight=self.findNode(root.right, subRoot)
                if checkLeft!=None and checkLeft.val==subRoot.val:
                    return checkLeft
                elif checkRight!=None and checkRight.val==subRoot.val:
                    return checkRight
        return None