class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentIndex = 1
        currentNode = head
        
        dummyNode = ListNode(-1)
        prevNode = dummyNode

        while currentNode:
            if currentIndex % 2 == 1:
                newNode = ListNode(currentNode.val)
                prevNode.next = newNode
                
                prevNode = newNode
            currentIndex += 1
            currentNode = currentNode.next
        
    
        currentIndex = 1
        currentNode = head

        while currentNode:
            if currentIndex % 2 == 0:
                newNode = ListNode(currentNode.val)
                prevNode.next = newNode
                
                prevNode = newNode
            currentIndex += 1
            currentNode = currentNode.next
            
        return dummyNode.next