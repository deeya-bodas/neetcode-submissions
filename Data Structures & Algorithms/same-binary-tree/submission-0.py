# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check_subtree(p_ptr, q_ptr):
            if p_ptr is None and q_ptr is None:
                return True
            elif p_ptr is None and q_ptr is not None:
                return False
            elif p_ptr is not None and q_ptr is None:
                return False
            elif p_ptr.val == q_ptr.val:
                return check_subtree(p_ptr.left, q_ptr.left) and check_subtree(p_ptr.right, q_ptr.right)
            else:
                return False

        return check_subtree(p, q)

        