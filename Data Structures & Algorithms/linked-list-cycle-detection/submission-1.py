# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if curr and curr.next:
            nextN = curr.next
            while curr and nextN:
                if nextN == curr:
                    return True
                else:
                    if curr.next:
                        curr = curr.next
                    else:
                        return False
                    if nextN.next:
                        nextN = nextN.next.next
                    else:
                        return False
            return False
        return False




        