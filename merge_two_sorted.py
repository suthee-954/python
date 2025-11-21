# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          dummy = ListNode(-1,None)
          temp = dummy
          list11=list1
          list22=list2
          while(list11 is not None and list22  is not None ):
            if list11.val <= list22.val:
                temp.next = list11
                temp = list11
                list11 = list11.next
            elif list22.val<list11.val:
                temp.next = list22
                temp = list22
                list22=list22.next
          if list11 is not None:
            temp.next = list11
          elif list22 is not None:
            temp.next = list22

          return dummy.next          






          
               





            

                                   
