class MyLinkedList:
    class Node:
        def __init__(self,val:int):
            self.val = val
            self.next = None

    def __init__(self):
        self.sentinal = self.Node(None)
        self.size = 0

    def is_empty(self):
        return self.size == 0    

    def get(self, index: int) -> int:
        if self.is_empty(): return -1
        if index < 0 or index >= self.size :return -1
        if index == 0 : return self.sentinal.next.val
        curr = self.sentinal.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        # what if its holding a value
        node.next = self.sentinal.next
        # now again point it to head
        self.sentinal.next = node
        self.size +=1 

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)
        if self.is_empty():
            self.addAtHead(val)
            return
        self.size +=1 
        curr = self.sentinal.next
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size :return 
        if index < 0:
            self.addAtHead(val)
            return
        node = self.Node(val)
        curr = self.sentinal
        for _ in range(index):
            curr = curr.next
        node.next = curr.next
        curr.next = node 
        self.size +=1 

       
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return            
        curr = self.sentinal
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1       



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)