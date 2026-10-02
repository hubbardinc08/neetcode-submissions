# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        visited.append(head)

        if (head is None):
            return False

        head = head.next

        while (head is not None):
            if (head in visited):
                return True
            
            visited.append(head)
            head = head.next
        
        return False