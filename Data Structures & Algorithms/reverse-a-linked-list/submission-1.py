# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        saved=head.next
        head.next=None
        while saved!=None:
            new=saved
            saved=saved.next
            new.next=head
            head=new
        return new