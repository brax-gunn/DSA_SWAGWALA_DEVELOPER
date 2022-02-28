class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        dummyNode = ListNode(-101)
        head = dummyNode
        
        while list1 is not None and list2 is not None:
            
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                dummyNode.next = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                dummyNode.next = newNode
                list2 = list2.next
            
            dummyNode = dummyNode.next
        
        if list1 is not None:
            dummyNode.next = list1
            
        if list2 is not None:
            dummyNode.next = list2
            
        return head.next