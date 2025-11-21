# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        temp.next=head
        
        count = 0

        temp2=head
        total = 0
        while (temp2!=None):
            total+=1
            temp2= temp2.next
            
        n1=total-(n-1)
        while(temp.next is not None):
            prev = temp
            cur =temp.next
            count+=1
            if count == n1:
                prev.next=cur.next
                cur.next = None
                temp = prev.next
                break
            temp=temp.next
        return dummy.next        
