# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        if(list1.val>list2.val):
            listHead=list2
            list2=list2.next
        else:
            listHead=list1
            list1=list1.next
        currNode=listHead
        while list1!=None and list2!=None:
            if list1.val>list2.val:
                currNode.next=list2
                currNode=currNode.next
                list2=list2.next
            else:
                currNode.next=list1
                currNode=currNode.next
                list1=list1.next
        while list1!=None:
            currNode.next=list1
            currNode=currNode.next
            list1=list1.next
        while list2!=None:
            currNode.next=list2
            currNode=currNode.next
            list2=list2.next
        return listHead
        