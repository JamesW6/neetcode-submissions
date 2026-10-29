# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        length=1
        while curr.next!=None:
            length+=1
            curr=curr.next
        curr=head
        if length-n==0:
            return head.next
        count=1
        while count<length-n:
            count+=1
            curr=curr.next
        curr.next=curr.next.next
        return head