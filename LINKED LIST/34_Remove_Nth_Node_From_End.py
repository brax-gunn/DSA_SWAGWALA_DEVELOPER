class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        totalNodes = 0
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        currentNode = dummyNode
        
        while currentNode is not None:
            totalNodes+=1
            currentNode = currentNode.next
        
        currentIndex = 1
        currentNode = dummyNode
        while currentIndex < totalNodes-n:
            currentIndex+=1
            currentNode = currentNode.next
            
        if currentNode.next is not None:
            currentNode.next = currentNode.next.next
        else:
            currentNode.next = None
        
        return dummyNode.next