class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def countNodes(head):
            curr = head
            count = 0
            while curr is not None:
                curr = curr.next 
                count += 1
            return count 
        
        if head is None:
            return head

        N = countNodes(head)
        indexToStop = N - n - 1
        
        # Case where we need to remove the head node
        if indexToStop < 0:
            return head.next
        
        i = 0
        dummy = head
        
        while i != indexToStop and dummy is not None:
            dummy = dummy.next
            i += 1 
        
        if dummy is not None and dummy.next is not None:
            dummy.next = dummy.next.next 

        return head