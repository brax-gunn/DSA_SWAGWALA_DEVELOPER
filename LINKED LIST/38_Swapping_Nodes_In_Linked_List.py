class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        totalNodes = 0
        currentNode = head
        while currentNode:
            totalNodes += 1
            if totalNodes == k:
                firstNode = currentNode
            currentNode = currentNode.next
        
        currentIndex = 0
        currentNode = head
        while currentNode:
            currentIndex+=1
            if currentIndex == totalNodes - k + 1:
                secondNode = currentNode
            currentNode = currentNode.next
                
        tempVal = firstNode.val
        firstNode.val = secondNode.val
        secondNode.val = tempVal
        
        return head