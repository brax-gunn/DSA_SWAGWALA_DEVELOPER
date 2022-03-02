class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-101)
        dummyNode.next = head
        
        prevNode = dummyNode
        currentNode = head
        
        while currentNode is not None:
            if currentNode.val == prevNode.val:
                currentNode = currentNode.next
            else:
                prevNode.next = currentNode
                prevNode = prevNode.next
                currentNode = currentNode.next
        prevNode.next = None
        
        return dummyNode.next