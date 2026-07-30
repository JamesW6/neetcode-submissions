# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes=set()
        seenNodes.add(head)
        i=1
        while head!=None:
            if head.next in seenNodes:
                return True
            seenNodes.add(head)
            head=head.next
            i+=1
        return False