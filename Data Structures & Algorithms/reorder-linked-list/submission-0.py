# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        #step 1: find middle of linked list

        slow=fast=head
        
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #split the list
        second=slow.next
        slow.next=None


        #step 2:reverse seond half

        prev=None
        curr=second

        while curr is not None:
            tmp=curr.next
            curr.next=prev

            prev=curr
            curr=tmp
        

        #step 3:interleave:

        first=head
        
        while prev is not None:
            tmp1=first.next
            tmp2=prev.next

            first.next=prev
            prev.next=tmp1

            first=tmp1
            prev=tmp2







        


        
        


        