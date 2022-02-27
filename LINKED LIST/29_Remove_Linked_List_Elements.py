class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        currentNode = head
        prevNode = dummyNode
        
        while currentNode is not None:
            
            if currentNode.val == val:
                prevNode.next = currentNode.next
            else:
                prevNode = currentNode
                
            currentNode = currentNode.next
                
        return dummyNode.next