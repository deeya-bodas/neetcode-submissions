# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
            if node is None and subNode is None:
                return True
            if node is None or subNode is None:
                return False
            elif node.val != subNode.val:
                return False
            else:
                return isSameTree(node.left, subNode.left) and isSameTree(node.right, subNode.right)
            
        if root is None and subRoot is None:
            return True
        elif subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)