class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        prevNode = head
        currentNode = head.next
        
        while prevNode and currentNode:
            tempVal = prevNode.val
            prevNode.val = currentNode.val
            currentNode.val = tempVal
            
            prevNode = currentNode.next
            if currentNode.next:
                currentNode = currentNode.next.next
            
        return head