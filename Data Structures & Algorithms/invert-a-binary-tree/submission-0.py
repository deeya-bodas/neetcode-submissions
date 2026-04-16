# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def swapper(parent: Optional[TreeNode]):
            if parent == None:
                return
            else:
                temp = parent.left
                parent.left = parent.right
                parent.right = temp

                swapper(parent.left)
                swapper(parent.right)

        swapper(root)
        return root
        