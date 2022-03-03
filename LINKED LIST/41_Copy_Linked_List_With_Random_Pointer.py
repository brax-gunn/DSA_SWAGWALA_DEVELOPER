class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = {}
        
        dummyNode = Node(-1)
        
        prevNode = dummyNode
        oldPointer = head
        
        while oldPointer:
            newNode = Node(oldPointer.val)
            prevNode.next = newNode
            
            if oldPointer not in memo:
                memo[oldPointer] = newNode
            
            prevNode = newNode
            oldPointer = oldPointer.next
            
        prevNode =  dummyNode
        oldPointer = head
        newPointer = dummyNode.next
        while newPointer:
            if oldPointer.random in memo:
                newPointer.random = memo[oldPointer.random]
            oldPointer = oldPointer.next
            newPointer = newPointer.next
            
        return dummyNode.next