class MyLinkedList:

    def __init__(self):
        self.ll = []

    def get(self, index: int) -> int:
        if index < len(self.ll):
            return self.ll[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.ll.insert(0,val)

    def addAtTail(self, val: int) -> None:
        self.ll.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.ll):
            self.ll.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.ll):
            self.ll.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)