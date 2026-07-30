# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes={}
        i=0
        while head!=None:
            if head in seenNodes:
                return True
            seenNodes[head]=i
            head=head.next
            i+=1
        return False