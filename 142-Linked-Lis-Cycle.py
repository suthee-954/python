# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        s = set()
        while(l is not None):
            if(l in s):
                return l
            else:  
                s.add(l)  
            l = l.next
        return None      
