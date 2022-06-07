# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = dict()
        
        while head:
            if visited.get(head, 0):
                return True
            visited[head] = 1
            head = head.next
            
        return False
            
        