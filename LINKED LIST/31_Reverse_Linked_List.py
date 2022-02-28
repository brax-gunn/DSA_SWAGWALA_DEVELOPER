class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevNode = None
        currentNode = head
        
        while currentNode is not None:
            tempNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            
            currentNode = tempNode
        
        return prevNode