class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge2Lists(left, right)

    def merge2Lists(self, list1, list2):
        dummy = ListNode(-1)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next= list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
    
        if list2:
            curr.next = list2

        return dummy.next