# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
            
        prev = None
        this = head
        n = head.next

        while this != None :
            this.next = prev
            prev = this
            this = n
            if(n != None):
                n = n.next

        return prev