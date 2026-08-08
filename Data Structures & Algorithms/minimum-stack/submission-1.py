class Node:
    def __init__(self, val, next_node=None):
        self.next=next_node
        self.val=val

class MinStack:

    def __init__(self):
        self.head=None
        self.min_stack=None

    def push(self, val: int) -> None:
        if self.head:
            new_head=Node(val, self.head)
            self.head=new_head
            if val<=self.min_stack.val:
                new_min=Node(val,self.min_stack)
                self.min_stack=new_min
            if not self.min_stack.next:
                temp=Node(val, None)
                self.min_stack.next=temp
        else:
            self.head=Node(val)
            self.min_stack=Node(val)
            print(self.head.val)

    def pop(self) -> None:
        if self.min_stack.val==self.head.val:
            self.min_stack=self.min_stack.next
        self.head=self.head.next
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_stack.val
        
